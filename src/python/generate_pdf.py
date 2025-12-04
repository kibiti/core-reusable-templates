import sys
import json
from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader

def generate_pdf(template_path, output_pdf, data_json):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    
    # Load data
    with open(data_json, 'r') as f:
        data = json.load(f)
    
    # Render HTML
    html_content = template.render(**data)
    
    # Generate PDF
    HTML(string=html_content).write_pdf(output_pdf, stylesheets=[CSS(string=open('templates/common/_base_styles.css').read())])
    print(f"PDF generated: {output_pdf}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python generate_pdf.py <template-path> <output-pdf> <data-json>")
        sys.exit(1)
    generate_pdf(sys.argv[1], sys.argv[2], sys.argv[3])
