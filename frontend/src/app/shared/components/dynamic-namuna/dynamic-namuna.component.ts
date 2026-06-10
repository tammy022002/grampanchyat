import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { DataGridComponent, GridColumn } from '../data-grid/data-grid.component';
import { HasPermissionDirective } from '../../directives/has-permission.directive';
import { ApiBaseService } from '../../../core/services/api-base.service';
import { PdfService } from '../../../core/services/pdf.service';
import { NamunaSchemaRegistry } from './namuna-schema.registry';

@Component({
  selector: 'app-dynamic-namuna',
  standalone: true,
  imports: [CommonModule, DataGridComponent, HasPermissionDirective, ReactiveFormsModule],
  template: `
    <div class="page-header">
      <h2>{{ formatTitle(tableName) }}</h2>
      <button class="btn-primary" (click)="openForm()">+ Add Entry</button>
    </div>
    
    <div class="page-content">
      <app-data-grid 
        [endpoint]="'/namuna/' + tableName" 
        [columns]="columns"
        [actions]="['Edit', 'Delete', 'Print']"
        [reloadTrigger]="gridRefreshTick"
        (actionClicked)="onGridAction($event)">
      </app-data-grid>
    </div>

    <!-- Dynamic Form Modal Overlay -->
    <div class="modal-overlay" *ngIf="showForm">
      <div class="modal-content">
        <div class="modal-header">
          <h3>{{ editingId ? 'Edit' : 'New' }} {{ formatTitle(tableName) }}</h3>
          <button class="close-btn" (click)="closeForm()">×</button>
        </div>
        
        <form [formGroup]="form" (ngSubmit)="onSubmit()">
          <div class="form-body">
            <div class="form-group" *ngFor="let col of formColumns">
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
    .btn-primary { background-color: #0056b3; color: white; border: none; padding: 10px 18px; cursor: pointer; border-radius: 6px; font-weight: bold; font-size: 15px; transition: 0.2s; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    .btn-primary:hover { background-color: #004494; transform: translateY(-1px); box-shadow: 0 4px 8px rgba(0,0,0,0.15); }
    .btn-primary:disabled { background-color: #95a5a6; cursor: not-allowed; transform: none; box-shadow: none; }
    .btn-secondary { background-color: #ecf0f1; color: #2c3e50; border: none; padding: 10px 18px; cursor: pointer; border-radius: 6px; font-weight: bold; font-size: 15px; margin-right: 10px; transition: 0.2s; }
    .btn-secondary:hover { background-color: #bdc3c7; }

    .modal-overlay { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.6); display: flex; justify-content: center; align-items: center; z-index: 1000; backdrop-filter: blur(3px); }
    .modal-content { background: white; width: 550px; max-width: 95%; border-radius: 12px; box-shadow: 0 15px 30px rgba(0,0,0,0.2); display: flex; flex-direction: column; max-height: 90vh; }
    .modal-header { padding: 20px 25px; border-bottom: 1px solid #ecf0f1; display: flex; justify-content: space-between; align-items: center; background: #f8f9fa; border-radius: 12px 12px 0 0; }
    .modal-header h3 { margin: 0; color: #2c3e50; font-size: 20px; }
    .close-btn { background: none; border: none; font-size: 28px; cursor: pointer; color: #7f8c8d; line-height: 1; transition: 0.2s; }
    .close-btn:hover { color: #e74c3c; }
    .form-body { padding: 25px; overflow-y: auto; flex: 1; }
    .form-group { margin-bottom: 20px; }
    .form-group label { display: block; margin-bottom: 8px; font-weight: 600; font-size: 0.95rem; color: #34495e; }
    .form-control { width: 100%; padding: 12px 15px; border: 1px solid #bdc3c7; border-radius: 6px; box-sizing: border-box; font-size: 15px; transition: border-color 0.2s; }
    .form-control:focus { outline: none; border-color: #3498db; box-shadow: 0 0 0 3px rgba(52,152,219,0.1); }
    .modal-footer { padding: 20px 25px; border-top: 1px solid #ecf0f1; text-align: right; background-color: #f8f9fa; border-radius: 0 0 12px 12px; }
  `]
})
export class DynamicNamunaComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private fb = inject(FormBuilder);
  private apiService = inject(ApiBaseService);
  private pdfService = inject(PdfService);

  tableName = '';
  columns: GridColumn[] = [];
  formColumns: GridColumn[] = [];
  
  showForm = false;
  editingId: any = null;
  loading = false;
  form!: FormGroup;
  gridRefreshTick = 0;

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.tableName = params.get('table') || '';
      
      // Load columns dynamically from Schema Registry, fallback to generic if undefined
      this.columns = NamunaSchemaRegistry[this.tableName] || [
        { field: 'id', header: 'Record ID' },
        { field: 'created_at', header: 'Date', type: 'date' },
        { field: 'description', header: 'Details / Description' },
        { field: 'amount', header: 'Amount/Value', type: 'currency' },
        { field: 'status', header: 'Status' }
      ];
      this.formColumns = this.columns.filter(c => c.field !== 'id');
      this.buildForm();
    });
  }

  buildForm() {
    const group: any = {};
    this.formColumns.forEach(col => {
      group[col.field] = ['', Validators.required];
    });
    this.form = this.fb.group(group);
  }

  openForm(row?: any) {
    this.showForm = true;
    if (row) {
      this.editingId = row.id;
      this.form.patchValue(row);
    } else {
      this.editingId = null;
      this.form.reset();
      if (this.form.contains('created_at')) {
        this.form.patchValue({ created_at: new Date().toISOString().split('T')[0] });
      }
    }
  }

  closeForm() {
    this.showForm = false;
  }

  onGridAction(event: any) {
    if (event.action === 'Edit') {
      this.openForm(event.row);
    } else if (event.action === 'Delete') {
      if (confirm('Are you sure you want to delete this record?')) {
        this.apiService.delete('/namuna/' + this.tableName + '?id=' + event.row.id).subscribe(() => {
          this.gridRefreshTick++;
        });
      }
    } else if (event.action === 'Print') {
      this.pdfService.generateRowReceipt(this.tableName, this.columns, event.row);
    }
  }

  onSubmit() {
    if (this.form.valid) {
      this.loading = true;
      const payload = this.form.value;
      if (this.editingId) payload.id = this.editingId;
      
      this.apiService.post('/namuna/' + this.tableName, payload).subscribe({
        next: () => {
          this.loading = false;
          this.closeForm();
          this.gridRefreshTick++;
        },
        error: () => this.loading = false
      });
    }
  }

  formatTitle(name: string): string {
    return name.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
  }
}
