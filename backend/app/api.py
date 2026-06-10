from fastapi import APIRouter
from app.modules.masters.controllers import router as masters_router
from app.modules.finance.controllers import router as finance_router
from app.modules.tax.controllers import router as tax_router
from app.modules.works.controllers import router as works_router
from app.modules.employees.controllers import router as employees_router
from app.modules.reports.controllers import router as reports_router
from app.modules.users.controllers import router as users_router
from app.modules.namuna.controllers import router as namuna_router

api_router = APIRouter()

api_router.include_router(users_router, prefix="/auth", tags=["Authentication"])
api_router.include_router(masters_router, prefix="/masters", tags=["Masters"])
api_router.include_router(finance_router, prefix="/finance", tags=["Finance"])
api_router.include_router(tax_router, prefix="/tax", tags=["Tax"])
api_router.include_router(works_router, prefix="/works", tags=["Works"])
api_router.include_router(employees_router, prefix="/employees", tags=["Employees"])
api_router.include_router(reports_router, prefix="/reports", tags=["Reports"])
api_router.include_router(namuna_router, prefix="/namuna", tags=["Dynamic Namune"])
