from sqlalchemy.orm import Session
from typing import List
from app.modules.employees.repositories import attendance_repo, salary_payment_repo, travel_allowance_repo
from app.modules.employees.schemas import *
from app.core.exceptions import BusinessRuleException

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
        # Validate net salary calculation
        expected_net = salary_in.gross_salary - salary_in.deductions
        if abs(expected_net - salary_in.net_salary) > 0.01:
            raise BusinessRuleException("Net salary does not match gross minus deductions")
            
        obj = salary_payment_repo.create(db, salary_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def create_travel_allowance(db: Session, ta_in: TravelAllowanceCreate) -> TravelAllowanceResponse:
        obj = travel_allowance_repo.create(db, ta_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj
