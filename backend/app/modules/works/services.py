from sqlalchemy.orm import Session
from typing import List
from app.modules.works.repositories import work_estimate_repo, measurement_book_repo, work_bill_repo
from app.modules.works.schemas import *
from app.core.exceptions import BusinessRuleException

class WorksService:
    @staticmethod
    def get_estimates(db: Session, skip: int, limit: int) -> List[WorkEstimateResponse]:
        return work_estimate_repo.get_all(db, skip, limit)

    @staticmethod
    def create_estimate(db: Session, estimate_in: WorkEstimateCreate) -> WorkEstimateResponse:
        obj = work_estimate_repo.create(db, estimate_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def create_measurement(db: Session, measurement_in: MeasurementBookCreate) -> MeasurementBookResponse:
        obj = measurement_book_repo.create(db, measurement_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def create_bill(db: Session, bill_in: WorkBillCreate) -> WorkBillResponse:
        # Business rule logic here e.g., Bill amount shouldn't exceed estimated cost
        obj = work_bill_repo.create(db, bill_in.model_dump())
        
        # Post automatic accounting transaction
        from app.modules.finance.services import FinanceService
        work_est = work_estimate_repo.get_by_id(db, bill_in.work_id)
        work_name = work_est.work_name if work_est else "Development Work"
        account_head = "Road Construction" if "road" in work_name.lower() else "Public Works"
        
        FinanceService.post_accounting_transaction(
            db=db,
            tx_date=bill_in.bill_date,
            voucher_no=f"V-BILL-{obj.bill_id}",
            receipt_amount=0.0,
            payment_amount=bill_in.amount,
            account_head=account_head,
            narration=f"Expense: Payment for Work Bill #{obj.bill_id} ({work_name})"
        )
        
        db.commit()
        db.refresh(obj)
        return obj
