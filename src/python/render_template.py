import sys
import json
from jinja2 import Environment, FileSystemLoader

def render_template(template_path, data_json, output_html):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_path)
    
    # Load data
    with open(data_json, 'r') as f:
        data = json.load(f)
    
    # Render and save
    html_content = template.render(**data)
    with open(output_html, 'w') as f:
        f.write(html_content)
    print(f"HTML rendered: {output_html}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python render_template.py <template-path> <data-json> <output-html>")
        sys.exit(1)
    render_template(sys.argv[1], sys.argv[2], sys.argv[3])
