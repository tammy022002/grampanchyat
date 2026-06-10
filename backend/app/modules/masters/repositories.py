from app.shared.utils.repository import BaseRepository
from app.modules.masters.models import VillageMaster, EmployeeMaster, FinancialYearMaster

class VillageMasterRepository(BaseRepository[VillageMaster]):
    def __init__(self):
        super().__init__(VillageMaster)

class EmployeeMasterRepository(BaseRepository[EmployeeMaster]):
    def __init__(self):
        super().__init__(EmployeeMaster)

class FinancialYearMasterRepository(BaseRepository[FinancialYearMaster]):
    def __init__(self):
        super().__init__(FinancialYearMaster)

village_repo = VillageMasterRepository()
employee_repo = EmployeeMasterRepository()
fy_repo = FinancialYearMasterRepository()
