import os
import re

lineworks_target = "https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2"

def master_repair(content, filename):
    # 1. First, strip EVERY SINGLE <a> tag in the file to reset state
    # BUT we want to keep the navigation! 
    # So we only strip inside the <main> tag or outside the <nav> block.
    
    parts = re.split(r'(<nav.*?</nav>|<header.*?</header>|<footer>.*?</footer>|<script.*?</script>)', content, flags=re.IGNORECASE | re.DOTALL)
    new_parts = []
    
    for part in parts:
        if re.match(r'<(nav|header|footer|script)', part, re.I):
            # Protected areas: keep exactly as is
            new_parts.append(part)
        else:
            # Main content or Body files: STRIP ALL <a> TAGS and broken artifacts
            p = part
            p = re.sub(r'</?a[^>]*>', '', p, flags=re.I)
            p = re.sub(r'/" target="_blank" style="color:#1a73e8;">', '', p)
            p = re.sub(r'target="_blank" style="color:#1a73e8;">', '', p)
            p = re.sub(r'>chouseisan\.com>', 'chouseisan.com', p)
            p = re.sub(r'chouseisan\.com>', 'chouseisan.com', p)
            p = re.sub(r'canva\.com>', 'canva.com', p)
            p = re.sub(r'>>', '>', p) # Correct double close tags
            
            # Re-apply links SAFELY
            # Split by tags to avoid linkifying tag attributes
            sub_parts = re.split(r'(<[^>]+>)', p)
            processed_sub = []
            tag_stack = []
            exclude_tags = ['title', 'h1', 'h2', 'h3', 'a', 'strong', 'button']
            
            patterns = [
                (r'\bforms\.google\.com\b', 'https://forms.google.com'),
                (r'\bdocs\.google\.com\b', 'https://docs.google.com'),
                (r'\bdrive\.google\.com\b', 'https://drive.google.com'),
                (r'\bmeet\.google\.com\b', 'https://meet.google.com'),
                (r'\bcanva\.com\b', 'https://canva.com'),
                (r'\bchouseisan\.com\b', 'https://chouseisan.com'),
            ]

            for sp in sub_parts:
                if sp.startswith('<'):
                    tag_match = re.match(r'<(/?)(\w+)', sp)
                    if tag_match:
                        is_end = tag_match.group(1) == '/'
                        tag_name = tag_match.group(2).lower()
                        if is_end:
                            if tag_stack and tag_stack[-1] == tag_name: tag_stack.pop()
                        else:
                            tag_stack.append(tag_name)
                    processed_sub.append(sp)
                else:
                    in_exclude = any(t in exclude_tags for t in tag_stack)
                    if not in_exclude and sp.strip():
                        for regex, url in patterns:
                            sp = re.sub(regex, f'<a href="{url}" target="_blank" class="text-link">\\g<0></a>', sp)
                        sp = re.sub(r'\bLINE WORKS\b', f'<a href="{lineworks_target}" target="_blank" class="text-link">LINE WORKS</a>', sp)
                    processed_sub.append(sp)
            new_parts.append("".join(processed_sub))
            
    final_content = "".join(new_parts)
    
    # Final cleanup of any potential stray tags in Title (outside our split areas)
    final_content = re.sub(r'<title>(.*?)</title>', lambda m: f'<title>{re.sub("<[^>]+>", "", m.group(1))}</title>', final_content, flags=re.IGNORECASE | re.DOTALL)
    
    return final_content

def process_all():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                print(f"Master Repair {filepath}...")
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = master_repair(content, file)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    process_all()
