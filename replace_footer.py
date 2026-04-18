import os
import re

dir_path = r"f:\Antigravity\ニュースを自動で収集\pta-guide"
target_texts = [
    "Designed by Akiyuki Hayashi, PTA President, FY2025",
    "Designed by Akiyuki Hayashi, PTA President, FY2025"
]
replacement = "Designed by Akiyuki Hayashi, PTA President, FY2025"

changed_count = 0

for file in os.listdir(dir_path):
    if file.endswith(".html") or file.endswith(".py"):
        filepath = os.path.join(dir_path, file)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for t in target_texts:
            new_content = new_content.replace(t, replacement)
            
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            changed_count += 1
            print(f"Updated {file}")

print(f"Total files updated: {changed_count}")
