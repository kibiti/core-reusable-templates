# Core Reusable Templates for Elimuhub Education Consultants

This repository provides reusable HTML templates for Elimuhub Education Consultants' services, including reports, certificates, forms, invoices, packages, and tutor receipts. Templates are modular, use Jinja2 for dynamic data, and can be converted to PDF for sharing/printing.

## Features
- **Categorized Templates**: Organized by type (e.g., reports, certificates).
- **Common Components**: Shared headers, footers, and styles.
- **PDF Generation**: Python-based script using WeasyPrint.
- **CI/CD**: Automated testing and PDF generation via GitHub Actions.
- **Testing**: Unit tests for rendering and output.

## Setup
1. Clone: `git clone https://github.com/kibiti/core-reusable-templates.git`
2. Install: `pip install -r requirements.txt`
3. Render template: `python src/python/render_template.py <template> <data.json> <output.html>`
4. Generate PDF: `python src/python/generate_pdf.py <html-path> <output-pdf> <data.json>`

## Templates Overview
- `attendance/`: Attendance sheets.
- `certificates/`: Achievement/completion certs.
- `forms/`: Application/feedback forms.
- `invoices/`: Invoice templates.
- `packages/`: Tuition/package details.
- `reports/`: Academic/financial/project reports.
- `tutor/`: Tutor invoices/receipts.

## License
MIT.
