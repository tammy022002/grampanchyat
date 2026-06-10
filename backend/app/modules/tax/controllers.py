from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.shared.utils.pagination import PaginatedParams, PaginatedResponse
from app.shared.responses.base import BaseResponse
from app.modules.tax.schemas import *
from app.modules.tax.services import TaxService

router = APIRouter()

@router.get("/assessments", response_model=BaseResponse[PaginatedResponse[TaxAssessmentResponse]])
def get_assessments(params: PaginatedParams = Depends(), db: Session = Depends(get_db)):
    items = TaxService.get_assessments(db, params.skip, params.limit)
    total = len(items)
    return BaseResponse(data=PaginatedResponse(items=items, total=total, page=params.page, size=params.size, pages=1))

@router.post("/assessments", response_model=BaseResponse[TaxAssessmentResponse])
def create_assessment(assessment_in: TaxAssessmentCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=TaxService.create_assessment(db, assessment_in), message="Tax Assessment created")

@router.get("/demands", response_model=BaseResponse[PaginatedResponse[TaxDemandResponse]])
def get_demands(params: PaginatedParams = Depends(), db: Session = Depends(get_db)):
    items = TaxService.get_demands(db, params.skip, params.limit)
    total = len(items)
    return BaseResponse(data=PaginatedResponse(items=items, total=total, page=params.page, size=params.size, pages=1))

@router.post("/demands", response_model=BaseResponse[TaxDemandResponse])
def create_demand(demand_in: TaxDemandCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=TaxService.create_demand(db, demand_in), message="Tax Demand created")

@router.post("/receipts", response_model=BaseResponse[TaxReceiptResponse])
def create_tax_receipt(receipt_in: TaxReceiptCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=TaxService.create_tax_receipt(db, receipt_in), message="Tax Receipt generated")
