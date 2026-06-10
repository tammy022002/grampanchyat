import { GridColumn } from '../data-grid/data-grid.component';

export const NamunaSchemaRegistry: { [key: string]: GridColumn[] } = {
  'reappropriation': [
    { field: 'id', header: 'ID' },
    { field: 'financial_year', header: 'Financial Year' },
    { field: 'from_head', header: 'From Account Head' },
    { field: 'to_head', header: 'To Account Head' },
    { field: 'amount', header: 'Amount', type: 'currency' },
    { field: 'resolution_no', header: 'Resolution No' },
    { field: 'resolution_date', header: 'Resolution Date', type: 'date' },
    { field: 'remarks', header: 'Remarks' }
  ],
  'income_expense': [
    { field: 'id', header: 'ID' },
    { field: 'transaction_date', header: 'Date', type: 'date' },
    { field: 'receipt_amount', header: 'Receipt Amount', type: 'currency' },
    { field: 'expense_amount', header: 'Expense Amount', type: 'currency' },
    { field: 'account_head', header: 'Account Head' },
    { field: 'narration', header: 'Narration' }
  ],
  'assets_liabilities': [
    { field: 'id', header: 'ID' },
    { field: 'financial_year', header: 'Financial Year' },
    { field: 'asset_name', header: 'Asset Name' },
    { field: 'asset_value', header: 'Asset Value', type: 'currency' },
    { field: 'liability_name', header: 'Liability Name' },
    { field: 'liability_value', header: 'Liability Value', type: 'currency' }
  ],
  'daily_cashbook': [
    { field: 'id', header: 'ID' },
    { field: 'date', header: 'Date', type: 'date' },
    { field: 'opening_balance', header: 'Opening Balance', type: 'currency' },
    { field: 'receipts', header: 'Receipts', type: 'currency' },
    { field: 'payments', header: 'Payments', type: 'currency' },
    { field: 'closing_balance', header: 'Closing Balance', type: 'currency' }
  ],
  'ledger': [
    { field: 'id', header: 'ID' },
    { field: 'account_head', header: 'Account Head' },
    { field: 'transaction_date', header: 'Transaction Date', type: 'date' },
    { field: 'debit', header: 'Debit', type: 'currency' },
    { field: 'credit', header: 'Credit', type: 'currency' },
    { field: 'balance', header: 'Balance', type: 'currency' }
  ],
  'receipt': [
    { field: 'id', header: 'ID' },
    { field: 'receipt_no', header: 'Receipt No' },
    { field: 'receipt_date', header: 'Date', type: 'date' },
    { field: 'payer_name', header: 'Payer Name' },
    { field: 'amount', header: 'Amount', type: 'currency' },
    { field: 'purpose', header: 'Purpose' },
    { field: 'payment_mode', header: 'Payment Mode' }
  ],
  'tax_assessment': [
    { field: 'id', header: 'ID' },
    { field: 'property_no', header: 'Property No' },
    { field: 'owner_name', header: 'Owner Name' },
    { field: 'tax_type', header: 'Tax Type' },
    { field: 'annual_value', header: 'Annual Value', type: 'currency' },
    { field: 'tax_amount', header: 'Tax Amount', type: 'currency' }
  ],
  'tax_demand': [
    { field: 'id', header: 'ID' },
    { field: 'assessment_id', header: 'Assessment ID', type: 'number' },
    { field: 'demand_year', header: 'Demand Year' },
    { field: 'amount_due', header: 'Amount Due', type: 'currency' },
    { field: 'due_date', header: 'Due Date', type: 'date' }
  ],
  'demand_notice': [
    { field: 'id', header: 'ID' },
    { field: 'demand_id', header: 'Demand ID', type: 'number' },
    { field: 'issue_date', header: 'Issue Date', type: 'date' },
    { field: 'taxpayer_name', header: 'Taxpayer Name' },
    { field: 'amount', header: 'Amount', type: 'currency' }
  ],
  'tax_receipt': [
    { field: 'id', header: 'ID' },
    { field: 'receipt_no', header: 'Receipt No' },
    { field: 'taxpayer_id', header: 'Taxpayer ID', type: 'number' },
    { field: 'tax_type', header: 'Tax Type' },
    { field: 'amount', header: 'Amount', type: 'currency' },
    { field: 'receipt_date', header: 'Receipt Date', type: 'date' }
  ],
  'misc_demand': [
    { field: 'id', header: 'ID' },
    { field: 'demand_type', header: 'Demand Type' },
    { field: 'person_name', header: 'Person Name' },
    { field: 'amount', header: 'Amount', type: 'currency' },
    { field: 'due_date', header: 'Due Date', type: 'date' }
  ],
  'work_estimate': [
    { field: 'id', header: 'ID' },
    { field: 'work_name', header: 'Work Name' },
    { field: 'estimated_cost', header: 'Estimated Cost', type: 'currency' },
    { field: 'estimate_date', header: 'Estimate Date', type: 'date' },
    { field: 'engineer_name', header: 'Engineer Name' }
  ],
  'measurement_book': [
    { field: 'id', header: 'ID' },
    { field: 'work_id', header: 'Work ID', type: 'number' },
    { field: 'measurement_date', header: 'Measurement Date', type: 'date' },
    { field: 'quantity', header: 'Quantity' },
    { field: 'remarks', header: 'Remarks' }
  ],
  'work_bill': [
    { field: 'id', header: 'ID' },
    { field: 'work_id', header: 'Work ID', type: 'number' },
    { field: 'contractor_name', header: 'Contractor Name' },
    { field: 'amount', header: 'Amount', type: 'currency' },
    { field: 'bill_date', header: 'Bill Date', type: 'date' }
  ],
  'road_register': [
    { field: 'id', header: 'ID' },
    { field: 'road_name', header: 'Road Name' },
    { field: 'length', header: 'Length' },
    { field: 'width', header: 'Width' },
    { field: 'location', header: 'Location' }
  ],
  'land_register': [
    { field: 'id', header: 'ID' },
    { field: 'survey_no', header: 'Survey No' },
    { field: 'area', header: 'Area' },
    { field: 'location', header: 'Location' },
    { field: 'ownership_status', header: 'Ownership' }
  ],
  'employee_register': [
    { field: 'id', header: 'ID' },
    { field: 'name', header: 'Name' },
    { field: 'designation', header: 'Designation' },
    { field: 'pay_scale', header: 'Pay Scale' },
    { field: 'joining_date', header: 'Joining Date', type: 'date' },
    { field: 'status', header: 'Status' }
  ],
  'attendance': [
    { field: 'id', header: 'ID' },
    { field: 'employee_id', header: 'Employee ID', type: 'number' },
    { field: 'work_id', header: 'Work ID', type: 'number' },
    { field: 'date', header: 'Date', type: 'date' },
    { field: 'status', header: 'Status' }
  ],
  'salary_payment': [
    { field: 'id', header: 'ID' },
    { field: 'employee_id', header: 'Employee ID', type: 'number' },
    { field: 'work_id', header: 'Work ID', type: 'number' },
    { field: 'salary_month', header: 'Month' },
    { field: 'gross_salary', header: 'Gross Salary', type: 'currency' },
    { field: 'deductions', header: 'Deductions', type: 'currency' },
    { field: 'net_salary', header: 'Net Salary', type: 'currency' }
  ],
  'travel_allowance': [
    { field: 'id', header: 'ID' },
    { field: 'employee_id', header: 'Employee ID', type: 'number' },
    { field: 'travel_date', header: 'Travel Date', type: 'date' },
    { field: 'source', header: 'Source' },
    { field: 'destination', header: 'Destination' },
    { field: 'amount', header: 'Amount', type: 'currency' }
  ],
  'stamp_register': [
    { field: 'id', header: 'ID' },
    { field: 'stamp_type', header: 'Stamp Type' },
    { field: 'quantity', header: 'Quantity' },
    { field: 'issue_date', header: 'Issue Date', type: 'date' },
    { field: 'balance', header: 'Balance' }
  ],
  'consumable_stock': [
    { field: 'id', header: 'ID' },
    { field: 'item_name', header: 'Item Name' },
    { field: 'opening_stock', header: 'Opening Stock' },
    { field: 'received_qty', header: 'Received Qty' },
    { field: 'issued_qty', header: 'Issued Qty' },
    { field: 'balance_qty', header: 'Balance Qty' }
  ],
  'movable_assets': [
    { field: 'id', header: 'ID' },
    { field: 'asset_name', header: 'Asset Name' },
    { field: 'purchase_date', header: 'Purchase Date', type: 'date' },
    { field: 'value', header: 'Value', type: 'currency' },
    { field: 'location', header: 'Location' },
    { field: 'condition', header: 'Condition' }
  ],
  'immovable_assets': [
    { field: 'id', header: 'ID' },
    { field: 'asset_name', header: 'Asset Name' },
    { field: 'survey_no', header: 'Survey No' },
    { field: 'location', header: 'Location' },
    { field: 'value', header: 'Value', type: 'currency' }
  ],
  'tree_register': [
    { field: 'id', header: 'ID' },
    { field: 'tree_type', header: 'Tree Type' },
    { field: 'location', header: 'Location' },
    { field: 'plantation_date', header: 'Plantation Date', type: 'date' },
    { field: 'status', header: 'Status' }
  ],
  'advance_deposit': [
    { field: 'id', header: 'ID' },
    { field: 'person_name', header: 'Person Name' },
    { field: 'amount', header: 'Amount', type: 'currency' },
    { field: 'deposit_date', header: 'Deposit Date', type: 'date' },
    { field: 'refund_date', header: 'Refund Date', type: 'date' }
  ],
  'petty_cash': [
    { field: 'id', header: 'ID' },
    { field: 'date', header: 'Date', type: 'date' },
    { field: 'purpose', header: 'Purpose' },
    { field: 'amount', header: 'Amount', type: 'currency' },
    { field: 'balance', header: 'Balance', type: 'currency' }
  ],
  'audit_objection': [
    { field: 'id', header: 'ID' },
    { field: 'audit_year', header: 'Audit Year' },
    { field: 'objection_no', header: 'Objection No' },
    { field: 'description', header: 'Description' },
    { field: 'status', header: 'Status' }
  ],
  'audit_compliance': [
    { field: 'id', header: 'ID' },
    { field: 'objection_id', header: 'Objection ID', type: 'number' },
    { field: 'action_taken', header: 'Action Taken' },
    { field: 'compliance_date', header: 'Compliance Date', type: 'date' },
    { field: 'status', header: 'Status' }
  ],
  'reserved_fund': [
    { field: 'id', header: 'ID' },
    { field: 'scheme_type', header: 'Scheme Type' },
    { field: 'budget_allocated', header: 'Budget Allocated', type: 'currency' },
    { field: 'expenditure', header: 'Expenditure', type: 'currency' },
    { field: 'balance', header: 'Balance', type: 'currency' }
  ],
  'refund_order': [
    { field: 'id', header: 'ID' },
    { field: 'person_name', header: 'Person Name' },
    { field: 'reason', header: 'Reason' },
    { field: 'amount', header: 'Amount', type: 'currency' },
    { field: 'refund_date', header: 'Refund Date', type: 'date' }
  ]
};
