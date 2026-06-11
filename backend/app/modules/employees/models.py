from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from app.core.database import Base

class Attendance(Base):
    __tablename__ = 'attendance'
    
    attendance_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee_master.employee_id', ondelete='CASCADE'))
    work_id = Column(Integer, ForeignKey('work_estimate.estimate_id', ondelete='CASCADE'))
    date = Column(Date)
    status = Column(String(50))

class SalaryPayment(Base):
    __tablename__ = 'salary_payment'
    
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee_master.employee_id', ondelete='CASCADE'))
    work_id = Column(Integer, ForeignKey('work_estimate.estimate_id', ondelete='SET NULL'), nullable=True)
    salary_month = Column(String(50))
    gross_salary = Column(Numeric(15, 2))
    deductions = Column(Numeric(15, 2))
    net_salary = Column(Numeric(15, 2))

class TravelAllowance(Base):
    __tablename__ = 'travel_allowance'
    
    ta_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employee_master.employee_id', ondelete='CASCADE'))
    travel_date = Column(Date)
    source = Column(String(255))
    destination = Column(String(255))
    amount = Column(Numeric(15, 2))
