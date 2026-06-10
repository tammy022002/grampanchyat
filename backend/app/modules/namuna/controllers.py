from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.database import get_db

router = APIRouter()

# Map frontend namune URLs to exact DB table names if they differ slightly
TABLE_MAP = {
    "reserved_fund": "reserved_fund_utilization"
}

def get_db_table_name(frontend_table: str) -> str:
    return TABLE_MAP.get(frontend_table, frontend_table)

@router.get("/{table_name}")
def get_dynamic(table_name: str, db: Session = Depends(get_db)):
    db_table = get_db_table_name(table_name)
    try:
        # Prevent SQL injection by strictly ensuring alphanumeric table names
        if not db_table.replace("_", "").isalnum():
            raise HTTPException(status_code=400, detail="Invalid table name")

        # Fetch records
        result = db.execute(text(f"SELECT * FROM {db_table}")).mappings().all()
        
        # We must alias the Primary Key column (which ends in _id) to just "id" so the frontend Grid can read it
        items = []
        for row in result:
            row_dict = dict(row)
            # Find the primary key column to map to 'id'
            for key in row_dict.keys():
                if key.endswith('_id') or key == 'id':
                    row_dict['id'] = row_dict[key]
                    break
            items.append(row_dict)

        return {"success": True, "data": {"items": items, "total": len(items), "page": 1, "size": 100, "pages": 1}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{table_name}")
async def post_dynamic(table_name: str, request: Request, db: Session = Depends(get_db)):
    db_table = get_db_table_name(table_name)
    try:
        if not db_table.replace("_", "").isalnum():
            raise HTTPException(status_code=400, detail="Invalid table name")

        body = await request.json()
        if not body:
            raise HTTPException(status_code=400, detail="Empty payload")

        # Strip out any 'id' passed from frontend, let postgres auto-increment serial handle it
        if 'id' in body:
            del body['id']

        columns = list(body.keys())
        keys = ", ".join(columns)
        values = ", ".join([f":{k}" for k in columns])

        stmt = text(f"INSERT INTO {db_table} ({keys}) VALUES ({values}) RETURNING *")
        result = db.execute(stmt, body).mappings().first()
        
        # --- BUSINESS LOGIC CASCADES ---
        from datetime import date
        today_str = date.today().isoformat()

        if db_table == "tax_assessment":
            assessment_id = result["assessment_id"]
            tax_amount = result["tax_amount"]
            owner_name = result["owner_name"]
            tax_type = result["tax_type"]
            
            # 1. Automatically generate Tax Demand
            demand_stmt = text(f"INSERT INTO tax_demand (assessment_id, demand_year, amount_due, due_date) VALUES (:aid, '2026-2027', :amt, '2026-12-31') RETURNING demand_id")
            demand_result = db.execute(demand_stmt, {"aid": assessment_id, "amt": tax_amount}).mappings().first()
            demand_id = demand_result["demand_id"]
            
            # 2. Automatically generate Demand Notice
            notice_stmt = text(f"INSERT INTO demand_notice (demand_id, issue_date, taxpayer_name, amount) VALUES (:did, :today, :name, :amt)")
            db.execute(notice_stmt, {"did": demand_id, "today": today_str, "name": owner_name, "amt": tax_amount})
            
            # 3. Automatically generate Tax Receipt (Marking it as fully paid with an Auto-Receipt)
            receipt_no = f"RCPT-AUTO-{assessment_id}"
            receipt_stmt = text(f"INSERT INTO tax_receipt (receipt_no, taxpayer_id, tax_type, amount, receipt_date) VALUES (:rno, :aid, :ttype, :amt, :today)")
            db.execute(receipt_stmt, {"rno": receipt_no, "aid": assessment_id, "ttype": tax_type, "amt": tax_amount, "today": today_str})

            # 4. Automatically push to Cashbook & Ledger
            cashbook_stmt = text(f"INSERT INTO cashbook (transaction_date, voucher_no, receipt_amount, payment_amount, balance, narration) VALUES (:today, :rno, :amt, 0, :amt, 'Auto-generated from Tax Assessment')")
            db.execute(cashbook_stmt, {"today": today_str, "rno": receipt_no, "amt": tax_amount})
            
            ledger_stmt = text(f"INSERT INTO ledger (account_head, transaction_date, debit, credit, balance) VALUES (:ttype, :today, 0, :amt, :amt)")
            db.execute(ledger_stmt, {"ttype": f"Tax: {tax_type}", "today": today_str, "amt": tax_amount})

        elif db_table == "work_estimate":
            estimate_id = result["estimate_id"]
            amount = result["estimated_cost"]
            engineer = result["engineer_name"]
            
            # 1. Measurement Book
            mb_stmt = text(f"INSERT INTO measurement_book (work_id, measurement_date, quantity, remarks) VALUES (:wid, :today, 0, 'Auto-generated for estimate')")
            db.execute(mb_stmt, {"wid": estimate_id, "today": today_str})
            
            # 2. Attendance
            att_stmt = text(f"INSERT INTO attendance (employee_id, work_id, date, status) VALUES (1, :wid, :today, 'Pending Start')")
            db.execute(att_stmt, {"wid": estimate_id, "today": today_str})
            
            # 3. Work Bill
            bill_stmt = text(f"INSERT INTO work_bill (work_id, contractor_name, amount, bill_date) VALUES (:wid, 'Pending Contractor', :amt, :today)")
            db.execute(bill_stmt, {"wid": estimate_id, "amt": amount, "today": today_str})

        elif db_table in ["receipt", "tax_receipt"]:
            receipt_no = result["receipt_no"]
            amount = result["amount"]
            receipt_date = result.get("receipt_date", today_str)
            purpose = result.get("purpose", result.get("tax_type", "General Receipt"))
            
            # Automatically push to Cashbook & Ledger
            cashbook_stmt = text(f"INSERT INTO cashbook (transaction_date, voucher_no, receipt_amount, payment_amount, balance, narration) VALUES (:rdate, :rno, :amt, 0, :amt, :narration)")
            db.execute(cashbook_stmt, {"rdate": receipt_date, "rno": receipt_no, "amt": amount, "narration": f"Auto-generated from {purpose}"})
            
            ledger_stmt = text(f"INSERT INTO ledger (account_head, transaction_date, debit, credit, balance) VALUES (:purpose, :rdate, 0, :amt, :amt)")
            db.execute(ledger_stmt, {"purpose": purpose, "rdate": receipt_date, "amt": amount})

        db.commit()

        return {"success": True, "message": "Entry saved permanently to PostgreSQL."}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
