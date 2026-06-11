-- Clear existing data if necessary (optional, but good for idempotency)
TRUNCATE TABLE Village_Master, Employee_Master, Financial_Year_Master, Budget_Master, Tax_Assessment, Tax_Demand, Tax_Receipt, Cashbook, Work_Estimate, Measurement_Book, Work_Bill, Attendance, Salary_Payment, Assets_Liabilities RESTART IDENTITY CASCADE;

-- 1. Village Master
INSERT INTO Village_Master (village_name, gram_panchayat_name, taluka, district) VALUES
('Shrigonda', 'Shrigonda Gram Panchayat', 'Shrigonda', 'Ahmednagar');

-- 2. Financial Year
INSERT INTO Financial_Year_Master (fy_year, start_date, end_date) VALUES
('2026-2027', '2026-04-01', '2027-03-31');

-- 3. Budget Master
INSERT INTO Budget_Master (financial_year, department, account_head, estimated_receipts, estimated_expenditure, approved_by, approved_date) VALUES
('2026-2027', 'Public Works', 'Road Construction', 0.00, 500000.00, 'Sarpanch', '2026-04-10'),
('2026-2027', 'Taxation', 'Property Tax', 1500000.00, 0.00, 'Sarpanch', '2026-04-10');

-- 4. Employee Master
INSERT INTO Employee_Master (employee_name, designation, joining_date, salary, status) VALUES
('Suresh Kumar', 'Gram Sevak', '2020-05-10', 35000.00, 'Active'),
('Ramesh Patil', 'Peon', '2022-08-15', 18000.00, 'Active');

-- 5. Tax Assessment (Ram Patil)
INSERT INTO Tax_Assessment (property_no, owner_name, tax_type, annual_value, tax_amount) VALUES
('House 42', 'Ram Patil', 'Property Tax', 12000.00, 1200.00),
('House 88', 'Sunil Verma', 'Water Tax', 4500.00, 450.00);

-- 6. Tax Demand
INSERT INTO Tax_Demand (assessment_id, demand_year, amount_due, due_date) VALUES
(1, '2026-2027', 1200.00, '2026-12-31');

-- 7. Tax Receipt
INSERT INTO Tax_Receipt (receipt_no, taxpayer_id, tax_type, amount, receipt_date) VALUES
('RCPT-991', 1, 'Property Tax', 1200.00, '2026-10-15');

-- 8. Cashbook
INSERT INTO Cashbook (transaction_date, voucher_no, receipt_amount, payment_amount, balance, narration) VALUES
('2026-10-15', 'V-101', 1200.00, 0.00, 1200.00, 'Income: Tax Collection - Ram Patil'),
('2026-10-20', 'V-102', 0.00, 200000.00, -198800.00, 'Expense: Road Construction Bill #1'),
('2026-10-31', 'V-103', 0.00, 35000.00, -233800.00, 'Expense: Oct Salary - Suresh Kumar');

-- 9. Work Estimate
INSERT INTO Work_Estimate (work_name, estimated_cost, estimate_date, engineer_name) VALUES
('Zilla Parishad Road Construction', 500000.00, '2026-05-01', 'Er. Deshmukh');

-- 10. Measurement Book
INSERT INTO Measurement_Book (work_id, measurement_date, quantity, remarks) VALUES
(1, '2026-10-10', 1.00, 'MB for Road Construction (Phase 1)');

-- 11. Work Bill
INSERT INTO Work_Bill (work_id, contractor_name, amount, bill_date) VALUES
(1, 'Patil Constructions', 200000.00, '2026-10-15');

-- 12. Attendance
INSERT INTO Attendance (employee_id, work_id, date, status) VALUES
(1, 1, '2026-10-01', 'Present');

-- 13. Salary Payment
INSERT INTO Salary_Payment (employee_id, work_id, salary_month, gross_salary, deductions, net_salary) VALUES
(1, 1, 'October 2026', 35000.00, 2000.00, 33000.00);

-- 14. Assets & Liabilities
INSERT INTO Assets_Liabilities (financial_year, asset_name, asset_value, liability_name, liability_value) VALUES
('2026-2027', 'Gram Panchayat Main Building', 2500000.00, 'Bank Loan', 500000.00);
