import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';
import { NotificationService } from '../services/notification.service';
import { AuthStore } from '../state/auth.store';
import { Router } from '@angular/router';

export const errorInterceptor: HttpInterceptorFn = (req, next) => {
  const notificationService = inject(NotificationService);
  const authStore = inject(AuthStore);
  const router = inject(Router);

  return next(req).pipe(
    catchError((error) => {
      if (error.status === 401) {
        // Handle token expiration / unauthorized
        notificationService.showError('Session Expired', 'Please login again.');
        authStore.logout();
        router.navigate(['/auth/login']);
      } else if (error.status === 403) {
        notificationService.showError('Access Denied', 'You do not have permission for this action.');
      } else if (error.status === 422) {
        // Validation Error
        const msg = error.error?.message || 'Validation failed';
        notificationService.showError('Validation Error', msg);
      } else {
        const msg = error.error?.message || 'An unexpected error occurred.';
        notificationService.showError('Error', msg);
      }
      return throwError(() => error);
    })
  );
};
