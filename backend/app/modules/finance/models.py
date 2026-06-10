from sqlalchemy import Column, Integer, String, Date, Numeric, Text
from app.core.database import Base

class BudgetMaster(Base):
    __tablename__ = 'budget_master'
    
    budget_id = Column(Integer, primary_key=True, autoincrement=True)
    financial_year = Column(String(50))
    department = Column(String(255))
    account_head = Column(String(255))
    estimated_receipts = Column(Numeric(15, 2))
    estimated_expenditure = Column(Numeric(15, 2))
    approved_by = Column(String(255))
    approved_date = Column(Date)

class Cashbook(Base):
    __tablename__ = 'cashbook'
    
    entry_id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_date = Column(Date)
    voucher_no = Column(String(100))
    receipt_amount = Column(Numeric(15, 2))
    payment_amount = Column(Numeric(15, 2))
    balance = Column(Numeric(15, 2))
    narration = Column(Text)

class Ledger(Base):
    __tablename__ = 'ledger'
    
    ledger_id = Column(Integer, primary_key=True, autoincrement=True)
    account_head = Column(String(255))
    transaction_date = Column(Date)
    debit = Column(Numeric(15, 2))
    credit = Column(Numeric(15, 2))
    balance = Column(Numeric(15, 2))

class Receipt(Base):
    __tablename__ = 'receipt'
    
    receipt_id = Column(Integer, primary_key=True, autoincrement=True)
    receipt_no = Column(String(100))
    receipt_date = Column(Date)
    payer_name = Column(String(255))
    amount = Column(Numeric(15, 2))
    purpose = Column(Text)
    payment_mode = Column(String(50))
