import os
import re

# Correct LINE WORKS Campaign URL
lineworks_target = "https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2"

def clean_and_relinquish(content):
    # 1. Strip ALL <a> and </a> tags that were automatically generated or were broken
    # We strip any <a> tag that has "text-link" class or is just broken.
    content = re.sub(r'<a[^>]*class="text-link"[^>]*>', '', content, flags=re.I)
    content = re.sub(r'</a>', '', content, flags=re.I)
    
    # 2. Fix the "chouseisan.com>" and similar artifacts
    content = content.replace('chouseisan.com>', 'chouseisan.com')
    content = content.replace('canva.com>', 'canva.com')
    content = content.replace('www.canva.com>', 'www.canva.com')
    # Remove fragments of previous broken tags
    content = re.sub(r'/" target="_blank" style="color:#1a73e8;">', '', content)
    content = re.sub(r'target="_blank" style="color:#1a73e8;">', '', content)
    content = re.sub(r'<strongchouseisan\.com', '<strong>chouseisan.com', content)
    
    # 3. Handle specific navigation breakage (if index/modern/kawaii were broken)
    content = re.sub(r'← 戻る>', '← 戻る</a>', content)
    content = re.sub(r'📋 フォーム>', '📋 フォーム</a>', content)
    content = re.sub(r'📝 ドキュメント>', '📝 ドキュメント</a>', content)
    content = re.sub(r'📁 ドライブ>', '📁 ドライブ</a>', content)
    content = re.sub(r'💬 LINE WORKS>', '💬 LINE WORKS</a>', content)
    content = re.sub(r'📊 シート>', '📊 シート</a>', content)
    content = re.sub(r'📹 Meet>', '📹 Meet</a>', content)
    content = re.sub(r'🎨 Canva>', '🎨 Canva</a>', content)
    content = re.sub(r'📅 調整さん>', '📅 調整さん</a>', content)

    # 4. Safe Re-linkification
    def linkify(text):
        # Tools to linkify
        patterns = [
            (r'chouseisan\.com', 'https://chouseisan.com'),
            (r'canva\.com', 'https://canva.com'),
            (r'forms\.google\.com', 'https://forms.google.com'),
            (r'docs\.google\.com', 'https://docs.google.com'),
            (r'drive\.google\.com', 'https://drive.google.com'),
            (r'meet\.google\.com', 'https://meet.google.com'),
        ]
        res = text
        for pat, url in patterns:
            res = re.sub(r'\b' + pat + r'\b', f'<a href="{url}" target="_blank" class="text-link">{pat}</a>', res)
        # LINE WORKS
        res = re.sub(r'\bLINE WORKS\b', f'<a href="{lineworks_target}" target="_blank" class="text-link">LINE WORKS</a>', res)
        return res

    # Use a split-and-map to avoid attribute linkification
    parts = re.split(r'(<[^>]+>)', content)
    new_parts = []
    tag_stack = []
    exclude_tags = ['title', 'h1', 'h2', 'h3', 'a', 'nav', 'header', 'footer', 'script', 'style', 'button']
    
    for p in parts:
        if p.startswith('<'):
            tag_match = re.match(r'<(/?)(\w+)', p)
            if tag_match:
                tag_name = tag_match.group(2).lower()
                is_end = tag_match.group(1) == '/'
                if is_end:
                    if tag_stack and tag_stack[-1] == tag_name: tag_stack.pop()
                else: tag_stack.append(tag_name)
                # Correct campaign URL in existing manual links
                if tag_name == 'a' and ('line.worksmobile.com' in p or 'worksmobile.com' in p):
                    p = re.sub(r'href="[^"]+"', f'href="{lineworks_target}"', p)
            new_parts.append(p)
        else:
            in_exclude = any(t in exclude_tags for t in tag_stack)
            if not in_exclude and p.strip():
                new_parts.append(linkify(p))
            else:
                new_parts.append(p)
                
    return "".join(new_parts)

def process():
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                path = os.path.join(root, f)
                print(f"Fixing {path}...")
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                fixed = clean_and_relinquish(content)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(fixed)

if __name__ == "__main__":
    process()
