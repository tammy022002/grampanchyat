import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

export interface ToastMessage {
  type: 'success' | 'error' | 'warning' | 'info';
  title: string;
  message: string;
}

@Injectable({
  providedIn: 'root'
})
export class NotificationService {
  private _toasts = new BehaviorSubject<ToastMessage[]>([]);
  public toasts$ = this._toasts.asObservable();

  showSuccess(title: string, message: string) {
    this.addToast({ type: 'success', title, message });
  }

  showError(title: string, message: string) {
    this.addToast({ type: 'error', title, message });
  }

  private addToast(toast: ToastMessage) {
    const current = this._toasts.value;
    this._toasts.next([...current, toast]);
    
    // Auto remove after 5 seconds
    setTimeout(() => {
      this.removeToast(toast);
    }, 5000);
  }

  removeToast(toast: ToastMessage) {
    const current = this._toasts.value;
    this._toasts.next(current.filter(t => t !== toast));
  }
}
