import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { AuthService } from '../../../core/auth/auth.service';
import { NotificationService } from '../../../core/services/notification.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  template: `
    <div class="login-wrapper">
      <div class="login-card">
        <h2>Gram Panchayat ERP</h2>
        <p class="subtitle">Secure Administrator Login</p>
        
        <form [formGroup]="loginForm" (ngSubmit)="onSubmit()">
          <div class="form-group">
            <label>Username</label>
            <input type="text" formControlName="username" class="form-control" placeholder="admin">
          </div>
          
          <div class="form-group">
            <label>Password</label>
            <input type="password" formControlName="password" class="form-control" placeholder="admin123">
          </div>
          
          <button type="submit" [disabled]="loginForm.invalid || loading" class="btn-primary">
            {{ loading ? 'Authenticating...' : 'Login' }}
          </button>
        </form>
      </div>
    </div>
  `,
  styles: [`
    .login-wrapper { display: flex; justify-content: center; align-items: center; height: 100vh; background-color: #2c3e50; }
    .login-card { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); width: 100%; max-width: 350px; text-align: center; }
    h2 { margin-top: 0; color: #2c3e50; }
    .subtitle { color: #7f8c8d; margin-bottom: 24px; font-size: 0.9rem; }
    .form-group { text-align: left; margin-bottom: 20px; }
    .form-group label { display: block; margin-bottom: 8px; font-weight: bold; font-size: 0.9rem; color: #34495e; }
    .form-control { width: 100%; padding: 12px; border: 1px solid #bdc3c7; border-radius: 4px; box-sizing: border-box; font-size: 1rem; }
    .form-control:focus { outline: none; border-color: #3498db; }
    .btn-primary { width: 100%; padding: 14px; background-color: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; transition: background-color 0.2s; }
    .btn-primary:hover { background-color: #2980b9; }
    .btn-primary:disabled { background-color: #95a5a6; cursor: not-allowed; }
  `]
})
export class LoginComponent {
  private fb = inject(FormBuilder);
  private authService = inject(AuthService);
  private notificationService = inject(NotificationService);

  loginForm = this.fb.nonNullable.group({
    username: ['admin', Validators.required],
    password: ['admin123', Validators.required]
  });

  loading = false;

  onSubmit() {
    if (this.loginForm.valid) {
      this.loading = true;
      const { username, password } = this.loginForm.getRawValue();
      
      this.authService.login(username, password).subscribe({
        next: () => {
          this.loading = false;
          this.notificationService.showSuccess('Success', 'Login Successful!');
        },
        error: (err) => {
          this.loading = false;
          // error interceptor handles the toast
        }
      });
    }
  }
}
