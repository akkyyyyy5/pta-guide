# -*- coding: utf-8 -*-
"""
HTMLファイルの文字化け修正スクリプト

現状: BOM付きUTF-8で保存されているが、一部のコンテンツが
      「CP932として読んでUTF-8で書き直した」形式で文字化けしている。
      
修正: 文字化けしているセクションを正しいUTF-8に変換する。
"""

filepath = r'f:\Antigravity\ニュースを自動で収集\pta-guide\index.html'

with open(filepath, 'rb') as f:
    raw = f.read()

# BOMを取り除いてUTF-8として読み込み
if raw[:3] == b'\xef\xbb\xbf':
    content = raw[3:].decode('utf-8', errors='replace')
else:
    content = raw.decode('utf-8', errors='replace')

print(f"Total length: {len(content)}")

# 文字化けのパターン確認:「繝輔ぃ」が「ファイル」の文字化けなら
# これはUTF-8バイト列をCP932で読んで人間が見ている状態
# 実際のファイルバイトはUTF-8なので、正しくデコードできているはず

# まずタイトルを確認
title_start = content.find('<title>')
title_end = content.find('</title>')
print(f"Title: {content[title_start:title_end+8]}")

# 問題のある部分を探す：文字化けパターンの典型例
if '繝輔ぃ' in content:
    print("MOJIBAKE DETECTED in content!")
    idx = content.find('繝輔ぃ')
    print(f"Context: ...{content[max(0,idx-20):idx+30]}...")
    
    # 修正方法：UTF-8として読んだ文字列をCP932でencode→UTF-8でdecode
    # これは「CP932で解釈されてUTF-8に再エンコードされた」テキストを元に戻す操作
    try:
        fixed_sample = content[max(0,idx-5):idx+15].encode('cp932').decode('utf-8')
        print(f"Fixed sample: {fixed_sample}")
        print("Fix method: encode(cp932) -> decode(utf-8)")
    except Exception as e:
        print(f"Fix failed: {e}")
else:
    print("No mojibake pattern found in decoded content")
    print("The file should display correctly in browser")
    print(f"\nSample (1000-2000): {content[1000:1500]}")

# タグ直後のコンテンツを確認
google_idx = content.find('Google')
print(f"\nFirst 'Google' at position {google_idx}")
if google_idx >= 0:
    print(f"Context: {content[google_idx:google_idx+50]}")
