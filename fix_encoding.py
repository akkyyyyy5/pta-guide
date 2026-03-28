# -*- coding: utf-8 -*-
"""
HTMLファイルの文字化け修正スクリプト（本番）

原因: UTF-8バイト列をCP932(Shift-JIS)として読み込み、
      UTF-8で書き直した結果の二重エンコード
修正: encode('cp932') -> decode('utf-8') で元に戻す
"""

filepath = r'f:\Antigravity\ニュースを自動で収集\pta-guide\index.html'

with open(filepath, 'rb') as f:
    raw = f.read()

# BOM付きUTF-8として読み込み
if raw[:3] == b'\xef\xbb\xbf':
    garbled = raw[3:].decode('utf-8', errors='replace')
else:
    garbled = raw.decode('utf-8', errors='replace')

# 修正: encode(cp932) -> decode(utf-8) でオリジナルのUTF-8に戻す
# errors='ignore'でCP932に変換できない文字(主にHTML属性のASCII)はそのまま維持
fixed = garbled.encode('cp932', errors='ignore').decode('utf-8', errors='replace')

print(f"Original garbled length: {len(garbled)}")
print(f"Fixed length: {len(fixed)}")

# タイトルを確認
t_start = fixed.find('<title>')
t_end = fixed.find('</title>')
print(f"Title after fix: {fixed[t_start:t_end+8]}")

# 追加: step-lineworks セクションのh2タグを確認
lw_idx = fixed.find('step-lineworks')
if lw_idx >= 0:
    print(f"LINE WORKS section found at: {lw_idx}")
    print(f"Context: {fixed[lw_idx:lw_idx+100]}")
else:
    print("LINE WORKS section NOT found - may need to re-add sections")

# BOM付きUTF-8で書き出す
with open(filepath, 'wb') as f:
    f.write(b'\xef\xbb\xbf')
    f.write(fixed.encode('utf-8'))

print("\nFile saved successfully!")
