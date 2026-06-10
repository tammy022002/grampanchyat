from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.shared.utils.pagination import PaginatedParams, PaginatedResponse
from app.shared.responses.base import BaseResponse
from app.modules.works.schemas import *
from app.modules.works.services import WorksService

router = APIRouter()

@router.get("/estimates", response_model=BaseResponse[PaginatedResponse[WorkEstimateResponse]])
def get_estimates(params: PaginatedParams = Depends(), db: Session = Depends(get_db)):
    items = WorksService.get_estimates(db, params.skip, params.limit)
    total = len(items)
    return BaseResponse(data=PaginatedResponse(items=items, total=total, page=params.page, size=params.size, pages=1))

@router.post("/estimates", response_model=BaseResponse[WorkEstimateResponse])
def create_estimate(estimate_in: WorkEstimateCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=WorksService.create_estimate(db, estimate_in), message="Estimate created")

@router.post("/measurements", response_model=BaseResponse[MeasurementBookResponse])
def create_measurement(measurement_in: MeasurementBookCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=WorksService.create_measurement(db, measurement_in), message="Measurement created")

@router.post("/bills", response_model=BaseResponse[WorkBillResponse])
def create_bill(bill_in: WorkBillCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=WorksService.create_bill(db, bill_in), message="Bill created")
