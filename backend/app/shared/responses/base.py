from typing import TypeVar, Generic, Optional, Any, List
from pydantic import BaseModel

T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    success: bool = True
    message: str = "Success"
    data: Optional[T] = None
    
class ErrorDetail(BaseModel):
    field: str
    msg: str

class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    errors: List[ErrorDetail] = []
