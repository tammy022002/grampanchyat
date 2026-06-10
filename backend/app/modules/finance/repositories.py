from app.shared.utils.repository import BaseRepository
from app.modules.finance.models import BudgetMaster, Cashbook, Ledger, Receipt

class BudgetRepository(BaseRepository[BudgetMaster]):
    def __init__(self):
        super().__init__(BudgetMaster)

class CashbookRepository(BaseRepository[Cashbook]):
    def __init__(self):
        super().__init__(Cashbook)

class ReceiptRepository(BaseRepository[Receipt]):
    def __init__(self):
        super().__init__(Receipt)

budget_repo = BudgetRepository()
cashbook_repo = CashbookRepository()
receipt_repo = ReceiptRepository()
