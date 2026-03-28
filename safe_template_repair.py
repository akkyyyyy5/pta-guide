import os
import re

def safe_fix(content, domain, url):
    # Pattern 1: [domain]" target="_blank" style="color:#1a73e8;">[strong?][domain][strong?]</a>
    # This is the most common mess.
    messy_pattern = re.escape(domain) + r'["\']?\s*target=["\']_blank["\']\s*style=["\']color:#1a73e8;["\?]?>(?:<strong>)?' + re.escape(domain) + r'(?:</strong>)?</a>'
    content = re.sub(messy_pattern, f'<strong><a href="{url}" target="_blank" class="text-link">{domain}</a></strong>', content)

    # Pattern 2: the "target=..." leak on its own
    content = re.sub(r'["\']?\s*target=["\']_blank["\']\s*style=["\']color:#1a73e8;["\?]>', '', content)
    
    # Pattern 3: double strong tags
    content = content.replace(f'<strong><strong><a href="{url}"', f'<strong><a href="{url}"')
    content = content.replace(f'</a></strong></strong>', f'</a></strong>')

    return content

def process():
    tools = {
        "docs_body.html": ("docs.google.com", "https://docs.google.com"),
        "drive_body.html": ("drive.google.com", "https://drive.google.com"),
        "forms_body.html": ("forms.google.com", "https://forms.google.com"),
        "meet_body.html": ("meet.google.com", "https://meet.google.com"),
        "sheets_body.html": ("sheets.google.com", "https://sheets.google.com"),
        "lw_body.html": ("line.worksmobile.com", "https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2"),
        "canva_body.html": ("canva.com", "https://canva.com"),
        "chouseisan_body.html": ("chouseisan.com", "https://chouseisan.com")
    }
    
    for f, (dom, url) in tools.items():
        if not os.path.exists(f): continue
        print(f"Repairing {f}...")
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Exact replacement for the common "Step 1" leak
        content = safe_fix(content, dom, url)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

if __name__ == "__main__":
    process()
