import os
import re

def ultimate_cleanup(content):
    # 1. Convert style attributes to class
    content = content.replace('style="color:#1a73e8;"', 'class="text-link"')
    
    # 2. Fix double link closures
    content = re.sub(r'</a>\s*</a>', '</a>', content)
    
    # 3. Fix double strong/bold tags
    content = re.sub(r'<strong>\s*<strong>', '<strong>', content)
    content = re.sub(r'</strong>\s*</strong>', '</strong>', content)
    
    # 4. Fix doubled URL patterns: <a...>url</a>url
    # or url<a...>url</a>
    # (Common if my previous script was too aggressive)
    # We'll just leave them for now unless they are very obvious.
    
    # 5. Fix the "target=..." leak if any remained
    content = re.sub(r'["\']?\s*target=["\']_blank["\']\s*class=["\']text-link["\']\s*>', '>', content)

    # 6. Specific fix for double link text like docs.google.comdocs.google.com
    for dom in ["docs.google.com", "drive.google.com", "forms.google.com", "meet.google.com", "sheets.google.com", "canva.com", "chouseisan.com"]:
        content = content.replace(f'{dom}{dom}', dom)

    return content

def ultra_clean(content):
    import re
    # 属性がテキストとして露出している場合のパターン (e.g. " target="_blank" style="color:#1a73e8;">)
    # <a>タグの外にあることを想定
    content = re.sub(r'["\']?\s*target=["\']_blank["\']\s*style=["\'][^"\']*["\']?>', '', content)
    # 二重リンクの残骸を掃除
    content = re.sub(r'</a>\s*<a[^>]*>', ' ', content)
    # 重複するhrefの残骸を掃除
    content = re.sub(r'href=["\']https?://[^"\']+["\']" target=["\']_blank["\']', 'target="_blank"', content)
    return content

def cleanup_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = ultra_clean(content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Ulti-Cleaned: {path}")

def process():
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                fixed = ultimate_cleanup(content)
                if fixed != content:
                    print(f"Ulti-Cleaned: {path}")
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(fixed)

if __name__ == "__main__":
    process()
