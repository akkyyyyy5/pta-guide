import os
import re

directory = r'f:\Antigravity\ニュースを自動で収集\pta-guide'
file_count = 0
changed_files = 0

# Matches <a href="https://SOME_DOMAIN>...</a>
# Note: we only match if it misses the closing quote. Assumes no spaces in the URL.
pattern = re.compile(r'<a\s+href="([^">]+)>(.*?)</a>')

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content, num_subs = pattern.subn(r'<a href="\1" target="_blank" class="text-link">\2</a>', content)
        
        if num_subs > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            changed_files += 1
            print(f"Fixed {num_subs} broken links in {filename}")
        
print(f"Total HTML files processed: {len([f for f in os.listdir(directory) if f.endswith('.html')])}")
print(f"Total files updated: {changed_files}")
