import { Injectable, signal, computed } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthStore {
  // State
  private _token = signal<string | null>(localStorage.getItem('token'));
  private _permissions = signal<string[]>([]);
  private _roles = signal<string[]>([]);
  private _username = signal<string | null>(null);

  // Selectors
  token = computed(() => this._token());
  isAuthenticated = computed(() => !!this._token());
  permissions = computed(() => this._permissions());
  roles = computed(() => this._roles());
  username = computed(() => this._username());

  // Actions
  setToken(token: string) {
    localStorage.setItem('token', token);
    this._token.set(token);
  }

  setUserDetails(username: string, roles: string[], permissions: string[]) {
    this._username.set(username);
    this._roles.set(roles);
    this._permissions.set(permissions);
  }

  logout() {
    localStorage.removeItem('token');
    this._token.set(null);
    this._username.set(null);
    this._roles.set([]);
    this._permissions.set([]);
  }

  hasPermission(permission: string): boolean {
    return this._permissions().includes(permission);
  }
}
