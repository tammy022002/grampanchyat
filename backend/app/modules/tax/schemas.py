from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

class TaxAssessmentBase(BaseModel):
    property_no: str
    owner_name: str
    tax_type: str
    annual_value: float
    tax_amount: float

class TaxAssessmentCreate(TaxAssessmentBase):
    pass

class TaxAssessmentResponse(TaxAssessmentBase):
    assessment_id: int
    model_config = ConfigDict(from_attributes=True)

class TaxDemandBase(BaseModel):
    assessment_id: int
    demand_year: str
    amount_due: float
    due_date: date

class TaxDemandCreate(TaxDemandBase):
    pass

class TaxDemandResponse(TaxDemandBase):
    demand_id: int
    model_config = ConfigDict(from_attributes=True)

class TaxReceiptBase(BaseModel):
    receipt_no: str
    taxpayer_id: int
    tax_type: str
    amount: float
    receipt_date: date

class TaxReceiptCreate(TaxReceiptBase):
    pass

class TaxReceiptResponse(TaxReceiptBase):
    tax_receipt_id: int
    model_config = ConfigDict(from_attributes=True)
