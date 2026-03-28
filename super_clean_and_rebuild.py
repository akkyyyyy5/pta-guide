import os
import re

lineworks_target = "https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2"

def sanitize_content(content, filename):
    # 1. First, strip ALL existing <a> tags that I likely created (class="text-link")
    # This prevents nesting and fixes the broken trailing tags
    # We use a non-greedy match to find the end of the <a> tag and its matching </a>
    content = re.sub(r'<a[^>]+class="text-link"[^>]*>(.*?)</a>', r'\1', content, flags=re.IGNORECASE | re.DOTALL)
    
    # 2. Fix the specific leakage artifacts like /" target="_blank" style="color:#1a73e8;">
    content = re.sub(r'/" target="_blank" style="color:#1a73e8;">', '', content)
    content = re.sub(r'target="_blank" style="color:#1a73e8;">', '', content)
    
    # 3. Clean up Title tags (remove any accidental tags inside <title>)
    def clean_title(m):
        inner = m.group(1)
        cleaned = re.sub(r'<[^>]+>', '', inner) # Strip all tags inside title
        return f'<title>{cleaned}</title>'
    
    content = re.sub(r'<title>(.*?)</title>', clean_title, content, flags=re.IGNORECASE | re.DOTALL)

    # 4. Remove problematic inline styles in Modern files
    if 'modern_' in filename:
        # Remove background/color overrides that make it hard to read in dark mode
        content = re.sub(r'style="background:#e8f5e9;border-left:4px solid #00a800;margin-bottom:32px;"', '', content)
        content = re.sub(r'style="background:#e0f2f1;border-left:4px solid #00897b;margin-bottom:32px;"', '', content)
        content = re.sub(r'style="background:#f3e5f5;border-left:4px solid #5E35B1;margin-bottom:32px;"', '', content)
        content = re.sub(r'style="color:#00a800;"', '', content)
        content = re.sub(r'style="color:#00897b;"', '', content)
        content = re.sub(r'style="color:#5E35B1;"', '', content)

    # 5. Re-apply links SAFELY
    # Only in text nodes, avoiding certain parent tags
    exclude_parents = ['title', 'h1', 'h2', 'h3', 'nav', 'header', 'footer', 'script', 'style', 'a', 'button']
    
    parts = re.split(r'(<[^>]+>)', content)
    new_parts = []
    tag_stack = []
    
    # Patterns to linkify
    patterns = [
        (r'\bforms\.google\.com\b', 'https://forms.google.com'),
        (r'\bdocs\.google\.com\b', 'https://docs.google.com'),
        (r'\bdrive\.google\.com\b', 'https://drive.google.com'),
        (r'\bmeet\.google\.com\b', 'https://meet.google.com'),
        (r'\bcanva\.com\b', 'https://canva.com'),
        (r'\bchouseisan\.com\b', 'https://chouseisan.com'),
    ]

    for part in parts:
        if part.startswith('<'):
            tag_match = re.match(r'<(/?)(\w+)', part)
            if tag_match:
                is_end = tag_match.group(1) == '/'
                tag_name = tag_match.group(2).lower()
                if is_end:
                    if tag_stack and tag_stack[-1] == tag_name:
                        tag_stack.pop()
                else:
                    tag_stack.append(tag_name)
                    # Special Case: LINE WORKS campaign URL replacement in <a> hrefs
                    if tag_name == 'a' and ('line.worksmobile.com' in part or 'worksmobile.com' in part):
                        part = re.sub(r'href="[^"]+"', f'href="{lineworks_target}"', part)
            new_parts.append(part)
        else:
            # This is a text node
            in_exclude = any(t in exclude_parents for t in tag_stack)
            if not in_exclude and part.strip():
                # Apply patterns
                for regex, url in patterns:
                    part = re.sub(regex, f'<a href="{url}" target="_blank" class="text-link">\\g<0></a>', part)
                # Linkify "LINE WORKS" text specifically to campaign URL if not already in <a>
                part = re.sub(r'\bLINE WORKS\b', f'<a href="{lineworks_target}" target="_blank" class="text-link">LINE WORKS</a>', part)
            new_parts.append(part)

    return "".join(new_parts)

def process_all():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                print(f"Processing {filepath}...")
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = sanitize_content(content, file)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    process_all()
