import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthStore } from '../state/auth.store';

export const authGuard: CanActivateFn = (route, state) => {
  const authStore = inject(AuthStore);
  const router = inject(Router);

  if (authStore.isAuthenticated()) {
    return true;
  }

  return router.parseUrl('/auth/login');
};

export const permissionGuard: CanActivateFn = (route, state) => {
  const authStore = inject(AuthStore);
  const router = inject(Router);
  
  const requiredPermission = route.data['permission'] as string;
  
  if (!requiredPermission || authStore.hasPermission(requiredPermission)) {
    return true;
  }

  return router.parseUrl('/unauthorized');
};
