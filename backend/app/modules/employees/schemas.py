from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class AttendanceBase(BaseModel):
    employee_id: int
    work_name: str
    date: date
    status: str

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    attendance_id: int
    model_config = ConfigDict(from_attributes=True)

class SalaryPaymentBase(BaseModel):
    employee_id: int
    salary_month: str
    gross_salary: float
    deductions: float
    net_salary: float

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
