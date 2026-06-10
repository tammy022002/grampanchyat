from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.reports.services import ReportService

router = APIRouter()

@router.get("/generate/{report_type}")
def generate_report(
    report_type: str,
    format: str = Query("pdf", description="Format: pdf or excel"),
    db: Session = Depends(get_db)
):
    if format.lower() == "excel":
        return ReportService.generate_excel_report(db, report_type)
    else:
        return ReportService.generate_pdf_report(db, report_type)
