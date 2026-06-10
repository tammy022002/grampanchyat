import { Component, inject } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { CommonModule } from '@angular/common';
import { AuthStore } from './core/state/auth.store';
import { AuthService } from './core/auth/auth.service';
import { MENU_CONFIG } from './core/config/menu.config';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  authStore = inject(AuthStore);
  authService = inject(AuthService);
  menuCategories = MENU_CONFIG;

  logout() {
    this.authService.logout();
  }
}
