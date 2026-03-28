"""
build_quick.py
簡易版ガイド（quick.html）をビルド
= フォーム簡易版 + body_p3（Docs/Drive） + body_p4（LW/Sheets/Meet）
各セクション末尾に「詳細版ガイドを見る」リンクを注入
"""
import os, re

base = r'f:\Antigravity\ニュースを自動で収集\pta-guide'

def r(name):
    with open(os.path.join(base, name), encoding='utf-8') as f:
        return f.read()

CSS = r('_css.txt')

# パーツ読み込み
forms_quick = r('forms_quick_body.html')
docs_drive  = r('body_p3.html')   # Docs + Drive
lw_sh_meet  = r('body_p4.html')   # LINE WORKS + Sheets + Meet + 完了バナー + footer

# 各セクション末尾(</section>の直前)に「詳細版を見る」リンクを追加
def add_detail_link(html, section_id, url, color, label):
    """section_idに該当するsectionの末尾に詳細リンクを追加"""
    link_html = (
        f'<div style="margin-top:16px;text-align:center;">'
        f'<a href="{url}" style="display:inline-block;background:{color};color:white;'
        f'text-decoration:none;border-radius:8px;padding:12px 28px;font-size:14px;font-weight:700;">'
        f'&#128214; {label}</a></div>\n'
    )
    # sectionの</div>\n</section>の直前に挿入
    target = f'id="{section_id}"'
    if target in html:
        # そのsectionの最後の</div>\n</section>を探してリンクを追加
        parts = html.split(target, 1)
        before = parts[0]
        after = parts[1]
        # afterの中で最初の</section>を探す
        sec_end = after.find('</section>')
        if sec_end >= 0:
            # </section>の直前の</div>の直前に追加
            last_div = after.rfind('</div>', 0, sec_end)
            if last_div >= 0:
                after = after[:last_div] + link_html + after[last_div:]
        html = before + target + after
    return html

# Docs・Drive にリンク追加
docs_drive = add_detail_link(docs_drive, 'step-docs', 'docs.html', '#1565c0', '\u8a73\u7d30\u7248\u30ac\u30a4\u30c9\u3092\u898b\u308b \u2192')
docs_drive = add_detail_link(docs_drive, 'step-drive', 'drive.html', '#137333', '\u8a73\u7d30\u7248\u30ac\u30a4\u30c9\u3092\u898b\u308b \u2192')

# LINE WORKS・Sheets・Meet にリンク追加
lw_sh_meet = add_detail_link(lw_sh_meet, 'step-lineworks', 'lineworks.html', '#00a800', '\u8a73\u7d30\u7248\u30ac\u30a4\u30c9\u3092\u898b\u308b \u2192')
lw_sh_meet = add_detail_link(lw_sh_meet, 'step-sheets', 'sheets.html', '#43a047', '\u8a73\u7d30\u7248\u30ac\u30a4\u30c9\u3092\u898b\u308b \u2192')
lw_sh_meet = add_detail_link(lw_sh_meet, 'step-meet', 'meet.html', '#039be5', '\u8a73\u7d30\u7248\u30ac\u30a4\u30c9\u3092\u898b\u308b \u2192')

# Canva・調整さん にリンク追加
lw_sh_meet = add_detail_link(lw_sh_meet, 'step-canva', 'canva.html', '#7d2ae8', '\u8a73\u7d30\u7248\u30ac\u30a4\u30c9\u3092\u898b\u308b \u2192')
lw_sh_meet = add_detail_link(lw_sh_meet, 'step-chouseisan', 'chouseisan.html', '#00897b', '\u8a73\u7d30\u7248\u30ac\u30a4\u30c9\u3092\u898b\u308b \u2192')

# ナビ
nav = (
    '<nav class="toc"><div class="toc-inner">'
    '<a href="index.html" style="color:#9e9e9e;">\u2190 \u30db\u30fc\u30e0</a>'
    '<a href="#step-forms" style="color:#5E35B1;">&#128203; \u30d5\u30a9\u30fc\u30e0</a>'
    '<a href="#step-docs">&#128221; \u30c9\u30ad\u30e5\u30e1\u30f3\u30c8</a>'
    '<a href="#step-drive">&#128193; \u30c9\u30e9\u30a4\u30d6</a>'
    '<a href="#step-lineworks">&#128172; LINE WORKS</a>'
    '<a href="#step-sheets">&#128202; \u30b7\u30fc\u30c8</a>'
    '<a href="#step-meet">&#128249; Meet</a>'
    '<a href="#step-canva">&#127912; Canva</a>'
    '<a href="#step-chouseisan">&#128197; \u8abf\u6574\u3055\u3093</a>'
    '</div></nav>'
)

