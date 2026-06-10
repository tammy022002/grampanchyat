import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { MENU_CONFIG } from '../../core/config/menu.config';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="dashboard-header">
      <h2>Gram Panchayat Command Center</h2>
      <p>Overview of Finances, Taxation, and Works.</p>
    </div>

    <!-- Summary Cards -->
    <div class="summary-cards">
      <div class="card bg-primary">
        <div class="card-icon">💰</div>
        <div class="card-info">
          <h3>₹45,23,000</h3>
          <p>Total Revenue (YTD)</p>
        </div>
      </div>
      
      <div class="card bg-warning">
        <div class="card-icon">⚠️</div>
        <div class="card-info">
          <h3>₹12,40,500</h3>
          <p>Pending Tax Demand</p>
        </div>
      </div>

      <div class="card bg-success">
        <div class="card-icon">🚧</div>
        <div class="card-info">
          <h3>14</h3>
          <p>Active Work Estimates</p>
        </div>
      </div>

      <div class="card bg-info">
        <div class="card-icon">👥</div>
        <div class="card-info">
          <h3>28</h3>
          <p>Total Employees</p>
        </div>
      </div>
    </div>

    <!-- All Namune Actions -->
    <div class="quick-actions-section">
      <h3>All Modules & Registers (33 Namune)</h3>
      
      <div *ngFor="let category of menuCategories" class="category-block">
        <h4 class="category-header">{{ category.title }}</h4>
        <div class="quick-actions">
          <button *ngFor="let item of category.items" class="action-btn" [routerLink]="item.path">
            <span class="icon">📄</span> {{ item.label }}
          </button>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .dashboard-header { margin-bottom: 30px; }
    .dashboard-header h2 { margin: 0; color: #2c3e50; font-size: 24px; }
    .dashboard-header p { margin: 5px 0 0 0; color: #7f8c8d; }
    
    .summary-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px; margin-bottom: 40px; }
    .card { display: flex; align-items: center; padding: 20px; border-radius: 8px; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .card-icon { font-size: 40px; margin-right: 20px; opacity: 0.8; }
    .card-info h3 { margin: 0; font-size: 28px; }
    .card-info p { margin: 5px 0 0 0; font-size: 14px; opacity: 0.9; }
    
    .bg-primary { background: linear-gradient(135deg, #3498db, #2980b9); }
    .bg-warning { background: linear-gradient(135deg, #f39c12, #d35400); }
    .bg-success { background: linear-gradient(135deg, #2ecc71, #27ae60); }
    .bg-info { background: linear-gradient(135deg, #9b59b6, #8e44ad); }

    .quick-actions-section h3 { margin-bottom: 5px; color: #2c3e50; font-size: 22px; }
    .category-block { margin-top: 25px; margin-bottom: 10px; background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.03); border: 1px solid #f0f0f0; }
    .category-header { color: #34495e; font-size: 16px; margin-top: 0; margin-bottom: 15px; border-bottom: 2px solid #ecf0f1; padding-bottom: 8px; }
    .quick-actions { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }
    .action-btn { display: flex; align-items: center; justify-content: flex-start; padding: 12px 15px; background-color: #f8f9fa; border: 1px solid #e0e0e0; border-radius: 6px; cursor: pointer; font-size: 14px; font-weight: 600; color: #2c3e50; transition: all 0.2s ease; }
    .action-btn:hover { background-color: #eaf2f8; border-color: #3498db; transform: translateY(-2px); box-shadow: 0 4px 8px rgba(0,0,0,0.05); color: #2980b9; }
    .action-btn .icon { font-size: 18px; margin-right: 12px; }
  `]
})
export class DashboardComponent {
  menuCategories = MENU_CONFIG;
}
