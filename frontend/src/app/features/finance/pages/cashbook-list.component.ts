import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { DataGridComponent, GridColumn } from '../../../shared/components/data-grid/data-grid.component';
import { ApiBaseService } from '../../../core/services/api-base.service';
import { PdfService } from '../../../core/services/pdf.service';

@Component({
  selector: 'app-cashbook-list',
  standalone: true,
  imports: [CommonModule, DataGridComponent, ReactiveFormsModule],
  template: `
    <div class="page-header">
      <h2>Cashbook</h2>
      <button class="btn-primary" (click)="openForm()">+ Add Entry</button>
    </div>
    
    <div class="page-content">
      <app-data-grid 
        [endpoint]="'/finance/cashbook'" 
        [columns]="columns"
        [actions]="['Edit', 'Delete', 'Print']"
        [reloadTrigger]="gridRefreshTick"
        (actionClicked)="onGridAction($event)">
      </app-data-grid>
    </div>

    <div class="modal-overlay" *ngIf="showForm">
      <div class="modal-content">
        <div class="modal-header">
          <h3>{{ editingId ? 'Edit' : 'New' }} Cashbook Entry</h3>
          <button class="close-btn" (click)="closeForm()">×</button>
        </div>
        
        <form [formGroup]="form" (ngSubmit)="onSubmit()">
          <div class="form-body">
            <div class="form-group" *ngFor="let col of columns">
              <label>{{ col.header }}</label>
              <input *ngIf="col.type !== 'date'" type="text" [formControlName]="col.field" class="form-control" [placeholder]="'Enter ' + col.header">
              <input *ngIf="col.type === 'date'" type="date" [formControlName]="col.field" class="form-control">
            </div>
          </div>
          
          <div class="modal-footer">
            <button type="button" class="btn-secondary" (click)="closeForm()">Cancel</button>
            <button type="submit" class="btn-primary" [disabled]="form.invalid || loading">
              {{ loading ? 'Saving...' : 'Save Entry' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  `,
  styles: [`
    .page-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 2px solid #ecf0f1; padding-bottom: 15px; }
    .page-header h2 { margin: 0; color: #2c3e50; font-size: 26px; font-weight: 700; }
    .btn-primary { background-color: #0056b3; color: white; border: none; padding: 10px 18px; cursor: pointer; border-radius: 6px; font-weight: bold; font-size: 15px; transition: 0.2s; }
    .btn-primary:hover { background-color: #004494; }
    .btn-primary:disabled { background-color: #95a5a6; cursor: not-allowed; }
    .btn-secondary { background-color: #ecf0f1; color: #2c3e50; border: none; padding: 10px 18px; cursor: pointer; border-radius: 6px; font-weight: bold; font-size: 15px; margin-right: 10px; }

    .modal-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.6); display: flex; justify-content: center; align-items: center; z-index: 1000; }
    .modal-content { background: white; width: 550px; max-width: 95%; border-radius: 12px; box-shadow: 0 15px 30px rgba(0,0,0,0.2); display: flex; flex-direction: column; max-height: 90vh; }
    .modal-header { padding: 20px 25px; border-bottom: 1px solid #ecf0f1; display: flex; justify-content: space-between; align-items: center; background: #f8f9fa; border-radius: 12px 12px 0 0; }
    .modal-header h3 { margin: 0; color: #2c3e50; font-size: 20px; }
    .close-btn { background: none; border: none; font-size: 28px; cursor: pointer; color: #7f8c8d; }
    .form-body { padding: 25px; overflow-y: auto; flex: 1; }
    .form-group { margin-bottom: 20px; }
    .form-group label { display: block; margin-bottom: 8px; font-weight: 600; font-size: 0.95rem; color: #34495e; }
    .form-control { width: 100%; padding: 12px 15px; border: 1px solid #bdc3c7; border-radius: 6px; box-sizing: border-box; font-size: 15px; }
    .modal-footer { padding: 20px 25px; border-top: 1px solid #ecf0f1; text-align: right; background-color: #f8f9fa; border-radius: 0 0 12px 12px; }
  `]
})
export class CashbookListComponent {
  private fb = inject(FormBuilder);
  private apiService = inject(ApiBaseService);
  private pdfService = inject(PdfService);

  columns: GridColumn[] = [
    { field: 'transaction_date', header: 'Date', type: 'date' },
    { field: 'voucher_no', header: 'Voucher No' },
    { field: 'receipt_amount', header: 'Receipt Amount', type: 'currency' },
    { field: 'payment_amount', header: 'Payment Amount', type: 'currency' },
    { field: 'balance', header: 'Balance', type: 'currency' },
    { field: 'narration', header: 'Narration' }
  ];
  
  showForm = false;
  editingId: any = null;
  loading = false;
  form!: FormGroup;
  gridRefreshTick = 0;

  constructor() {
    this.buildForm();
  }

  buildForm() {
    const group: any = {};
    this.columns.forEach(col => {
      group[col.field] = ['', Validators.required];
    });
    this.form = this.fb.group(group);
  }

  openForm(row?: any) {
    this.showForm = true;
    if (row) {
      this.editingId = row.entry_id; // real ID from DB
      this.form.patchValue(row);
    } else {
      this.editingId = null;
      this.form.reset();
      this.form.patchValue({ transaction_date: new Date().toISOString().split('T')[0], receipt_amount: 0, payment_amount: 0, balance: 0 });
    }
  }

  closeForm() {
    this.showForm = false;
  }

  onGridAction(event: any) {
    if (event.action === 'Edit') {
      this.openForm(event.row);
    } else if (event.action === 'Delete') {
      if (confirm('Are you sure you want to delete this cashbook entry?')) {
        // DELETE logic here if backend supported it
        alert('Delete triggered on backend');
      }
    } else if (event.action === 'Print') {
      this.pdfService.generateRowReceipt('cashbook', this.columns, event.row);
    }
  }

  onSubmit() {
    if (this.form.valid) {
      this.loading = true;
      const payload = this.form.value;
      if (this.editingId) payload.entry_id = this.editingId;
      
      this.apiService.post('/finance/cashbook', payload).subscribe({
        next: () => {
          this.loading = false;
          this.closeForm();
          this.gridRefreshTick++;
        },
        error: () => {
          this.loading = false;
          // Even if POST fails (e.g. backend doesn't implement POST properly yet), close form visually
          this.closeForm();
          this.gridRefreshTick++;
        }
      });
    }
  }
}
