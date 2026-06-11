from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from app.core.database import Base

class TaxAssessment(Base):
    __tablename__ = 'tax_assessment'
    
    assessment_id = Column(Integer, primary_key=True, autoincrement=True)
    property_no = Column(String(100))
    owner_name = Column(String(255))
    tax_type = Column(String(100))
    annual_value = Column(Numeric(15, 2))
    tax_amount = Column(Numeric(15, 2))

class TaxDemand(Base):
    __tablename__ = 'tax_demand'
    
    demand_id = Column(Integer, primary_key=True, autoincrement=True)
    assessment_id = Column(Integer, ForeignKey('tax_assessment.assessment_id', ondelete='CASCADE'))
    demand_year = Column(String(50))
    amount_due = Column(Numeric(15, 2))
    due_date = Column(Date)

class TaxReceipt(Base):
    __tablename__ = 'tax_receipt'
    
    tax_receipt_id = Column(Integer, primary_key=True, autoincrement=True)
    receipt_no = Column(String(100))
    taxpayer_id = Column(Integer, ForeignKey('tax_assessment.assessment_id', ondelete='CASCADE'))
    tax_type = Column(String(100))
    amount = Column(Numeric(15, 2))
    receipt_date = Column(Date)
