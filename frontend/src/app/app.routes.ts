import { Routes } from '@angular/router';
import { authGuard } from './core/auth/auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  {
    path: 'auth',
    loadChildren: () => import('./features/users/routes/auth.routes').then(m => m.AUTH_ROUTES)
  },
  {
    path: 'dashboard',
    loadComponent: () => import('./features/dashboard/dashboard.component').then(m => m.DashboardComponent),
    canActivate: [authGuard]
  },
  {
    path: 'finance',
    loadChildren: () => import('./features/finance/finance.routes').then(m => m.FINANCE_ROUTES),
    canActivate: [authGuard]
  },
  {
    path: 'namuna/:table',
    loadComponent: () => import('./shared/components/dynamic-namuna/dynamic-namuna.component').then(m => m.DynamicNamunaComponent),
    canActivate: [authGuard]
  }
];
