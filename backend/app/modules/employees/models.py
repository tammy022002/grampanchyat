from sqlalchemy import Column, Integer, String, Date, Numeric
from app.core.database import Base

class Attendance(Base):
    __tablename__ = 'attendance'
    
    attendance_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer)
    work_name = Column(String(255))
    date = Column(Date)
    status = Column(String(50))

class SalaryPayment(Base):
    __tablename__ = 'salary_payment'
    
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer)
    salary_month = Column(String(50))
    gross_salary = Column(Numeric(15, 2))
    deductions = Column(Numeric(15, 2))
    net_salary = Column(Numeric(15, 2))

class TravelAllowance(Base):
    __tablename__ = 'travel_allowance'
    
    ta_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer)
    travel_date = Column(Date)
    source = Column(String(255))
    destination = Column(String(255))
    amount = Column(Numeric(15, 2))
