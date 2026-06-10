from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.shared.utils.pagination import PaginatedParams, PaginatedResponse
from app.shared.responses.base import BaseResponse
from app.modules.masters.schemas import *
from app.modules.masters.services import MastersService

router = APIRouter()

# VILLAGES
@router.get("/villages", response_model=BaseResponse[PaginatedResponse[VillageMasterResponse]])
def get_villages(
    params: PaginatedParams = Depends(),
    db: Session = Depends(get_db)
):
    items = MastersService.get_villages(db, params.skip, params.limit)
    # Mock total count for simplicity in this boiler, should be queried in prod
    total = len(items) if len(items) < params.limit else params.limit * 10
    pages = (total // params.size) + (1 if total % params.size > 0 else 0)
    
    return BaseResponse(
        data=PaginatedResponse(
            items=items,
            total=total,
            page=params.page,
            size=params.size,
            pages=pages
        )
    )

@router.post("/villages", response_model=BaseResponse[VillageMasterResponse])
def create_village(village_in: VillageMasterCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=MastersService.create_village(db, village_in), message="Village created successfully")

@router.put("/villages/{village_id}", response_model=BaseResponse[VillageMasterResponse])
def update_village(village_id: int, village_in: VillageMasterUpdate, db: Session = Depends(get_db)):
    return BaseResponse(data=MastersService.update_village(db, village_id, village_in), message="Village updated successfully")

# EMPLOYEES
@router.get("/employees", response_model=BaseResponse[PaginatedResponse[EmployeeMasterResponse]])
def get_employees(params: PaginatedParams = Depends(), db: Session = Depends(get_db)):
    items = MastersService.get_employees(db, params.skip, params.limit)
    total = len(items) if len(items) < params.limit else params.limit * 10
    pages = (total // params.size) + (1 if total % params.size > 0 else 0)
    return BaseResponse(data=PaginatedResponse(items=items, total=total, page=params.page, size=params.size, pages=pages))

@router.post("/employees", response_model=BaseResponse[EmployeeMasterResponse])
def create_employee(employee_in: EmployeeMasterCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=MastersService.create_employee(db, employee_in), message="Employee created successfully")

# FINANCIAL YEARS
@router.get("/financial-years", response_model=BaseResponse[PaginatedResponse[FinancialYearMasterResponse]])
def get_financial_years(params: PaginatedParams = Depends(), db: Session = Depends(get_db)):
    items = MastersService.get_financial_years(db, params.skip, params.limit)
    total = len(items) if len(items) < params.limit else params.limit * 10
    pages = (total // params.size) + (1 if total % params.size > 0 else 0)
    return BaseResponse(data=PaginatedResponse(items=items, total=total, page=params.page, size=params.size, pages=pages))

@router.post("/financial-years", response_model=BaseResponse[FinancialYearMasterResponse])
def create_financial_year(fy_in: FinancialYearMasterCreate, db: Session = Depends(get_db)):
    return BaseResponse(data=MastersService.create_financial_year(db, fy_in), message="Financial Year created successfully")
