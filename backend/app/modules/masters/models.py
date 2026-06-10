from sqlalchemy import Column, Integer, String, Date, Numeric
from app.core.database import Base

class VillageMaster(Base):
    __tablename__ = 'village_master'
    
    village_id = Column(Integer, primary_key=True, autoincrement=True)
    village_name = Column(String(255))
    gram_panchayat_name = Column(String(255))
    taluka = Column(String(255))
    district = Column(String(255))

class EmployeeMaster(Base):
    __tablename__ = 'employee_master'
    
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    employee_name = Column(String(255))
    designation = Column(String(255))
    joining_date = Column(Date)
    salary = Column(Numeric(15, 2))
    status = Column(String(50))

class FinancialYearMaster(Base):
    __tablename__ = 'financial_year_master'
    
    fy_id = Column(Integer, primary_key=True, autoincrement=True)
    fy_year = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date)
