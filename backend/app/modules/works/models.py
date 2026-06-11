from sqlalchemy import Column, Integer, String, Date, Numeric, Text, ForeignKey
from app.core.database import Base

class WorkEstimate(Base):
    __tablename__ = 'work_estimate'
    
    estimate_id = Column(Integer, primary_key=True, autoincrement=True)
    work_name = Column(String(255))
    estimated_cost = Column(Numeric(15, 2))
    estimate_date = Column(Date)
    engineer_name = Column(String(255))

class MeasurementBook(Base):
    __tablename__ = 'measurement_book'
    
    measurement_id = Column(Integer, primary_key=True, autoincrement=True)
    work_id = Column(Integer, ForeignKey('work_estimate.estimate_id', ondelete='CASCADE'))
    measurement_date = Column(Date)
    quantity = Column(Numeric(10, 2))
    remarks = Column(Text)

class WorkBill(Base):
    __tablename__ = 'work_bill'
    
    bill_id = Column(Integer, primary_key=True, autoincrement=True)
    work_id = Column(Integer, ForeignKey('work_estimate.estimate_id', ondelete='CASCADE'))
    contractor_name = Column(String(255))
    amount = Column(Numeric(15, 2))
    bill_date = Column(Date)
