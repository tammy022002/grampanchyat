import { Injectable } from '@angular/core';
import jsPDF from 'jspdf';
import autoTable from 'jspdf-autotable';
import { GridColumn } from '../../shared/components/data-grid/data-grid.component';

@Injectable({
  providedIn: 'root'
})
export class PdfService {

  generateRowReceipt(tableName: string, columns: GridColumn[], rowData: any) {
    const doc = new jsPDF();
    
    // Configurable Grampanchayat Info
    const gpName = 'GRAMPANCHAYAT OFFICE';
    const gpAddress = 'Grampanchayat Address, District, State - Pincode';
    
    // Header Setup
    doc.setFontSize(16);
    doc.setFont('helvetica', 'bold');
    
    // Center the Grampanchayat Name
    const pageWidth = doc.internal.pageSize.width || doc.internal.pageSize.getWidth();
    doc.text(gpName, pageWidth / 2, 20, { align: 'center' });
    
    // Center the Address
    doc.setFontSize(12);
    doc.setFont('helvetica', 'normal');
    doc.text(gpAddress, pageWidth / 2, 28, { align: 'center' });
    
    // Add a horizontal line
    doc.setLineWidth(0.5);
    doc.line(14, 32, pageWidth - 14, 32);

    // Generation Date
    const today = new Date().toLocaleDateString('en-GB');
    doc.setFontSize(10);
    doc.setFont('helvetica', 'italic');
    doc.text(`Generated On: ${today}`, 14, 40);
    
    // Title of the specific table record
    const formattedTitle = tableName.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
    doc.setFontSize(14);
    doc.setFont('helvetica', 'bold');
    doc.text(`${formattedTitle} - Record Details`, pageWidth / 2, 50, { align: 'center' });
    
    // Prepare Data for the Table
    const tableBody = columns.map(col => {
      let value = rowData[col.field];
      if (col.type === 'currency' && value !== null && value !== undefined) {
        value = '$' + parseFloat(value).toFixed(2);
      }
      return [col.header, value != null ? value.toString() : ''];
    });

    // Generate AutoTable
    autoTable(doc, {
      startY: 55,
      head: [['Field', 'Value']],
      body: tableBody,
      theme: 'grid',
      headStyles: { fillColor: [0, 86, 179] }, // Match primary button color
      styles: { fontSize: 11, cellPadding: 5 }
    });

    // Save the PDF
    const safeTitle = formattedTitle.replace(/[^a-zA-Z0-9]/g, '_');
    const recordId = rowData.id || 'record';
    doc.save(`${safeTitle}_${recordId}.pdf`);
  }
}
