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

def replace_diagram_blocks(md_text):
    # 1. PlantUML blocks
    puml_pattern = re.compile(r'```plantuml\s*\n(.*?)\n```', re.DOTALL)
    def puml_replacer(match):
        puml_code = match.group(1).strip()
        try:
            encoded = deflate_and_encode(puml_code)
            url = f"https://www.plantuml.com/plantuml/svg/{encoded}"
            return f'\n\n<div class="diagram-container"><img src="{url}" class="plantuml-diagram" alt="PlantUML Diagram"></div>\n\n'
        except Exception as e:
            print(f"Failed to encode PlantUML: {e}")
            return match.group(0)
    md_text = puml_pattern.sub(puml_replacer, md_text)
    
    # 2. Mermaid blocks
    mermaid_pattern = re.compile(r'```mermaid\s*\n(.*?)\n```', re.DOTALL)
    def mermaid_replacer(match):
        mermaid_code = match.group(1).strip()
        return f'\n\n<pre class="mermaid">\n{mermaid_code}\n</pre>\n\n'
    md_text = mermaid_pattern.sub(mermaid_replacer, md_text)
    
    return md_text

def get_styled_html(md_path, font_size="10pt"):
    # Read Markdown content
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    # Clean YAML frontmatter if present
    if md_text.startswith('---'):
        parts = md_text.split('---', 2)
        if len(parts) >= 3:
            md_text = parts[2]
            
    # Pre-process Markdown for diagrams
    md_text = replace_diagram_blocks(md_text)
            
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_text, extensions=['tables', 'fenced_code', 'toc', 'sane_lists'])
    
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
        """

    # Enforce the body font size and style diagrams.
    css_content += f"\nbody {{ font-size: {font_size} !important; }}\n@media print {{ body {{ font-size: {font_size} !important; }} }}\n.diagram-container {{ text-align: center; margin: 25px 0; page-break-inside: avoid; }}\n.plantuml-diagram {{ max-width: 85%; max-height: 500px; height: auto; border: 1px solid #eaeaea; border-radius: 6px; padding: 10px; background-color: #fff; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }}\n"

    # Mermaid JS script if mermaid diagrams exist
    mermaid_script = ""
    if 'class="mermaid"' in html_content:
        mermaid_script = """
        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({ startOnLoad: true, theme: 'neutral' });
        </script>
        """

    # Extract title from markdown or filename
    title = os.path.basename(md_path)
    title_match = re.search(r'#\s+(.+)', md_text)
    if title_match:
        title = title_match.group(1).strip()

    styled_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    <style>
        {css_content}
    </style>
    {mermaid_script}
</head>
<body>
    {html_content}
</body>
</html>"""
    return styled_html, ('class="mermaid"' in html_content)

def convert_single_md(page, md_path, pdf_path):
    styled_html, has_mermaid = get_styled_html(md_path)
    temp_html_path = md_path + '.temp.html'
    
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(styled_html)
        
    try:
        abs_html_path = os.path.abspath(temp_html_path)
        file_url = f"file:///{abs_html_path.replace(os.sep, '/')}"
        page.goto(file_url, wait_until="networkidle")
        if has_mermaid:
            page.wait_for_timeout(1500)
            
        os.makedirs(os.path.dirname(os.path.abspath(pdf_path)), exist_ok=True)
        page.pdf(
            path=pdf_path, 
            format="A4", 
            margin={"top": "15mm", "bottom": "15mm", "left": "15mm", "right": "15mm"},
            print_background=True,
            display_header_footer=True,
            header_template='<div style="font-size: 8px; width: 100%; text-align: right; margin-right: 20px; color: #999;"><span class="title"></span></div>',
            footer_template='<div style="font-size: 8px; width: 100%; text-align: center; color: #999;">Page <span class="pageNumber"></span> / <span class="totalPages"></span></div>'
        )
        print(f"Successfully generated PDF: {pdf_path}")
        return True
    except Exception as e:
        print(f"Error generating PDF for {md_path}: {e}")
        return False
    finally:
        if os.path.exists(temp_html_path):
            try:
                os.remove(temp_html_path)
            except Exception:
                pass

def convert_files(file_pairs):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        for md_path, pdf_path in file_pairs:
            print(f"Processing: {md_path} -> {pdf_path}")
            convert_single_md(page, md_path, pdf_path)
        browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python md_to_pdf.py <input.md> <output.pdf>")
        print("  python md_to_pdf.py --batch <file1.md> <file2.md> ...")
        sys.exit(1)
        
    if sys.argv[1] == "--batch":
        md_files = sys.argv[2:]
        file_pairs = [(f, os.path.splitext(f)[0] + ".pdf") for f in md_files if f.endswith(".md")]
        convert_files(file_pairs)
    elif len(sys.argv) == 3:
        md_in = sys.argv[1]
        pdf_out = sys.argv[2]
        convert_files([(md_in, pdf_out)])
    else:
        md_files = [f for f in sys.argv[1:] if f.endswith(".md")]
        file_pairs = [(f, os.path.splitext(f)[0] + ".pdf") for f in md_files]
        convert_files(file_pairs)
