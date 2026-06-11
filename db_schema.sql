CREATE TABLE Village_Master (
    village_id SERIAL PRIMARY KEY,
    village_name VARCHAR(255),
    gram_panchayat_name VARCHAR(255),
    taluka VARCHAR(255),
    district VARCHAR(255)
);

CREATE TABLE Employee_Master (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(255),
    designation VARCHAR(255),
    joining_date DATE,
    salary NUMERIC(15,2),
    status VARCHAR(50)
);

CREATE TABLE Financial_Year_Master (
    fy_id SERIAL PRIMARY KEY,
    fy_year VARCHAR(50),
    start_date DATE,
    end_date DATE
);

CREATE TABLE Budget_Master (
    budget_id SERIAL PRIMARY KEY,
    financial_year VARCHAR(50),
    department VARCHAR(255),
    account_head VARCHAR(255),
    estimated_receipts NUMERIC(15,2),
    estimated_expenditure NUMERIC(15,2),
    approved_by VARCHAR(255),
    approved_date DATE
);

CREATE TABLE Reappropriation (
    reallocation_id SERIAL PRIMARY KEY,
    financial_year VARCHAR(50),
    from_head VARCHAR(255),
    to_head VARCHAR(255),
    amount NUMERIC(15,2),
    resolution_no VARCHAR(100),
    resolution_date DATE,
    remarks TEXT
);

CREATE TABLE Income_Expense (
    transaction_id SERIAL PRIMARY KEY,
    transaction_date DATE,
    receipt_amount NUMERIC(15,2),
    expense_amount NUMERIC(15,2),
    account_head VARCHAR(255),
    narration TEXT
);

CREATE TABLE Assets_Liabilities (
    record_id SERIAL PRIMARY KEY,
    financial_year VARCHAR(50),
    asset_name VARCHAR(255),
    asset_value NUMERIC(15,2),
    liability_name VARCHAR(255),
    liability_value NUMERIC(15,2)
);

CREATE TABLE Cashbook (
    entry_id SERIAL PRIMARY KEY,
    transaction_date DATE,
    voucher_no VARCHAR(100),
    receipt_amount NUMERIC(15,2),
    payment_amount NUMERIC(15,2),
    balance NUMERIC(15,2),
    narration TEXT
);

CREATE TABLE Daily_Cashbook (
    daily_id SERIAL PRIMARY KEY,
    date DATE,
    opening_balance NUMERIC(15,2),
    receipts NUMERIC(15,2),
    payments NUMERIC(15,2),
    closing_balance NUMERIC(15,2)
);

CREATE TABLE Ledger (
    ledger_id SERIAL PRIMARY KEY,
    account_head VARCHAR(255),
    transaction_date DATE,
    debit NUMERIC(15,2),
    credit NUMERIC(15,2),
    balance NUMERIC(15,2)
);

CREATE TABLE Receipt (
    receipt_id SERIAL PRIMARY KEY,
    receipt_no VARCHAR(100),
    receipt_date DATE,
    payer_name VARCHAR(255),
    amount NUMERIC(15,2),
    purpose TEXT,
    payment_mode VARCHAR(50)
);

CREATE TABLE Tax_Assessment (
    assessment_id SERIAL PRIMARY KEY,
    property_no VARCHAR(100),
    owner_name VARCHAR(255),
    tax_type VARCHAR(100),
    annual_value NUMERIC(15,2),
    tax_amount NUMERIC(15,2)
);

CREATE TABLE Tax_Demand (
    demand_id SERIAL PRIMARY KEY,
    assessment_id INT REFERENCES Tax_Assessment(assessment_id) ON DELETE CASCADE,
    demand_year VARCHAR(50),
    amount_due NUMERIC(15,2),
    due_date DATE
);

CREATE TABLE Demand_Notice (
    notice_id SERIAL PRIMARY KEY,
    demand_id INT REFERENCES Tax_Demand(demand_id) ON DELETE CASCADE,
    issue_date DATE,
    taxpayer_name VARCHAR(255),
    amount NUMERIC(15,2)
);

CREATE TABLE Tax_Receipt (
    tax_receipt_id SERIAL PRIMARY KEY,
    receipt_no VARCHAR(100),
    taxpayer_id INT REFERENCES Tax_Assessment(assessment_id) ON DELETE CASCADE,
    tax_type VARCHAR(100),
    amount NUMERIC(15,2),
    receipt_date DATE
);

CREATE TABLE Misc_Demand (
    demand_id SERIAL PRIMARY KEY,
    demand_type VARCHAR(100),
    amount NUMERIC(15,2),
    person_name VARCHAR(255),
    due_date DATE
);

CREATE TABLE Contingency_Expense (
    expense_id SERIAL PRIMARY KEY,
    date DATE,
    purpose TEXT,
    amount NUMERIC(15,2),
    approved_by VARCHAR(255)
);

CREATE TABLE Employee_Register (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    designation VARCHAR(255),
    pay_scale VARCHAR(100),
    joining_date DATE,
    status VARCHAR(50)
);

CREATE TABLE Stamp_Register (
    stamp_id SERIAL PRIMARY KEY,
    stamp_type VARCHAR(100),
    quantity NUMERIC(10,2),
    issue_date DATE,
    balance NUMERIC(10,2)
);

CREATE TABLE Consumable_Stock (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(255),
    opening_stock NUMERIC(10,2),
    received_qty NUMERIC(10,2),
    issued_qty NUMERIC(10,2),
    balance_qty NUMERIC(10,2)
);

