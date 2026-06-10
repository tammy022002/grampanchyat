from app.shared.utils.repository import BaseRepository
from app.modules.employees.models import Attendance, SalaryPayment, TravelAllowance

class AttendanceRepository(BaseRepository[Attendance]):
    def __init__(self):
        super().__init__(Attendance)

class SalaryPaymentRepository(BaseRepository[SalaryPayment]):
    def __init__(self):
        super().__init__(SalaryPayment)

class TravelAllowanceRepository(BaseRepository[TravelAllowance]):
    def __init__(self):
        super().__init__(TravelAllowance)

attendance_repo = AttendanceRepository()
salary_payment_repo = SalaryPaymentRepository()
travel_allowance_repo = TravelAllowanceRepository()
