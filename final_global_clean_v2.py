import os
import re

def final_global_clean(content):
    # Fix the persistent leakage pattern: [domain]" target="_blank" style="color:#1a73e8;">
    domains = ["docs.google.com", "drive.google.com", "forms.google.com", "meet.google.com", "canva.com", "chouseisan.com", "www.canva.com"]
    
    for dom in domains:
        # Leakage after a domain string
        leak_pattern = dom + r'["\'] target=["\']_blank["\'] style=["\']color:#1a73e8;["\']>'
        content = re.sub(leak_pattern, dom, content, flags=re.I)
        
        # Doubled link tags: <a ...>dom</a><a ...>dom</a>
        content = re.sub(r'<a[^>]*>' + dom + r'</a>\s*<a[^>]*>' + dom + r'</a>', f'<a href="https://{dom}" target="_blank" class="text-link">{dom}</a>', content, flags=re.I)

    # General cleanup
    content = re.sub(r'</a>\s*</a>', '</a>', content)
    content = re.sub(r'</a>\s*</strong>\s*</a>', '</strong></a>', content)
    
    # Fix the specific docs.google.com case in line 42 of modern_docs
    content = content.replace('docs.google.com" target="_blank" style="color:#1a73e8;">', 'docs.google.com')

    return content

def process():
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                path = os.path.join(root, f)
                print(f"Final Clean V2 {path}...")
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                fixed = final_global_clean(content)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(fixed)

if __name__ == "__main__":
    process()
