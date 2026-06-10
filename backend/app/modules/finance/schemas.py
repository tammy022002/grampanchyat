from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

# Budget
class BudgetMasterBase(BaseModel):
    financial_year: str
    department: str
    account_head: str
    estimated_receipts: float
    estimated_expenditure: float
    approved_by: str
    approved_date: date

class BudgetMasterCreate(BudgetMasterBase):
    pass

class BudgetMasterResponse(BudgetMasterBase):
    budget_id: int
    model_config = ConfigDict(from_attributes=True)

# Cashbook
class CashbookBase(BaseModel):
    transaction_date: date
    voucher_no: str
    receipt_amount: float
    payment_amount: float
    balance: float
    narration: str

class CashbookCreate(CashbookBase):
    pass

class CashbookResponse(CashbookBase):
    entry_id: int
    model_config = ConfigDict(from_attributes=True)

# Receipt
class ReceiptBase(BaseModel):
    receipt_no: str
    receipt_date: date
    payer_name: str
    amount: float
    purpose: str
    payment_mode: str

class ReceiptCreate(ReceiptBase):
    pass

class ReceiptResponse(ReceiptBase):
    receipt_id: int
    model_config = ConfigDict(from_attributes=True)
