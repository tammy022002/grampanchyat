import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, tap } from 'rxjs';
import { AuthStore } from '../state/auth.store';
import { Router } from '@angular/router';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private http = inject(HttpClient);
  private authStore = inject(AuthStore);
  private router = inject(Router);
  
  login(username: string, password: string): Observable<any> {
    const body = new URLSearchParams();
    body.set('username', username);
    body.set('password', password);

    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded'
    });

    return this.http.post<any>('http://localhost:8000/api/v1/auth/login', body.toString(), { headers }).pipe(
      tap(res => {
        if (res.access_token) {
          this.authStore.setToken(res.access_token);
          this.authStore.setUserDetails(username, ['ADMIN'], ['finance:write', 'finance:read']);
          this.router.navigate(['/dashboard']);
        }
      })
    );
  }

  logout() {
    this.authStore.logout();
    this.router.navigate(['/auth/login']);
  }
}
