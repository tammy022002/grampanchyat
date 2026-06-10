import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="dashboard-header">
      <h2>Gram Panchayat Dashboard</h2>
      <p>Welcome to the central ERP command center. Select an action below to get started.</p>
    </div>

    <div class="summary-cards">
      <div class="card revenue">
        <h3>Total Revenue</h3>
        <div class="value">₹ 24,50,000</div>
        <div class="trend positive">↑ 12% vs last month</div>
      </div>
      <div class="card tax">
        <h3>Pending Tax Demand</h3>
        <div class="value">₹ 3,25,000</div>
        <div class="trend negative">↓ 5% recovery</div>
      </div>
      <div class="card works">
        <h3>Active Works</h3>
        <div class="value">14 Projects</div>
        <div class="trend neutral">On schedule</div>
      </div>
      <div class="card staff">
        <h3>Total Staff</h3>
        <div class="value">45</div>
        <div class="trend positive">Fully staffed</div>
      </div>
    </div>

    <div class="quick-actions-section">
      <h3>All 33 Namune (Quick Actions)</h3>
      <div class="action-grid">
        <a *ngFor="let item of allActions" [routerLink]="item.path" class="action-btn">
          <span class="icon">{{ item.icon }}</span>
          <span class="label">{{ item.label }}</span>
        </a>
      </div>
    </div>
  `,
  styles: [`
    .dashboard-header { margin-bottom: 30px; }
    .dashboard-header h2 { margin: 0 0 10px 0; color: #2c3e50; font-size: 28px; }
    .dashboard-header p { margin: 0; color: #7f8c8d; font-size: 16px; }

    .summary-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-bottom: 40px; }
    .card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-top: 4px solid #3498db; }
    .card.revenue { border-color: #2ecc71; }
    .card.tax { border-color: #e74c3c; }
    .card.works { border-color: #f39c12; }
    .card.staff { border-color: #9b59b6; }
    .card h3 { margin: 0 0 15px 0; color: #7f8c8d; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
    .card .value { font-size: 32px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; }
    .card .trend { font-size: 14px; font-weight: 500; }
    .trend.positive { color: #27ae60; }
    .trend.negative { color: #c0392b; }
    .trend.neutral { color: #f39c12; }

    .quick-actions-section h3 { margin-bottom: 20px; color: #2c3e50; border-bottom: 2px solid #ecf0f1; padding-bottom: 10px; }
    .action-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 15px; }
    .action-btn { background: white; border: 1px solid #dfe6e9; border-radius: 8px; padding: 15px 20px; display: flex; align-items: center; text-decoration: none; color: #2c3e50; transition: all 0.2s ease; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
    .action-btn:hover { transform: translateY(-3px); box-shadow: 0 6px 12px rgba(0,0,0,0.08); border-color: #3498db; }
    .action-btn .icon { font-size: 24px; margin-right: 15px; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; background: #ebf5fb; color: #3498db; border-radius: 50%; }
    .action-btn .label { font-weight: 600; font-size: 15px; }
  `]
})
export class DashboardComponent {
  allActions = [
    // Finance
    { label: 'Budget Master', path: '/finance/budgets', icon: '📊' },
    { label: 'Cashbook', path: '/finance/cashbook', icon: '💵' },
    { label: 'Reappropriation', path: '/namuna/reappropriation', icon: '🔄' },
    { label: 'Income & Expense', path: '/namuna/income_expense', icon: '📈' },
    { label: 'Assets & Liabilities', path: '/namuna/assets_liabilities', icon: '⚖️' },
    { label: 'Daily Cashbook', path: '/namuna/daily_cashbook', icon: '📅' },
    { label: 'Ledger', path: '/namuna/ledger', icon: '📓' },
    { label: 'Receipt', path: '/namuna/receipt', icon: '🧾' },
    
    // Taxation
    { label: 'Tax Assessment', path: '/namuna/tax_assessment', icon: '🏘️' },
    { label: 'Tax Demand', path: '/namuna/tax_demand', icon: '📝' },
    { label: 'Demand Notice', path: '/namuna/demand_notice', icon: '✉️' },
    { label: 'Tax Receipt', path: '/namuna/tax_receipt', icon: '💳' },
    { label: 'Misc Demand', path: '/namuna/misc_demand', icon: '📌' },

    // Works & Infrastructure
    { label: 'Work Estimate', path: '/namuna/work_estimate', icon: '🏗️' },
    { label: 'Measurement Book', path: '/namuna/measurement_book', icon: '📏' },
    { label: 'Work Bill', path: '/namuna/work_bill', icon: '📋' },
    { label: 'Road Register', path: '/namuna/road_register', icon: '🛣️' },
    { label: 'Land Register', path: '/namuna/land_register', icon: '🏞️' },

    // Administration
    { label: 'Employee Register', path: '/namuna/employee_register', icon: '👥' },
    { label: 'Attendance', path: '/namuna/attendance', icon: '🕒' },
    { label: 'Salary Payment', path: '/namuna/salary_payment', icon: '💰' },
    { label: 'Travel Allowance', path: '/namuna/travel_allowance', icon: '✈️' },
    
    // Inventory
    { label: 'Stamp Register', path: '/namuna/stamp_register', icon: '📜' },
    { label: 'Consumable Stock', path: '/namuna/consumable_stock', icon: '📦' },
    { label: 'Movable Assets', path: '/namuna/movable_assets', icon: '🚗' },
    { label: 'Immovable Assets', path: '/namuna/immovable_assets', icon: '🏢' },
    { label: 'Tree Register', path: '/namuna/tree_register', icon: '🌳' },

    // Audits & Advances
    { label: 'Advance Deposit', path: '/namuna/advance_deposit', icon: '💸' },
    { label: 'Petty Cash', path: '/namuna/petty_cash', icon: '🪙' },
    { label: 'Audit Objection', path: '/namuna/audit_objection', icon: '🔍' },
    { label: 'Audit Compliance', path: '/namuna/audit_compliance', icon: '✅' },
    { label: 'Reserved Fund', path: '/namuna/reserved_fund', icon: '🏦' },
    { label: 'Refund Order', path: '/namuna/refund_order', icon: '↩️' }
  ];
}
