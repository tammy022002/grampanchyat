import { Component, Input, Output, EventEmitter, signal, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiBaseService } from '../../../core/services/api-base.service';

export interface GridColumn {
  field: string;
  header: string;
  type?: 'text' | 'date' | 'currency' | 'number';
}

@Component({
  selector: 'app-data-grid',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="grid-container">
      <table class="data-table">
        <thead>
          <tr>
            <th *ngFor="let col of columns" (click)="onSort(col.field)">
              {{ col.header }}
              <span *ngIf="sortField() === col.field">
                {{ sortOrder() === 'asc' ? '↑' : '↓' }}
              </span>
            </th>
            <th *ngIf="actions.length > 0">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr *ngFor="let row of data()">
            <td *ngFor="let col of columns">
              {{ formatCell(row[col.field], col.type) }}
            </td>
            <td *ngIf="actions.length > 0">
              <button *ngFor="let action of actions" (click)="onAction(action, row)">
                {{ action }}
              </button>
            </td>
          </tr>
          <tr *ngIf="data().length === 0 && !loading()">
            <td [colSpan]="columns.length + (actions.length > 0 ? 1 : 0)" class="text-center">No data found</td>
          </tr>
          <tr *ngIf="loading()">
            <td [colSpan]="columns.length + (actions.length > 0 ? 1 : 0)" class="text-center">Loading...</td>
          </tr>
        </tbody>
      </table>

      <!-- Pagination Controls -->
      <div class="pagination" *ngIf="total() > 0">
        <button [disabled]="page() === 1" (click)="changePage(page() - 1)">Previous</button>
        <span>Page {{ page() }} of {{ pages() }}</span>
        <button [disabled]="page() === pages()" (click)="changePage(page() + 1)">Next</button>
      </div>
    </div>
  `,
  styles: [`
    .grid-container { width: 100%; overflow-x: auto; }
    .data-table { width: 100%; border-collapse: collapse; }
    .data-table th, .data-table td { border: 1px solid #ddd; padding: 8px; }
    .data-table th { background-color: #f2f2f2; text-align: left; cursor: pointer; }
    .pagination { margin-top: 10px; display: flex; justify-content: space-between; }
    .text-center { text-align: center; padding: 20px; }
  `]
})
export class DataGridComponent implements OnInit {
  private _endpoint!: string;
  
  @Input({ required: true }) 
  set endpoint(val: string) {
    if (this._endpoint !== val) {
      this._endpoint = val;
      // Only load data if we have already initialized (to prevent double-loading on init)
      if (this.initialized) {
        this.page.set(1);
        this.loadData();
      }
    }
  }
  get endpoint(): string {
    return this._endpoint;
  }

  @Input({ required: true }) columns: GridColumn[] = [];
  @Input() actions: string[] = ['Edit', 'Delete', 'Print'];
  @Input() set reloadTrigger(val: number) {
    if (val > 0) {
      this.loadData();
    }
  }
  
  @Output() actionClicked = new EventEmitter<{ action: string, row: any }>();

  private apiService = inject(ApiBaseService);

  // State Signals
  data = signal<any[]>([]);
  total = signal(0);
  page = signal(1);
  size = signal(10);
  pages = signal(0);
  loading = signal(false);
  sortField = signal<string | null>(null);
  sortOrder = signal<'asc' | 'desc'>('asc');
  filters = signal<any>({});
  
  private initialized = false;

  ngOnInit() {
    this.initialized = true;
    this.loadData();
  }

  loadData() {
    if (!this.endpoint) return;
    this.loading.set(true);
    const params = { 
      page: this.page(), 
      size: this.size(), 
      sort: this.sortField(), 
      order: this.sortOrder(), 
      ...this.filters() 
    };
    
    this.apiService.get<any>(this.endpoint, params).subscribe({
      next: (res) => {
        this.data.set(res.data.items);
        this.total.set(res.data.total);
        this.pages.set(res.data.pages);
        this.loading.set(false);
      },
      error: () => this.loading.set(false)
    });
  }

  changePage(newPage: number) {
    this.page.set(newPage);
    this.loadData();
  }

  onSort(field: string) {
    if (this.sortField() === field) {
      this.sortOrder.set(this.sortOrder() === 'asc' ? 'desc' : 'asc');
    } else {
      this.sortField.set(field);
      this.sortOrder.set('asc');
    }
    this.page.set(1); // Reset to first page
    this.loadData();
  }

  onAction(action: string, row: any) {
    this.actionClicked.emit({ action, row });
  }

  formatCell(value: any, type?: string) {
    if (!value) return '';
    if (type === 'currency') return '$' + parseFloat(value).toFixed(2);
    // Add Date and other formatting as needed
    return value;
  }
}
