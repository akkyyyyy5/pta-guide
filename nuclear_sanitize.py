import os
import re

lineworks_target = "https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2"

def nuclear_sanitize(content, filename):
    # 1. Strip ALL <a> tags with class="text-link"
    # We do this in a loop to handle nested cases (though we shouldn't have them anymore)
    while True:
        original = content
        content = re.sub(r'<a[^>]+class="text-link"[^>]*>(.*?)</a>', r'\1', content, flags=re.IGNORECASE | re.DOTALL)
        if content == original:
            break
            
    # 2. Strip stray </a> tags that might have been left over from previous broken regex
    # These are usually at the end of a line like "</a></a>"
    # We'll compare <a and </a> counts later, but first let's clean known bad patterns
    content = re.sub(r'</a></a>', '</a>', content)
    content = re.sub(r'/" target="_blank" style="color:#1a73e8;">', '', content)
    content = re.sub(r'target="_blank" style="color:#1a73e8;">', '', content)
    
    # 3. Clean Title tags
    def clean_title(m):
        inner = m.group(1)
        cleaned = re.sub(r'<[^>]+>', '', inner)
        return f'<title>{cleaned}</title>'
    content = re.sub(r'<title>(.*?)</title>', clean_title, content, flags=re.IGNORECASE | re.DOTALL)

    # 4. Remove all remaining <a> tags inside <title> if any
    # This acts as a second layer of defense
    
    # 5. Re-apply links SAFELY
    exclude_parents = ['title', 'h1', 'h2', 'h3', 'nav', 'header', 'footer', 'script', 'style', 'a', 'button']
    
    parts = re.split(r'(<[^>]+>)', content)
    new_parts = []
    tag_stack = []
    
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
                    # Correct LINE WORKS link in hrefs
                    if tag_name == 'a' and ('line.worksmobile.com' in part or 'worksmobile.com' in part):
                        part = re.sub(r'href="[^"]+"', f'href="{lineworks_target}"', part)
            new_parts.append(part)
        else:
            in_exclude = any(t in exclude_parents for t in tag_stack)
            if not in_exclude and part.strip():
                # Apply patterns
                for regex, url in patterns:
                    # Avoid over-linking if it already looks like a link text in a text node
                    # But the text node here should NOT be inside an <a> because we stripped ours
                    # and we skip in_exclude anyway.
                    part = re.sub(regex, f'<a href="{url}" target="_blank" class="text-link">\\g<0></a>', part)
                # LINE WORKS
                part = re.sub(r'\bLINE WORKS\b', f'<a href="{lineworks_target}" target="_blank" class="text-link">LINE WORKS</a>', part)
            new_parts.append(part)

    # FINAL CHECK: if there are more </a> than <a, strip from end
    # This is a bit risky but we are in a nuclear mode
    # Let's just do it for text nodes? No.
    
    return "".join(new_parts)

def process_all():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                print(f"Cleaning {filepath}...")
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = nuclear_sanitize(content, file)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    process_all()
