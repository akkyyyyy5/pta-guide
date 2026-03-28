import os
import re

# Base directory for the pta-guide
base_dir = r'f:\Antigravity\ニュースを自動で収集\pta-guide'

# All relevant source templates and body files
files_to_repair = [
    'docs_body.html', 'drive_body.html', 'forms_body.html',
    'sheets_body.html', 'meet_body.html', 'lw_body.html',
    'canva_body.html', 'chouseisan_body.html',
    'body_p1.html', 'body_p2.html', 'body_p3.html', 'body_p4.html',
    'idx_body.html', 'forms_quick_body.html'
]

def repair_file(filename):
    path = os.path.join(base_dir, filename)
    if not os.path.exists(path):
        print(f"File not found: {filename}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern: <a href="https://URL> (missing quote and >)
    # Correct it to: <a href="URL" target="_blank" class="text-link">
    
    # regex matches: <a href="https://[anything_not_bracket_or_quote]> or just any broken link
    # We want to be careful not to break already correct tags.
    
    # This specifically targets the common broken pattern found in grep
    # <a href="https://xxx.com>
    repaired_content = re.sub(r'<a href="?(https?://[^">]+)>', r'<a href="\1" target="_blank" class="text-link">', content)
    
    # Also fix URLs that were somehow partially linkified like:
    # URL" target="_blank" style="color:#1a73e8;">URL
    # (Clean them up back to plain text first, then we let the rebuild script do it right)
    repaired_content = re.sub(r'(https?://[^"\s<>]+)" target="_blank"[^>]*>', r'\1', repaired_content)

    if repaired_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(repaired_content)
        print(f"Repaired: {filename}")
    else:
        print(f"No repair needed: {filename}")

if __name__ == "__main__":
    for f in files_to_repair:
        repair_file(f)
