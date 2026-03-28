import os
import re

def final_global_clean(content):
    # 1. Fix the specific leak pattern: [domain]" target="_blank" style="color:#1a73e8;"><a ...>[domain]</a></a>
    # We replace the whole mess with a clean link.
    
    # Patterns for tool domains
    domains = ["docs.google.com", "drive.google.com", "forms.google.com", "meet.google.com", "canva.com", "chouseisan.com", "www.canva.com"]
    
    for dom in domains:
        # Doubled link pattern with garbage
        bad_pattern = dom + r'["\'] target=["\']_blank["\'] style=["\']color:#1a73e8;["\']>\s*<a[^>]*>' + dom + r'</a>\s*</a>'
        clean_replacement = f'<a href="https://{dom}" target="_blank" class="text-link">{dom}</a>'
        content = re.sub(bad_pattern, clean_replacement, content, flags=re.I)
        
        # Simple doubled link pattern: <a ...>dom</a><strong><a ...>dom</a></strong></a>
        bad_pattern_2 = r'<a[^>]*class="text-link"[^>]*>' + dom + r'</a>\s*<strong>\s*<a[^>]*>' + dom + r'</a>\s*</strong>\s*</a>'
        clean_replacement_2 = f'<a href="https://{dom}" target="_blank" class="text-link">{dom}</a>'
        content = re.sub(bad_pattern_2, clean_replacement_2, content, flags=re.I)

        # Doubled link pattern without strong: <a ...>dom</a><a ...>dom</a></a>
        bad_pattern_3 = r'<a[^>]*class="text-link"[^>]*>' + dom + r'</a>\s*<a[^>]*>' + dom + r'</a>\s*</a>'
        content = re.sub(bad_pattern_3, clean_replacement_2, content, flags=re.I)

    # 2. Fix stray </a> tags at end of lines or after strong
    content = re.sub(r'</strong>\s*</a>', '</strong>', content)
    
    # 3. Fix nav corruption (just in case)
    content = content.replace('← 戻る>', '← 戻る</a>')
    content = re.sub(r'(📋|📝|📁|💬|📊|📹|🎨|📅)\s*([^<]+)>', r'\1 \2</a>', content)
    
    # 4. Final safety: remove ANY </a> that appears right after another </a>
    content = re.sub(r'</a>\s*</a>', '</a>', content)

    return content

def process():
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                path = os.path.join(root, f)
                print(f"Final Clean {path}...")
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                fixed = final_global_clean(content)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(fixed)

if __name__ == "__main__":
    process()
