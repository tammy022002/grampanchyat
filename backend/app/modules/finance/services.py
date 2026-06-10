from sqlalchemy.orm import Session
from typing import List
from app.modules.finance.repositories import budget_repo, cashbook_repo, receipt_repo
from app.modules.finance.schemas import *
from app.core.exceptions import BusinessRuleException

class FinanceService:
    @staticmethod
    def get_budgets(db: Session, skip: int, limit: int) -> List[BudgetMasterResponse]:
        return budget_repo.get_all(db, skip, limit)

    @staticmethod
    def create_budget(db: Session, budget_in: BudgetMasterCreate) -> BudgetMasterResponse:
        # Example Business Rule Validation
        if budget_in.estimated_expenditure < 0 or budget_in.estimated_receipts < 0:
            raise BusinessRuleException("Estimates cannot be negative")
            
        obj = budget_repo.create(db, budget_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_cashbook_entries(db: Session, skip: int, limit: int) -> List[CashbookResponse]:
        return cashbook_repo.get_all(db, skip, limit)

    @staticmethod
    def create_cashbook_entry(db: Session, cashbook_in: CashbookCreate) -> CashbookResponse:
        # Voucher verification logic would go here
        if not cashbook_in.voucher_no:
            raise BusinessRuleException("Voucher number is required for Cashbook entry")
            
        obj = cashbook_repo.create(db, cashbook_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_receipts(db: Session, skip: int, limit: int) -> List[ReceiptResponse]:
        return receipt_repo.get_all(db, skip, limit)

    @staticmethod
    def create_receipt(db: Session, receipt_in: ReceiptCreate) -> ReceiptResponse:
        obj = receipt_repo.create(db, receipt_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj
