export interface MenuCategory {
  title: string;
  items: { label: string, path: string }[];
}

export const MENU_CONFIG: MenuCategory[] = [
  {
    title: 'Masters',
    items: [
      { label: 'Village Master', path: '/namuna/village_master' },
      { label: 'Employee Master', path: '/namuna/employee_master' },
      { label: 'Financial Year', path: '/namuna/financial_year_master' }
    ]
  },
  {
    title: 'Finance (Namuna 1-7)',
    items: [
      { label: 'Budget Master', path: '/finance/budgets' }, 
      { label: 'Cashbook', path: '/finance/cashbook' },     
      { label: 'Reappropriation', path: '/namuna/reappropriation' },
      { label: 'Income & Expense', path: '/namuna/income_expense' },
      { label: 'Assets & Liabilities', path: '/namuna/assets_liabilities' },
      { label: 'Daily Cashbook', path: '/namuna/daily_cashbook' },
      { label: 'Ledger', path: '/namuna/ledger' },
      { label: 'Receipt', path: '/namuna/receipt' }
    ]
  },
  {
    title: 'Taxation (Namuna 8-12)',
    items: [
      { label: 'Tax Assessment', path: '/namuna/tax_assessment' },
      { label: 'Tax Demand', path: '/namuna/tax_demand' },
      { label: 'Demand Notice', path: '/namuna/demand_notice' },
      { label: 'Tax Receipt', path: '/namuna/tax_receipt' },
      { label: 'Misc Demand', path: '/namuna/misc_demand' }
    ]
  },
  {
    title: 'Works & Infrastructure',
    items: [
      { label: 'Work Estimate', path: '/namuna/work_estimate' },
      { label: 'Measurement Book', path: '/namuna/measurement_book' },
      { label: 'Work Bill', path: '/namuna/work_bill' }
    ]
  },
  {
    title: 'Employees & Payroll',
    items: [
      { label: 'Attendance', path: '/namuna/attendance' },
      { label: 'Salary Payment', path: '/namuna/salary_payment' },
      { label: 'Travel Allowance', path: '/namuna/travel_allowance' },
      { label: 'Employee Register', path: '/namuna/employee_register' }
    ]
  },
  {
    title: 'Inventory & Assets',
    items: [
      { label: 'Stamp Register', path: '/namuna/stamp_register' },
      { label: 'Consumable Stock', path: '/namuna/consumable_stock' },
      { label: 'Movable Assets', path: '/namuna/movable_assets' },
      { label: 'Immovable Assets', path: '/namuna/immovable_assets' },
      { label: 'Land Register', path: '/namuna/land_register' },
      { label: 'Road Register', path: '/namuna/road_register' },
      { label: 'Tree Register', path: '/namuna/tree_register' },
      { label: 'Investment Register', path: '/namuna/investment_register' }
    ]
  },
  {
    title: 'Audit & Loans',
    items: [
      { label: 'Audit Objection', path: '/namuna/audit_objection' },
      { label: 'Audit Compliance', path: '/namuna/audit_compliance' },
      { label: 'Loan Register', path: '/namuna/loan_register' },
      { label: 'Advance Deposit', path: '/namuna/advance_deposit' },
      { label: 'Petty Cash', path: '/namuna/petty_cash' }
    ]
  },
  {
    title: 'Other Registers',
    items: [
      { label: 'Refund Order', path: '/namuna/refund_order' },
      { label: 'Contingency Expense', path: '/namuna/contingency_expense' },
      { label: 'Monthly Income/Expense', path: '/namuna/monthly_income_expense' },
      { label: 'Monthly Expenditure', path: '/namuna/monthly_expenditure' },
      { label: 'Reserved Fund Utilization', path: '/namuna/reserved_fund_utilization' }
    ]
  }
];
