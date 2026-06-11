from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class AttendanceBase(BaseModel):
    employee_id: int
    work_id: int
    date: date
    status: str

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    attendance_id: int
    model_config = ConfigDict(from_attributes=True)

class SalaryPaymentBase(BaseModel):
    employee_id: int
    work_id: Optional[int] = None
    salary_month: str
    gross_salary: Optional[float] = 0.0
    deductions: Optional[float] = 0.0
    net_salary: Optional[float] = 0.0

class SalaryPaymentCreate(SalaryPaymentBase):
    pass

class SalaryPaymentResponse(SalaryPaymentBase):
    payment_id: int
    model_config = ConfigDict(from_attributes=True)

class TravelAllowanceBase(BaseModel):
    employee_id: int
    travel_date: date
    source: str
    destination: str
    amount: float

class TravelAllowanceCreate(TravelAllowanceBase):
    pass

class TravelAllowanceResponse(TravelAllowanceBase):
    ta_id: int
    model_config = ConfigDict(from_attributes=True)
