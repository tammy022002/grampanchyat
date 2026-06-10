from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
import io
import openpyxl
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class ReportService:
    @staticmethod
    def generate_excel_report(db: Session, report_type: str) -> StreamingResponse:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Report"
        
        # Mock data headers
        ws.append(["ID", "Date", "Description", "Amount"])
        ws.append([1, "2024-01-01", f"Sample {report_type} Entry", 1000.0])
        
        stream = io.BytesIO()
        wb.save(stream)
        stream.seek(0)
        
        return StreamingResponse(
            stream,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={report_type}_report.xlsx"}
        )

    @staticmethod
    def generate_pdf_report(db: Session, report_type: str) -> StreamingResponse:
        stream = io.BytesIO()
        c = canvas.Canvas(stream, pagesize=letter)
        c.drawString(100, 750, f"Gram Panchayat ERP - {report_type} Report")
        c.drawString(100, 730, "Generated automatically by system")
        c.save()
        
        stream.seek(0)
        return StreamingResponse(
            stream,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={report_type}_report.pdf"}
        )
