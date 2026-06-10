from app.shared.utils.repository import BaseRepository
from app.modules.tax.models import TaxAssessment, TaxDemand, TaxReceipt

class TaxAssessmentRepository(BaseRepository[TaxAssessment]):
    def __init__(self):
        super().__init__(TaxAssessment)

class TaxDemandRepository(BaseRepository[TaxDemand]):
    def __init__(self):
        super().__init__(TaxDemand)

class TaxReceiptRepository(BaseRepository[TaxReceipt]):
    def __init__(self):
        super().__init__(TaxReceipt)

tax_assessment_repo = TaxAssessmentRepository()
tax_demand_repo = TaxDemandRepository()
tax_receipt_repo = TaxReceiptRepository()