# ヒーロー
hero = (
    '<header class="hero">'
    '<div class="hero-inner">'
    '<div class="hero-badge">PTA \u30c7\u30b8\u30bf\u30eb\u63a8\u9032\u30ac\u30a4\u30c9 2026</div>'
    '<h1>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb<br><span>\u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9</span></h1>'
    '<p class="hero-sub">\u53b3\u9078\u3055\u308c\u305f\u30c4\u30fc\u30eb\u306e\u64cd\u4f5c\u65b9\u6cd5\u3092\u30d1\u30c3\u3068\u78ba\u8a8d\u3002<br>'
    '<strong>\u3059\u3079\u3066\u306e\u30c4\u30fc\u30eb\u304c PTA \u306a\u3089\u7121\u6599\u3067\u5229\u7528\u53ef\u80fd\u3067\u3059\u3002</strong></p>'
    '<div class="hero-chips">'
    '<span class="chip">\u2705 \u30b9\u30de\u30db\u5bfe\u5fdc</span>'
    '<span class="chip">\u2705 \u7121\u6599\u3067\u4f7f\u3048\u308b</span>'
    '<span class="chip">\u2705 \u64cd\u4f5c\u753b\u9762\u4ed8\u304d</span>'
    '</div></div></header>'
    '<main style="max-width:900px;margin:0 auto;padding:48px 20px;">'
)

# JavaScript
js = (
    '<script defer>'
    'const sections=document.querySelectorAll(".step-section");'
    'const navLinks=document.querySelectorAll(".toc a");'
    'const observer=new IntersectionObserver((entries)=>{'
    'entries.forEach(entry=>{'
    'if(entry.isIntersecting){'
    'navLinks.forEach(l=>{l.style.color="";l.style.borderBottomColor="transparent";});'
    'const id=entry.target.id;'
    'const link=document.querySelector(`.toc a[href="#${id}"]`);'
    'if(link){link.style.color="#5E35B1";link.style.borderBottomColor="#5E35B1";}'
    '}});},{threshold:0.3});'
    'sections.forEach(s=>observer.observe(s));'
    '</script>'
)

# 本文組み立て
google_header = '<div style="font-size:18px;font-weight:900;color:#5E35B1;margin:0 0 24px;border-bottom:2px solid #D1C4E9;padding-bottom:8px;">🔷 Google の便利なツール（すべて無料）</div>'
chat_header = '<div style="font-size:18px;font-weight:900;color:#00a800;margin:40px 0 24px;border-bottom:2px solid #e8f5e9;padding-bottom:8px;">💬 役員間の連絡ツール（別サービス）</div>'
other_header = '<div style="font-size:18px;font-weight:900;color:#7d2ae8;margin:40px 0 24px;border-bottom:2px solid #f3e5f5;padding-bottom:8px;">🎨 制作・調整ツール（外部サービス）</div>'

# body_p4.html の中身から LINE WORKS セクションを抽出して分離する必要があるか
# 面倒なので body_p4.html 側で調整するか、ここで split する
lw_split = lw_sh_meet.split('<section class="step-section" id="step-sheets">')
lw_part = lw_split[0]
sh_meet_plus = '<section class="step-section" id="step-sheets">' + lw_split[1]

# さらに Canva 以降を分離
plus_split = sh_meet_plus.split('<section class="step-section" id="step-canva">')
sh_meet_part = plus_split[0]
canva_chousei_raw = '<section class="step-section" id="step-canva">' + plus_split[1]

# canva_chousei_raw から完了バナー以降（finish-banner + </main> + footer）を分離
# body_p4.html末尾に含まれる完了バナー〜フッターを切り離す
finish_idx = canva_chousei_raw.find('<div class="finish-banner">')
if finish_idx >= 0:
    canva_chousei_part = canva_chousei_raw[:finish_idx]
    finish_footer_part = canva_chousei_raw[finish_idx:]
else:
    canva_chousei_part = canva_chousei_raw
    finish_footer_part = ''

body = (
    google_header
    + forms_quick
    + '\n<hr class="divider">\n'
    + docs_drive
    + '\n<hr class="divider">\n'
    + sh_meet_part
    + other_header
    + canva_chousei_part
    + '\n'
    + chat_header
    + lw_part
    + finish_footer_part
)

html = (
    '<!DOCTYPE html>\n<html lang="ja">\n<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
    '<title>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9\uff08\u7c21\u6613\u7248\uff09 | PTA\u30c7\u30b8\u30bf\u30eb\u63a8\u9032</title>\n'
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">\n'
    + CSS + '\n</head>\n<body>\n'
    + nav + '\n'
    + hero + '\n'
    + body + '\n'
    + js + '\n</body>\n</html>'
)

out = os.path.join(base, 'quick.html')
with open(out, 'wb') as f:
    f.write(b'\xef\xbb\xbf')
    f.write(html.encode('utf-8'))
print(f'Built quick.html: {len(html)} chars')
