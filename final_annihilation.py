import os
import re

def annihilation(content):
    # 1. Any string followed by " target="_blank" style="color:#1a73e8;">
    # This matches cases like: docs.google.com" target="_blank" style="color:#1a73e8;">
    # Or even just " target="_blank" style="color:#1a73e8;">
    content = re.sub(r'["\']?\s*target=["\']_blank["\']\s*style=["\']color:#1a73e8;["\?]>', '', content)
    
    # 2. Specific for calendar.google.com leak
    content = content.replace('style="color:#1a73e8;"><strong>calendar.google.com</strong>', '<strong><a href="https://calendar.google.com" target="_blank" class="text-link">calendar.google.com</a></strong>')
    
    # 3. Specific for line.worksmobile.com leak
    content = content.replace('style="color:#1a73e8;">line.worksmobile.com</a>', '<a href="https://line.worksmobile.com" target="_blank" class="text-link">line.worksmobile.com</a>')

    # 4. Cleanup line works redundant URLs
    content = content.replace('https://line.worksmobile.com', 'https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2')

    return content

def process():
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.html'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                fixed = annihilation(content)
                if fixed != content:
                    print(f"Annihilated: {path}")
                    with open(path, 'w', encoding='utf-8') as file:
                        file.write(fixed)

if __name__ == "__main__":
    process()