CREATE TABLE Movable_Assets (
    asset_id SERIAL PRIMARY KEY,
    asset_name VARCHAR(255),
    purchase_date DATE,
    value NUMERIC(15,2),
    location VARCHAR(255),
    condition VARCHAR(255)
);

CREATE TABLE Advance_Deposit (
    deposit_id SERIAL PRIMARY KEY,
    person_name VARCHAR(255),
    amount NUMERIC(15,2),
    deposit_date DATE,
    refund_date DATE
);

CREATE TABLE Petty_Cash (
    petty_cash_id SERIAL PRIMARY KEY,
    date DATE,
    purpose TEXT,
    amount NUMERIC(15,2),
    balance NUMERIC(15,2)
);

CREATE TABLE Attendance (
    attendance_id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES Employee_Master(employee_id) ON DELETE CASCADE,
    work_id INT REFERENCES Work_Estimate(estimate_id) ON DELETE CASCADE,
    date DATE,
    status VARCHAR(50)
);

CREATE TABLE Work_Estimate (
    estimate_id SERIAL PRIMARY KEY,
    work_name VARCHAR(255),
    estimated_cost NUMERIC(15,2),
    estimate_date DATE,
    engineer_name VARCHAR(255)
);

CREATE TABLE Measurement_Book (
    measurement_id SERIAL PRIMARY KEY,
    work_id INT REFERENCES Work_Estimate(estimate_id) ON DELETE CASCADE,
    measurement_date DATE,
    quantity NUMERIC(10,2),
    remarks TEXT
);

CREATE TABLE Work_Bill (
    bill_id SERIAL PRIMARY KEY,
    work_id INT REFERENCES Work_Estimate(estimate_id) ON DELETE CASCADE,
    contractor_name VARCHAR(255),
    amount NUMERIC(15,2),
    bill_date DATE
);

CREATE TABLE Salary_Payment (
    payment_id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES Employee_Master(employee_id) ON DELETE CASCADE,
    work_id INT REFERENCES Work_Estimate(estimate_id) ON DELETE SET NULL,
    salary_month VARCHAR(50),
    gross_salary NUMERIC(15,2),
    deductions NUMERIC(15,2),
    net_salary NUMERIC(15,2)
);

CREATE TABLE Immovable_Assets (
    asset_id SERIAL PRIMARY KEY,
    asset_name VARCHAR(255),
    survey_no VARCHAR(100),
    location VARCHAR(255),
    value NUMERIC(15,2)
);

CREATE TABLE Road_Register (
    road_id SERIAL PRIMARY KEY,
    road_name VARCHAR(255),
    length NUMERIC(10,2),
    width NUMERIC(10,2),
    location VARCHAR(255)
);

CREATE TABLE Land_Register (
    land_id SERIAL PRIMARY KEY,
    survey_no VARCHAR(100),
    area NUMERIC(10,2),
    location VARCHAR(255),
    ownership_status VARCHAR(100)
);

CREATE TABLE Investment_Register (
    investment_id SERIAL PRIMARY KEY,
    institution VARCHAR(255),
    amount NUMERIC(15,2),
    interest_rate NUMERIC(5,2),
    maturity_date DATE
);

CREATE TABLE Monthly_Income_Expense (
    report_id SERIAL PRIMARY KEY,
    month VARCHAR(50),
    total_receipts NUMERIC(15,2),
    total_expenses NUMERIC(15,2),
    closing_balance NUMERIC(15,2)
);

CREATE TABLE Monthly_Expenditure (
    report_id SERIAL PRIMARY KEY,
    month VARCHAR(50),
    account_head VARCHAR(255),
    amount NUMERIC(15,2)
);

CREATE TABLE Audit_Objection (
    objection_id SERIAL PRIMARY KEY,
    audit_year VARCHAR(50),
    objection_no VARCHAR(100),
    description TEXT,
    status VARCHAR(100)
);

CREATE TABLE Reserved_Fund_Utilization (
    utilization_id SERIAL PRIMARY KEY,
    scheme_type VARCHAR(100),
    budget_allocated NUMERIC(15,2),
    expenditure NUMERIC(15,2),
    balance NUMERIC(15,2)
);

CREATE TABLE Loan_Register (
    loan_id SERIAL PRIMARY KEY,
    lender VARCHAR(255),
    amount NUMERIC(15,2),
    interest_rate NUMERIC(5,2),
    start_date DATE,
    outstanding_balance NUMERIC(15,2)
);

CREATE TABLE Audit_Compliance (
    compliance_id SERIAL PRIMARY KEY,
    objection_id INT REFERENCES Audit_Objection(objection_id) ON DELETE CASCADE,
    action_taken TEXT,
    compliance_date DATE,
    status VARCHAR(100)
);

CREATE TABLE Travel_Allowance (
    ta_id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES Employee_Master(employee_id) ON DELETE CASCADE,
    travel_date DATE,
    source VARCHAR(255),
    destination VARCHAR(255),
    amount NUMERIC(15,2)
);

CREATE TABLE Refund_Order (
    refund_id SERIAL PRIMARY KEY,
    person_name VARCHAR(255),
    reason TEXT,
    amount NUMERIC(15,2),
    refund_date DATE
);

CREATE TABLE Tree_Register (
    tree_id SERIAL PRIMARY KEY,
    tree_type VARCHAR(255),
    location VARCHAR(255),
    plantation_date DATE,
    status VARCHAR(100)
);
