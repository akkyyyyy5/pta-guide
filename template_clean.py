import os
import re

def clean_body_file(content):
    # 1. Fix the [domain]" target="_blank" style="color:#1a73e8;">... pattern
    domains = {
        "docs.google.com": "https://docs.google.com",
        "drive.google.com": "https://drive.google.com",
        "forms.google.com": "https://forms.google.com",
        "meet.google.com": "https://meet.google.com",
        "sheets.google.com": "https://sheets.google.com",
        "canva.com": "https://canva.com",
        "chouseisan.com": "https://chouseisan.com",
        "line.worksmobile.com": "https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2",
        "jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2": "https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2"
    }
    
    for dom, url in domains.items():
        # Case 1: domain followed by attributes
        bad_pattern = re.escape(dom) + r'["\']?\s*target=["\']_blank["\']\s*style=["\']color:#1a73e8;["\']>\s*'
        content = re.sub(bad_pattern, f'<a href="{url}" target="_blank" class="text-link">{dom}</a>', content, flags=re.I)
        
        # Case 2: attributes followed by doubled tags
        bad_pattern_2 = r'style=["\']color:#1a73e8;["\']>\s*<a[^>]*>' + re.escape(dom) + r'</a>'
        content = re.sub(bad_pattern_2, f'<a href="{url}" target="_blank" class="text-link">{dom}</a>', content, flags=re.I)

        # Case 3: double link tags without garbage
        bad_pattern_3 = r'<a[^>]*>' + re.escape(dom) + r'</a>\s*<a[^>]*>' + re.escape(dom) + r'</a>'
        content = re.sub(bad_pattern_3, f'<a href="{url}" target="_blank" class="text-link">{dom}</a>', content, flags=re.I)

    # 2. General safety
    content = re.sub(r'</a>\s*</a>', '</a>', content)
    content = re.sub(r'</a>\s*</strong>\s*</a>', '</strong></a>', content)
    
    # 3. Fix the specific sheets.google.com line 19 in sheets_body.html
    content = content.replace('sheets.google.com" target="_blank"\n                style="color:#1a73e8;">', '<a href="https://sheets.google.com" target="_blank" class="text-link">sheets.google.com</a>')

    return content

def process():
    body_files = [f for f in os.listdir('.') if f.endswith('_body.html')]
    # Also add standard files and quick ones
    body_files += ["docs.html", "drive.html", "forms.html", "meet.html", "sheets.html", "lineworks.html", "canva.html", "chouseisan.html", "quick.html", "modern_quick.html", "kawaii_quick.html"]
    
    for f in body_files:
        if not os.path.exists(f): continue
        print(f"Template Clean: {f}")
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        fixed = clean_body_file(content)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(fixed)

if __name__ == "__main__":
    process()
