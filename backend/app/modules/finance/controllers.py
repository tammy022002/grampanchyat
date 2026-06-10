from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.shared.utils.pagination import PaginatedParams, PaginatedResponse
from app.shared.responses.base import BaseResponse
from app.modules.finance.schemas import *
from app.modules.finance.services import FinanceService

router = APIRouter()

# BUDGET
@router.get("/budgets", response_model=BaseResponse[PaginatedResponse[BudgetMasterResponse]])
def get_budgets(params: PaginatedParams = Depends(), db: Session = Depends(get_db)):
    items = FinanceService.get_budgets(db, params.skip, params.limit)
    total = len(items) if len(items) < params.limit else params.limit * 10
    pages = (total // params.size) + (1 if total % params.size > 0 else 0)
    return BaseResponse(data=PaginatedResponse(items=items, total=total, page=params.page, size=params.size, pages=pages))

@router.post("/budgets", response_model=BaseResponse[BudgetMasterResponse])
def create_budget(budget_in: BudgetMasterCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=FinanceService.create_budget(db, budget_in), message="Budget created successfully")

# CASHBOOK
@router.get("/cashbook", response_model=BaseResponse[PaginatedResponse[CashbookResponse]])
def get_cashbook(params: PaginatedParams = Depends(), db: Session = Depends(get_db)):
    items = FinanceService.get_cashbook_entries(db, params.skip, params.limit)
    total = len(items) if len(items) < params.limit else params.limit * 10
    pages = (total // params.size) + (1 if total % params.size > 0 else 0)
    return BaseResponse(data=PaginatedResponse(items=items, total=total, page=params.page, size=params.size, pages=pages))

@router.post("/cashbook", response_model=BaseResponse[CashbookResponse])
def create_cashbook_entry(cashbook_in: CashbookCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=FinanceService.create_cashbook_entry(db, cashbook_in), message="Cashbook entry created")

# RECEIPTS
@router.get("/receipts", response_model=BaseResponse[PaginatedResponse[ReceiptResponse]])
def get_receipts(params: PaginatedParams = Depends(), db: Session = Depends(get_db)):
    items = FinanceService.get_receipts(db, params.skip, params.limit)
    total = len(items) if len(items) < params.limit else params.limit * 10
    pages = (total // params.size) + (1 if total % params.size > 0 else 0)
    return BaseResponse(data=PaginatedResponse(items=items, total=total, page=params.page, size=params.size, pages=pages))

@router.post("/receipts", response_model=BaseResponse[ReceiptResponse])
def create_receipt(receipt_in: ReceiptCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=FinanceService.create_receipt(db, receipt_in), message="Receipt generated successfully")
