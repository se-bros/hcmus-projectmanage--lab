import sys
import os
import markdown
import re
import zlib
import string
import base64
from playwright.sync_api import sync_playwright

def deflate_and_encode(plantuml_text):
    # Step 1: UTF-8 encode
    utf8_bytes = plantuml_text.encode('utf-8')
    # Step 2: Deflate (raw format: wbits=-15)
    compressor = zlib.compressobj(level=9, method=zlib.DEFLATED, wbits=-15)
    compressed_bytes = compressor.compress(utf8_bytes) + compressor.flush()
    
    # Step 3: Re-encode with PlantUML base64 alphabet
    puml_alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + '-_'
    standard_b64 = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/'
    
    # Standard base64 encoding first
    b64_bytes = base64.b64encode(compressed_bytes)
    b64_str = b64_bytes.decode('ascii')
    
    # Translate standard base64 to PlantUML base64
    translation_table = str.maketrans(standard_b64, puml_alphabet)
    puml_encoded = b64_str.translate(translation_table).replace('=', '')
    return puml_encoded

def replace_plantuml_blocks(md_text):
    pattern = re.compile(r'```plantuml\s*\n(.*?)\n```', re.DOTALL)
    
    def replacer(match):
        puml_code = match.group(1).strip()
        try:
            encoded = deflate_and_encode(puml_code)
            # Use SVG for crisp vector graphics in PDF
            url = f"https://www.plantuml.com/plantuml/svg/{encoded}"
            return f'\n\n<div class="diagram-container"><img src="{url}" class="plantuml-diagram" alt="PlantUML Diagram"></div>\n\n'
        except Exception as e:
            print(f"Failed to encode PlantUML: {e}")
            return match.group(0)
            
    return pattern.sub(replacer, md_text)

def convert_md_to_pdf(md_path, pdf_path):
    # Read Markdown content
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    # Clean YAML frontmatter if present
    if md_text.startswith('---'):
        parts = md_text.split('---', 2)
        if len(parts) >= 3:
            md_text = parts[2]
            
    # Pre-process Markdown to convert PlantUML code blocks to interactive SVG URLs
    md_text = replace_plantuml_blocks(md_text)
            
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'toc'])
    
    # Try to load premium CSS from md-to-pdf skill
    script_dir = os.path.dirname(os.path.abspath(__file__))
    premium_css_path = os.path.abspath(os.path.join(script_dir, '..', '..', 'md-to-pdf', 'resources', 'markdown-pdf-premium.css'))
    
    css_content = ""
    if os.path.exists(premium_css_path):
        with open(premium_css_path, 'r', encoding='utf-8') as css_f:
            css_content = css_f.read()
    else:
        # Fallback stylesheet
        css_content = """
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                line-height: 1.6;
                color: #333;
                padding: 0;
                margin: 0;
                background: #fff;
            }
            h1, h2, h3, h4, h5, h6 {
                color: #111;
                margin-top: 1.5em;
                margin-bottom: 0.5em;
                font-weight: 600;
            }
            h1 {
                font-size: 2em;
                border-bottom: 2px solid #007799;
                padding-bottom: 0.3em;
                margin-top: 0;
            }
            h2 {
                font-size: 1.5em;
                border-bottom: 1px solid #ddd;
                padding-bottom: 0.2em;
                color: #005577;
            }
            h3 {
                font-size: 1.25em;
                color: #333;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 0.95em;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 10px 12px;
                text-align: left;
                vertical-align: top;
            }
            th {
                background-color: #f2f7f9;
                color: #005577;
                font-weight: 600;
            }
            tr:nth-child(even) {
                background-color: #fafafa;
            }
            blockquote {
                border-left: 4px solid #007799;
                padding: 12px 20px;
                margin: 20px 0;
                background-color: #f9fbfd;
                color: #444;
            }
            code {
                font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
                background-color: #f4f4f4;
                padding: 2px 6px;
                border-radius: 4px;
                font-size: 0.85em;
                color: #d14;
            }
            pre {
                background-color: #f6f8fa;
                padding: 16px;
                border-radius: 6px;
                overflow-x: auto;
                border: 1px solid #eaeef2;
            }
            pre code {
                background-color: transparent;
                padding: 0;
                color: inherit;
                font-size: 0.85em;
            }
            img {
                max-width: 100%;
                height: auto;
                display: block;
                margin: 20px auto;
            }
            hr {
                border: 0;
                border-top: 1px solid #ddd;
                margin: 30px 0;
            }
        """

    # Add style rules for diagram containers
    css_content += "\n.diagram-container { text-align: center; margin: 25px 0; page-break-inside: avoid; }\n.plantuml-diagram { max-width: 75%; max-height: 450px; height: auto; border: 1px solid #eaeaea; border-radius: 6px; padding: 10px; background-color: #fff; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }\n"

    # Styled HTML
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            {css_content}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Save temporary html file
    temp_html_path = md_path + '.temp.html'
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(styled_html)
        
    try:
        # Run playwright to print pdf
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            # Convert file path to absolute URL
            abs_html_path = os.path.abspath(temp_html_path)
            file_url = f"file:///{abs_html_path.replace(os.sep, '/')}"
            page.goto(file_url)
            page.wait_for_load_state("networkidle")
            page.pdf(
                path=pdf_path, 
                format="A4", 
                margin={"top": "15mm", "bottom": "15mm", "left": "10mm", "right": "10mm"},
                print_background=True
            )
            browser.close()
        print(f"Successfully generated PDF: {pdf_path}")
    finally:
        if os.path.exists(temp_html_path):
            os.remove(temp_html_path)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python md_to_pdf.py <input.md> <output.pdf>")
        sys.exit(1)
    md_in = sys.argv[1]
    pdf_out = sys.argv[2]
    convert_md_to_pdf(md_in, pdf_out)
