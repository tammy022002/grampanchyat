from app.shared.utils.repository import BaseRepository
from app.modules.works.models import WorkEstimate, MeasurementBook, WorkBill

class WorkEstimateRepository(BaseRepository[WorkEstimate]):
    def __init__(self):
        super().__init__(WorkEstimate)

class MeasurementBookRepository(BaseRepository[MeasurementBook]):
    def __init__(self):
        super().__init__(MeasurementBook)

class WorkBillRepository(BaseRepository[WorkBill]):
    def __init__(self):
        super().__init__(WorkBill)

work_estimate_repo = WorkEstimateRepository()
measurement_book_repo = MeasurementBookRepository()
work_bill_repo = WorkBillRepository()
