import os
import re

lineworks_target = "https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2"

def total_balance_fix(content, filename):
    # 1. Strip ALL our generated links and their broken traces
    content = re.sub(r'<a[^>]+class="text-link"[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'</a>', '<<TAG_CLOSE>>', content) # Temp marker
    
    # Remove ALL our text-link close tags? No, how to identify them?
    # Actually, let's just strip ALL <a> and </a> tags that are not in nav/header/footer
    # This is safer:
    
    parts = re.split(r'(<[^>]+>)', content)
    new_parts = []
    tag_stack = []
    
    # We'll use a stack to identify if we are inside a protected area
    protected_areas = ['title', 'nav', 'header', 'footer', 'script', 'style', 'button']
    
    for part in parts:
        if part.startswith('<'):
            tag_match = re.match(r'<(/?)(\w+)', part)
            if tag_match:
                is_end = tag_match.group(1) == '/'
                tag_name = tag_match.group(2).lower()
                
                in_protected = any(p in protected_areas for p in tag_stack)
                
                if tag_name == 'a':
                    if in_protected:
                        # Keep original nav/link tags
                        new_parts.append(part)
                    else:
                        # Strip accidental links in content
                        pass
                else:
                    new_parts.append(part)
                
                if is_end:
                    if tag_stack and tag_stack[-1] == tag_name:
                        tag_stack.pop()
                else:
                    tag_stack.append(tag_name)
        else:
            new_parts.append(part)
            
    content = "".join(new_parts)
    
    # 2. Re-clean leakage artifacts
    content = re.sub(r'/" target="_blank" style="color:#1a73e8;">', '', content)
    content = re.sub(r'target="_blank" style="color:#1a73e8;">', '', content)
    
    # 3. Clean Title tags again (double safety)
    content = re.sub(r'<title>(.*?)</title>', lambda m: f'<title>{re.sub("<[^>]+>", "", m.group(1))}</title>', content, flags=re.IGNORECASE | re.DOTALL)

    # 4. Re-apply links SAFELY
    exclude_parents = ['title', 'h1', 'h2', 'h3', 'nav', 'header', 'footer', 'script', 'style', 'a', 'button', 'strong'] # Added strong to avoid double nested
    
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
                    if tag_name == 'a' and ('line.worksmobile.com' in part or 'worksmobile.com' in part):
                        part = re.sub(r'href="[^"]+"', f'href="{lineworks_target}"', part)
            new_parts.append(part)
        else:
            in_exclude = any(t in exclude_parents for t in tag_stack)
            if not in_exclude and part.strip():
                for regex, url in patterns:
                    part = re.sub(regex, f'<a href="{url}" target="_blank" class="text-link">\\g<0></a>', part)
                part = re.sub(r'\bLINE WORKS\b', f'<a href="{lineworks_target}" target="_blank" class="text-link">LINE WORKS</a>', part)
            new_parts.append(part)

    return "".join(new_parts)

def process_all():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                print(f"Final Fix {filepath}...")
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = total_balance_fix(content, file)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    process_all()
