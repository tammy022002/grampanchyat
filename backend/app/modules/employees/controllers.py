from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.shared.utils.pagination import PaginatedParams, PaginatedResponse
from app.shared.responses.base import BaseResponse
from app.modules.employees.schemas import *
from app.modules.employees.services import EmployeesService

router = APIRouter()

@router.get("/attendance", response_model=BaseResponse[PaginatedResponse[AttendanceResponse]])
def get_attendance(params: PaginatedParams = Depends(), db: Session = Depends(get_db)):
    items = EmployeesService.get_attendances(db, params.skip, params.limit)
    total = len(items)
    return BaseResponse(data=PaginatedResponse(items=items, total=total, page=params.page, size=params.size, pages=1))

@router.post("/attendance", response_model=BaseResponse[AttendanceResponse])
def create_attendance(attendance_in: AttendanceCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=EmployeesService.create_attendance(db, attendance_in), message="Attendance marked")

@router.post("/salary", response_model=BaseResponse[SalaryPaymentResponse])
def process_salary(salary_in: SalaryPaymentCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=EmployeesService.create_salary_payment(db, salary_in), message="Salary processed")

@router.post("/travel-allowance", response_model=BaseResponse[TravelAllowanceResponse])
def request_ta(ta_in: TravelAllowanceCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=EmployeesService.create_travel_allowance(db, ta_in), message="TA requested")
