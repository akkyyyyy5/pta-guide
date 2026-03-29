import os
import glob

# 対象ファイル
target_files = glob.glob('*_body.html')
target_files.append('add_npo_plan.py')

replacements = [
    ("大容量がずっと無料で", "大容量が無料で"),
    ("PTAの役員会規模ならずっと無料で", "PTAの会議規模なら無料で"),
    ("PTA役員担当者", "PTAのIT担当者"),
    ("10月役員会", "10月定例会"),
    ("第3回 役員会", "第3回 ミーティング"),
    ("役員会", "会議"),
    ("役員名簿", "メンバー名簿"),
    ("役員", "メンバー"),
]

for file_path in target_files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
        
print("All replacements done.")
