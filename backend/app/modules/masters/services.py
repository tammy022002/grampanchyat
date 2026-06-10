from sqlalchemy.orm import Session
from app.modules.masters.repositories import village_repo, employee_repo, fy_repo
from app.modules.masters.schemas import *
from app.core.exceptions import NotFoundException
from typing import List

class MastersService:
    @staticmethod
    def get_villages(db: Session, skip: int, limit: int) -> List[VillageMasterResponse]:
        return village_repo.get_all(db, skip, limit)

    @staticmethod
    def create_village(db: Session, village_in: VillageMasterCreate) -> VillageMasterResponse:
        obj = village_repo.create(db, village_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def update_village(db: Session, village_id: int, village_in: VillageMasterUpdate) -> VillageMasterResponse:
        db_obj = village_repo.get_by_id(db, village_id)
        if not db_obj:
            raise NotFoundException("Village not found")
        obj = village_repo.update(db, db_obj, village_in.model_dump(exclude_unset=True))
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_employees(db: Session, skip: int, limit: int) -> List[EmployeeMasterResponse]:
        return employee_repo.get_all(db, skip, limit)

    @staticmethod
    def create_employee(db: Session, employee_in: EmployeeMasterCreate) -> EmployeeMasterResponse:
        obj = employee_repo.create(db, employee_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj

    # Same pattern for Financial Year etc.
    @staticmethod
    def get_financial_years(db: Session, skip: int, limit: int) -> List[FinancialYearMasterResponse]:
        return fy_repo.get_all(db, skip, limit)

    @staticmethod
    def create_financial_year(db: Session, fy_in: FinancialYearMasterCreate) -> FinancialYearMasterResponse:
        obj = fy_repo.create(db, fy_in.model_dump())
        db.commit()
        db.refresh(obj)
        return obj
