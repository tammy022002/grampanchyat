from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Type, TypeVar, Optional, Generic, Any
from app.core.database import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_by_id(self, db: Session, id: Any) -> Optional[ModelType]:
        # Using the primary key generically requires getting the PK column name.
        # Alternatively, assume we pass the column.
        return db.get(self.model, id)

    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[ModelType]:
        stmt = select(self.model).offset(skip).limit(limit)
        return db.execute(stmt).scalars().all()

    def create(self, db: Session, obj_in: dict) -> ModelType:
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        db.flush() # Flush to get IDs, commit will be handled by UoW / Service layer
        return db_obj

    def update(self, db: Session, db_obj: ModelType, obj_in: dict) -> ModelType:
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.add(db_obj)
        db.flush()
        return db_obj

    def delete(self, db: Session, id: Any) -> bool:
        obj = self.get_by_id(db, id)
        if obj:
            db.delete(obj)
            db.flush()
            return True
        return False
