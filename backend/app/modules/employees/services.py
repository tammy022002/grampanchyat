from sqlalchemy.orm import Session
from typing import List
import calendar
from datetime import date as py_date
from app.modules.employees.repositories import attendance_repo, salary_payment_repo, travel_allowance_repo
from app.modules.employees.schemas import *
from app.core.exceptions import BusinessRuleException, NotFoundException
from app.modules.masters.repositories import employee_repo
from app.modules.employees.models import Attendance
from app.modules.finance.services import FinanceService

class EmployeesService:
    @staticmethod
    def get_attendances(db: Session, skip: int, limit: int) -> List[AttendanceResponse]:
        return attendance_repo.get_all(db, skip, limit)

    @staticmethod
    def create_attendance(db: Session, attendance_in: AttendanceCreate) -> AttendanceResponse:
        obj = attendance_repo.create(db, attendance_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def create_salary_payment(db: Session, salary_in: SalaryPaymentCreate) -> SalaryPaymentResponse:
        # Fetch employee master to get the base salary
        employee = employee_repo.get_by_id(db, salary_in.employee_id)
        if not employee:
            raise NotFoundException("Employee not found in master records")
            
        base_salary = float(employee.salary) if employee.salary else 0.0
        
        # Parse month and year from salary_month e.g., "October 2026"
        month_map = {
            "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
            "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12
        }
        parts = salary_in.salary_month.strip().lower().split()
        month_num = 10
        year_num = 2026
        if len(parts) == 2:
            m_str, y_str = parts
            if m_str in month_map:
                month_num = month_map[m_str]
            try:
                year_num = int(y_str)
            except ValueError:
                pass
                
        # Query attendance days for the month
        start_date = py_date(year_num, month_num, 1)
        end_date = py_date(year_num, month_num, calendar.monthrange(year_num, month_num)[1])
        
        attendances = db.query(Attendance).filter(
            Attendance.employee_id == salary_in.employee_id,
            Attendance.date >= start_date,
            Attendance.date <= end_date
        ).all()
        
        total_days = calendar.monthrange(year_num, month_num)[1]
        
        if attendances:
            absent_days = sum(1 for a in attendances if a.status.strip().lower() in ['absent', 'leaves', 'lwp'])
            paid_days = max(0, total_days - absent_days)
        else:
            paid_days = total_days
            
        calculated_gross = round((base_salary / total_days) * paid_days, 2)
        deductions = salary_in.deductions if salary_in.deductions > 0.0 else 0.0
        calculated_net = round(calculated_gross - deductions, 2)
        
        creation_dict = salary_in.model_dump()
        
        # Override fields with computed values if they were sent as default 0.0
        if creation_dict.get("gross_salary") == 0.0:
            creation_dict["gross_salary"] = calculated_gross
        if creation_dict.get("net_salary") == 0.0:
            creation_dict["net_salary"] = calculated_net
            
        # Validate calculations
        expected_net = creation_dict["gross_salary"] - creation_dict["deductions"]
        if abs(expected_net - creation_dict["net_salary"]) > 0.01:
            raise BusinessRuleException("Net salary calculation mismatch")
            
        obj = salary_payment_repo.create(db, creation_dict)
        
        # Post automatic accounting transaction (expense)
        FinanceService.post_accounting_transaction(
            db=db,
            tx_date=py_date.today(),
            voucher_no=f"V-SAL-{obj.payment_id}",
            receipt_amount=0.0,
            payment_amount=obj.net_salary,
            account_head="Employee Salary",
            narration=f"Expense: Salary Payment for {employee.employee_name} ({salary_in.salary_month})"
        )
        
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def create_travel_allowance(db: Session, ta_in: TravelAllowanceCreate) -> TravelAllowanceResponse:
        obj = travel_allowance_repo.create(db, ta_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj
