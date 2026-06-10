from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import Optional

# Village Master
class VillageMasterBase(BaseModel):
    village_name: str
    gram_panchayat_name: str
    taluka: str
    district: str

class VillageMasterCreate(VillageMasterBase):
    pass

class VillageMasterUpdate(BaseModel):
    village_name: Optional[str] = None
    gram_panchayat_name: Optional[str] = None
    taluka: Optional[str] = None
    district: Optional[str] = None

class VillageMasterResponse(VillageMasterBase):
    village_id: int
    model_config = ConfigDict(from_attributes=True)

# Employee Master
class EmployeeMasterBase(BaseModel):
    employee_name: str
    designation: str
    joining_date: date
    salary: float
    status: str

class EmployeeMasterCreate(EmployeeMasterBase):
    pass

class EmployeeMasterUpdate(BaseModel):
    employee_name: Optional[str] = None
    designation: Optional[str] = None
    joining_date: Optional[date] = None
    salary: Optional[float] = None
    status: Optional[str] = None

class EmployeeMasterResponse(EmployeeMasterBase):
    employee_id: int
    model_config = ConfigDict(from_attributes=True)

# Financial Year Master
class FinancialYearMasterBase(BaseModel):
    fy_year: str
    start_date: date
    end_date: date

class FinancialYearMasterCreate(FinancialYearMasterBase):
    pass

class FinancialYearMasterUpdate(BaseModel):
    fy_year: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class FinancialYearMasterResponse(FinancialYearMasterBase):
    fy_id: int
    model_config = ConfigDict(from_attributes=True)
