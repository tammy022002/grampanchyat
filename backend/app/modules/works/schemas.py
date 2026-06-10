from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class WorkEstimateBase(BaseModel):
    work_name: str
    estimated_cost: float
    estimate_date: date
    engineer_name: str

class WorkEstimateCreate(WorkEstimateBase):
    pass

class WorkEstimateResponse(WorkEstimateBase):
    estimate_id: int
    model_config = ConfigDict(from_attributes=True)

class MeasurementBookBase(BaseModel):
    work_id: int
    measurement_date: date
    quantity: float
    remarks: str

class MeasurementBookCreate(MeasurementBookBase):
    pass

class MeasurementBookResponse(MeasurementBookBase):
    measurement_id: int
    model_config = ConfigDict(from_attributes=True)

class WorkBillBase(BaseModel):
    work_id: int
    contractor_name: str
    amount: float
    bill_date: date

class WorkBillCreate(WorkBillBase):
    pass

class WorkBillResponse(WorkBillBase):
    bill_id: int
    model_config = ConfigDict(from_attributes=True)
