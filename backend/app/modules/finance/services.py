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
        
        # Post automatic accounting transaction
        FinanceService.post_accounting_transaction(
            db=db,
            tx_date=receipt_in.receipt_date,
            voucher_no=receipt_in.receipt_no,
            receipt_amount=receipt_in.amount,
            payment_amount=0.0,
            account_head=receipt_in.purpose,
            narration=f"Income: {receipt_in.purpose} from {receipt_in.payer_name}"
        )
        
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def post_accounting_transaction(
        db: Session,
        tx_date,
        voucher_no: str,
        receipt_amount: float,
        payment_amount: float,
        account_head: str,
        narration: str
    ):
        from app.modules.finance.models import Cashbook, Ledger
        
        # Fetch last cashbook entry to compute closing balance
        last_cashbook = db.query(Cashbook).order_by(Cashbook.entry_id.desc()).first()
        prev_balance = float(last_cashbook.balance) if last_cashbook else 0.0
        new_balance = prev_balance + float(receipt_amount) - float(payment_amount)
        
        cashbook_entry = Cashbook(
            transaction_date=tx_date,
            voucher_no=voucher_no,
            receipt_amount=receipt_amount,
            payment_amount=payment_amount,
            balance=new_balance,
            narration=narration
        )
        db.add(cashbook_entry)
        
        # Fetch last ledger entry for this account head to compute closing balance
        last_ledger = db.query(Ledger).filter(Ledger.account_head == account_head).order_by(Ledger.ledger_id.desc()).first()
        prev_ledger_balance = float(last_ledger.balance) if last_ledger else 0.0
        new_ledger_balance = prev_ledger_balance + float(receipt_amount) - float(payment_amount)
        
        ledger_entry = Ledger(
            account_head=account_head,
            transaction_date=tx_date,
            debit=payment_amount,
            credit=receipt_amount,
            balance=new_ledger_balance
        )
        db.add(ledger_entry)
        db.flush()
