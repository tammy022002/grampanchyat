import { Routes } from '@angular/router';

export const FINANCE_ROUTES: Routes = [
  {
    path: 'budgets',
    loadComponent: () => import('./pages/budget-list.component').then(m => m.BudgetListComponent)
  },
  {
    path: 'cashbook',
    loadComponent: () => import('./pages/cashbook-list.component').then(m => m.CashbookListComponent)
  }
];
