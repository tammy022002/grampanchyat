from sqlalchemy.orm import Session
from typing import List
from app.modules.tax.repositories import tax_assessment_repo, tax_demand_repo, tax_receipt_repo
from app.modules.tax.schemas import *
from app.core.exceptions import BusinessRuleException, NotFoundException

class TaxService:
    @staticmethod
    def get_assessments(db: Session, skip: int, limit: int) -> List[TaxAssessmentResponse]:
        return tax_assessment_repo.get_all(db, skip, limit)

    @staticmethod
    def create_assessment(db: Session, assessment_in: TaxAssessmentCreate) -> TaxAssessmentResponse:
        obj = tax_assessment_repo.create(db, assessment_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_demands(db: Session, skip: int, limit: int) -> List[TaxDemandResponse]:
        return tax_demand_repo.get_all(db, skip, limit)

    @staticmethod
    def create_demand(db: Session, demand_in: TaxDemandCreate) -> TaxDemandResponse:
        assessment = tax_assessment_repo.get_by_id(db, demand_in.assessment_id)
        if not assessment:
            raise NotFoundException("Tax Assessment not found")
            
        obj = tax_demand_repo.create(db, demand_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def create_tax_receipt(db: Session, receipt_in: TaxReceiptCreate) -> TaxReceiptResponse:
        # Example validation logic: Do not allow over-collection if we had demand tracking logic here
        if receipt_in.amount <= 0:
            raise BusinessRuleException("Receipt amount must be greater than zero")
            
        obj = tax_receipt_repo.create(db, receipt_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj
