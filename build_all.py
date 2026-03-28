"""
build_all.py
全6ツールの詳細HTMLページを一括生成するビルダー
日本語コンテンツはこのファイル内にUnicode literalとして埋め込む
（Pythonファイル自体はASCII onlyなので文字化けなし）
"""
import os

base = r'f:\Antigravity\ニュースを自動で収集\pta-guide'

def read(name):
    with open(os.path.join(base, name), encoding='utf-8') as f:
        return f.read()

CSS = read('_css.txt')

def build(filename, title, color, body_html):
    """共通HTMLテンプレートでファイルを生成"""
    back = '\u30db\u30fc\u30e0\u3078\u623b\u308b'  # ホームへ戻る
    nav = (
        '<nav class="toc"><div class="toc-inner">'
        f'<a href="index.html" style="color:#9e9e9e;">\u2190 {back}</a>'
        '</div></nav>'
    )
    js = (
        '<script defer>'
        'const sections=document.querySelectorAll(".step-section");'
        'const navLinks=document.querySelectorAll(".toc a");'
        'const observer=new IntersectionObserver((entries)=>{'
        'entries.forEach(entry=>{'
        'if(entry.isIntersecting){'
        'navLinks.forEach(l=>l.style.color="");'
        'const id=entry.target.id;'
        'const link=document.querySelector(`.toc a[href="#${id}"]`);'
        'if(link){link.style.color="#5E35B1";link.style.borderBottomColor="#5E35B1";}'
        '}});},{threshold:0.3});'
        'sections.forEach(s=>observer.observe(s));'
        '</script>'
    )
    html = (
        '<!DOCTYPE html>\n<html lang="ja">\n<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
        f'<title>{title}</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">\n'
        + CSS + '\n</head>\n<body>\n'
        + nav + '\n'
        + body_html + '\n'
        + js + '\n</body>\n</html>'
    )
    out = os.path.join(base, filename)
    with open(out, 'wb') as f:
        f.write(b'\xef\xbb\xbf')
        f.write(html.encode('utf-8'))
    print(f'Built {filename}: {len(html)} chars')

# ===================================================
# forms.html
# ===================================================
forms_body = read('body_p2.html')  # フォームのステップ1-5

forms_hero = (
    '<header class="hero">'
    '<div class="hero-inner">'
    '<div class="hero-badge">PTA \u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u6d3b\u7528\u30ac\u30a4\u30c9</div>'
    '<h1>&#128203; Google\u30d5\u30a9\u30fc\u30e0<br><span>\u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9</span></h1>'
    '<p class="hero-sub">\u53c2\u52a0\u78ba\u8a8d\u30fb\u30a2\u30f3\u30b1\u30fc\u30c8\u3092\u7d19\u30bc\u30ed\u3067\u30c7\u30b8\u30bf\u30eb\u5316\u3002\u56de\u7b54\u304c\u81ea\u52d5\u3067\u96c6\u8a08\u3055\u308c\u307e\u3059\u3002</p>'
    '<div class="hero-chips">'
    '<span class="chip">\u2705 \u30b9\u30de\u30db\u5bfe\u5fdc</span>'
    '<span class="chip">\u2705 \u7121\u6599</span>'
    '<span class="chip">\u2705 \u81ea\u52d5\u96c6\u8a08</span>'
    '</div></div></header>'
    '<main style="max-width:900px;margin:0 auto;padding:48px 20px;">'
)

forms_footer = (
    '<div class="finish-banner">'
    '<div style="font-size:56px;margin-bottom:16px;">&#127881;</div>'
    '<h2>\u304a\u75b2\u308c\u3055\u307e\u3067\u3057\u305f\uff01</h2>'
    '<p>Google\u30d5\u30a9\u30fc\u30e0\u306e\u57fa\u672c\u306f\u30d0\u30c3\u30c1\u30ea\u3067\u3059\u3002<br>'
    '\u6700\u521d\u306e1\u56de\u3060\u3051\u64cd\u4f5c\u3059\u308c\u3070\u3001\u3042\u3068\u304b\u3089\u898b\u8fd4\u305b\u3070OK\u3002<br>'
    '\u30b4\u4e0d\u660e\u306a\u70b9\u306fPTA\u5f79\u54e1\u62c5\u5f53\u8005\u306b\u304a\u58f0\u304c\u3051\u304f\u3060\u3055\u3044\u3002</p>'
    '</div></main>'
    '<footer><p>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9 | PTA \u30c7\u30b8\u30bf\u30eb\u63a8\u9032\u59d4\u54e1\u4f1a</p></footer>'
)

build(
    'forms.html',
    'Google\u30d5\u30a9\u30fc\u30e0 \u6d3b\u7528\u30ac\u30a4\u30c9 | PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb',
    '#5E35B1',
    forms_hero + forms_body + forms_footer
)

# ===================================================
# docs.html
# ===================================================
docs_body = read('docs_body.html')
docs_hero = (
    '<header class="hero" style="background:linear-gradient(135deg,#1565c0 0%,#1a73e8 50%,#42a5f5 100%);">'
    '<div class="hero-inner">'
    '<div class="hero-badge">PTA \u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u6d3b\u7528\u30ac\u30a4\u30c9</div>'
    '<h1>&#128221; Google\u30c9\u30ad\u30e5\u30e1\u30f3\u30c8<br><span>\u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9</span></h1>'
    '<p class="hero-sub">\u304a\u624b\u7d19\u30fb\u8b70\u4e8b\u9332\u3092\u30aa\u30f3\u30e9\u30a4\u30f3\u3067\u4f5c\u6210\u30fb\u5171\u540c\u7de8\u96c6\u3002\u5c0f\u5ddd\u3067\u306e\u308a\u53d6\u308a\u4e0d\u8981\u3002</p>'
    '<div class="hero-chips">'
    '<span class="chip">\u2705 \u5171\u540c\u7de8\u96c6</span>'
    '<span class="chip">\u2705 \u30b3\u30e1\u30f3\u30c8\u6a5f\u80fd</span>'
    '<span class="chip">\u2705 PDF\u66f8\u304d\u51fa\u3057</span>'
    '</div></div></header>'
    '<main style="max-width:900px;margin:0 auto;padding:48px 20px;">'
)
docs_footer = (
    '<div class="finish-banner">'
    '<div style="font-size:56px;margin-bottom:16px;">&#127881;</div>'
    '<h2>\u304a\u75b2\u308c\u3055\u307e\u3067\u3057\u305f\uff01</h2>'
    '<p>Google\u30c9\u30ad\u30e5\u30e1\u30f3\u30c8\u3092\u4f7f\u3048\u3070\u3001\u304a\u624b\u7d19\u4f5c\u6210\u306e\u5f80\u5fa9\u30e1\u30fc\u30eb\u304c\u306a\u304f\u306a\u308a\u307e\u3059\u3002<br>'
    '\u305c\u3072\u6700\u521d\u306e1\u901a\u3067\u8a66\u3057\u3066\u307f\u3066\u304f\u3060\u3055\u3044\u3002</p>'
    '</div></main>'
    '<footer><p>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9 | PTA \u30c7\u30b8\u30bf\u30eb\u63a8\u9032\u59d4\u54e1\u4f1a</p></footer>'
)
build('docs.html', 'Google\u30c9\u30ad\u30e5\u30e1\u30f3\u30c8 \u6d3b\u7528\u30ac\u30a4\u30c9 | PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb', '#1565c0', docs_hero + docs_body + docs_footer)

# ===================================================
# drive.html
# ===================================================
drive_body = read('drive_body.html')
drive_hero = (
    '<header class="hero" style="background:linear-gradient(135deg,#137333 0%,#0f9d58 50%,#4caf50 100%);">'
    '<div class="hero-inner">'
    '<div class="hero-badge">PTA \u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u6d3b\u7528\u30ac\u30a4\u30c9</div>'
    '<h1>&#128193; Google\u30c9\u30e9\u30a4\u30d6<br><span>\u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9</span></h1>'
    '<p class="hero-sub">\u66f8\u985e\u30fb\u5199\u771f\u3092\u30af\u30e9\u30a6\u30c9\u3067\u4e00\u5143\u7ba1\u7406\u3002USB\u4e0d\u8981\u3001\u5f79\u54e1\u5168\u54e1\u304c\u3044\u3064\u3067\u3082\u30a2\u30af\u30bb\u30b9\u53ef\u80fd\u3002</p>'
    '<div class="hero-chips">'
    '<span class="chip">\u2705 \u30af\u30e9\u30a6\u30c9\u4fdd\u5b58</span>'
    '<span class="chip">\u2705 \u6a29\u9650\u7ba1\u7406</span>'
    '<span class="chip">\u2705 \u7121\u659915GB</span>'
    '</div></div></header>'
    '<main style="max-width:900px;margin:0 auto;padding:48px 20px;">'
)
drive_footer = (
    '<div class="finish-banner">'
    '<div style="font-size:56px;margin-bottom:16px;">&#127881;</div>'
    '<h2>\u304a\u75b2\u308c\u3055\u307e\u3067\u3057\u305f\uff01</h2>'
    '<p>Google\u30c9\u30e9\u30a4\u30d6\u3067\u3001\u5f79\u54e1\u5168\u54e1\u3067\u306e\u30d5\u30a1\u30a4\u30eb\u5171\u6709\u304c\u30b9\u30e0\u30fc\u30ba\u306b\u306a\u308a\u307e\u3059\u3002<br>'
    'USB\u30e1\u30e2\u30ea\u3084\u7d19\u3067\u306e\u53d7\u3051\u6e21\u3057\u304b\u3089\u5352\u696d\u3057\u307e\u3057\u3087\u3046\u3002</p>'
    '</div></main>'
    '<footer><p>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9 | PTA \u30c7\u30b8\u30bf\u30eb\u63a8\u9032\u59d4\u54e1\u4f1a</p></footer>'
)
build('drive.html', 'Google\u30c9\u30e9\u30a4\u30d6 \u6d3b\u7528\u30ac\u30a4\u30c9 | PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb', '#137333', drive_hero + drive_body + drive_footer)

# ===================================================
# lineworks.html
# ===================================================
lw_body = read('lw_body.html')
lw_hero = (
    '<header class="hero" style="background:linear-gradient(135deg,#00a800 0%,#00c300 50%,#4caf50 100%);">'
    '<div class="hero-inner">'
    '<div class="hero-badge">PTA \u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb\uff08\u5225\u30b5\u30fc\u30d3\u30b9\uff09</div>'
    '<h1>&#128172; LINE WORKS<br><span>\u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9</span></h1>'
    '<p class="hero-sub">PTA\u5f79\u54e1\u5c02\u7528\u30c1\u30e3\u30c3\u30c8\u3002\u30d7\u30e9\u30a4\u30d9\u30fc\u30c8LINE\u3068\u5206\u96e2\u3001\u975e\u55b6\u5229\u56e3\u4f53\u306f\u7121\u6599\u3067\u5229\u7528\u3067\u304d\u307e\u3059\u3002</p>'
    '<div class="hero-chips">'
    '<span class="chip">\u2705 \u975e\u55b6\u5229\u7121\u6599</span>'
    '<span class="chip">\u2705 \u65e2\u8aad\u78ba\u8a8d</span>'
    '<span class="chip">\u2705 \u30b0\u30eb\u30fc\u30d7\u30c8\u30fc\u30af</span>'
    '</div></div></header>'
    '<main style="max-width:900px;margin:0 auto;padding:48px 20px;">'
)
lw_footer = (
    '<div class="finish-banner">'
    '<div style="font-size:56px;margin-bottom:16px;">&#127881;</div>'
    '<h2>\u304a\u75b2\u308c\u3055\u307e\u3067\u3057\u305f\uff01</h2>'
    '<p>LINE WORKS\u3067\u3001\u5f79\u54e1\u9593\u306e\u9023\u7d61\u304c\u30b9\u30c3\u30ad\u30ea\u6574\u7406\u3055\u308c\u307e\u3059\u3002<br>'
    '\u30d7\u30e9\u30a4\u30d9\u30fc\u30c8LINE\u3068\u6df7\u305c\u305a\u306b\u3059\u3080\u3053\u3068\u3067\u3001\u30b3\u30df\u30e5\u30cb\u30b1\u30fc\u30b7\u30e7\u30f3\u306e\u30b9\u30c8\u30ec\u30b9\u304c\u5927\u5e45\u306b\u6e1b\u308a\u307e\u3059\u3002</p>'
    '</div></main>'
    '<footer><p>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9 | PTA \u30c7\u30b8\u30bf\u30eb\u63a8\u9032\u59d4\u54e1\u4f1a</p></footer>'
)
build('lineworks.html', 'LINE WORKS \u6d3b\u7528\u30ac\u30a4\u30c9 | PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb', '#00a800', lw_hero + lw_body + lw_footer)

# ===================================================
# sheets.html
# ===================================================
sheets_body = read('sheets_body.html')
sheets_hero = (
    '<header class="hero" style="background:linear-gradient(135deg,#1b5e20 0%,#43a047 50%,#66bb6a 100%);">'
    '<div class="hero-inner">'
    '<div class="hero-badge">PTA \u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u6d3b\u7528\u30ac\u30a4\u30c9</div>'
    '<h1>&#128202; Google\u30b9\u30d7\u30ec\u30c3\u30c9\u30b7\u30fc\u30c8<br><span>\u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9</span></h1>'
    '<p class="hero-sub">\u540d\u7c3f\u30fb\u4f1a\u8a08\u30fb\u30a4\u30d9\u30f3\u30c8\u9032\u6357\u3092Excel\u611f\u899a\u3067\u30af\u30e9\u30a6\u30c9\u7ba1\u7406\u3002\u30d5\u30a9\u30fc\u30e0\u3068\u9023\u643a\u3067\u81ea\u52d5\u96c6\u8a08\u3002</p>'
    '<div class="hero-chips">'
    '<span class="chip">\u2705 \u540d\u7c3f\u7ba1\u7406</span>'
    '<span class="chip">\u2705 \u4f1a\u8a08\u7ba1\u7406</span>'
    '<span class="chip">\u2705 \u81ea\u52d5\u96c6\u8a08</span>'
    '</div></div></header>'
    '<main style="max-width:900px;margin:0 auto;padding:48px 20px;">'
)
sheets_footer = (
    '<div class="finish-banner">'
    '<div style="font-size:56px;margin-bottom:16px;">&#127881;</div>'
    '<h2>\u304a\u75b2\u308c\u3055\u307e\u3067\u3057\u305f\uff01</h2>'
    '<p>\u30b9\u30d7\u30ec\u30c3\u30c9\u30b7\u30fc\u30c8\u304c\u4f7f\u3044\u3053\u306a\u305b\u308c\u3070\u3001PTA\u306e\u96c6\u8a08\u4f5c\u696d\u304c\u5927\u5e45\u306b\u697d\u306b\u306a\u308a\u307e\u3059\u3002<br>'
    'Google\u30d5\u30a9\u30fc\u30e0\u3068\u9023\u643a\u3059\u308c\u3070\u3001\u56de\u7b54\u96c6\u8a08\u304c\u81ea\u52d5\u5316\u3055\u308c\u307e\u3059\u3002</p>'
    '</div></main>'
    '<footer><p>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9 | PTA \u30c7\u30b8\u30bf\u30eb\u63a8\u9032\u59d4\u54e1\u4f1a</p></footer>'
)
build('sheets.html', 'Google\u30b9\u30d7\u30ec\u30c3\u30c9\u30b7\u30fc\u30c8 \u6d3b\u7528\u30ac\u30a4\u30c9 | PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb', '#1b5e20', sheets_hero + sheets_body + sheets_footer)

# ===================================================
# meet.html
# ===================================================
meet_body = read('meet_body.html')
meet_hero = (
    '<header class="hero" style="background:linear-gradient(135deg,#0277bd 0%,#039be5 50%,#4fc3f7 100%);">'
    '<div class="hero-inner">'
    '<div class="hero-badge">PTA \u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u6d3b\u7528\u30ac\u30a4\u30c9</div>'
    '<h1>&#128249; Google Meet<br><span>\u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9</span></h1>'
    '<p class="hero-sub">\u81ea\u5b85\u304b\u3089\u5f79\u54e1\u4f1a\u306b\u53c2\u52a0\u3002Gmail\u3042\u308c\u3070\u4eca\u3059\u3050\u4f7f\u3048\u308b\u30aa\u30f3\u30e9\u30a4\u30f3\u4f1a\u8b70\u30c4\u30fc\u30eb\u3002</p>'
    '<div class="hero-chips">'
    '<span class="chip">\u2705 \u7121\u6599</span>'
    '<span class="chip">\u2705 \u753b\u9762\u5171\u6709</span>'
    '<span class="chip">\u2705 \u30ab\u30ec\u30f3\u30c0\u30fc\u9023\u643a</span>'
    '</div></div></header>'
    '<main style="max-width:900px;margin:0 auto;padding:48px 20px;">'
)
meet_footer = (
    '<div class="finish-banner">'
    '<div style="font-size:56px;margin-bottom:16px;">&#127881;</div>'
    '<h2>\u304a\u75b2\u308c\u3055\u307e\u3067\u3057\u305f\uff01</h2>'
    '<p>Google Meet\u3067\u3001\u5f79\u54e1\u4f1a\u304c\u300c\u5b66\u6821\u306b\u884c\u304b\u306a\u304f\u3066\u3044\u3044\u300d\u306b\u306a\u308a\u307e\u3059\u3002<br>'
    '\u6700\u521d\u306e\u4f1a\u8b70\u3067\u64cd\u4f5c\u3092\u899a\u3048\u308c\u3070\u3001\u3042\u3068\u306f\u5168\u54e1\u304c\u6c17\u8efd\u306b\u53c2\u52a0\u3067\u304d\u307e\u3059\u3002</p>'
    '</div></main>'
    '<footer><p>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9 | PTA \u30c7\u30b8\u30bf\u30eb\u63a8\u9032\u59d4\u54e1\u4f1a</p></footer>'
)
build('meet.html', 'Google Meet \u6d3b\u7528\u30ac\u30a4\u30c9 | PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb', '#0277bd', meet_hero + meet_body + meet_footer)

# ===================================================
# canva.html
# ===================================================
canva_body = read('canva_body.html')
canva_hero = (
    '<header class="hero" style="background:linear-gradient(135deg,#7d2ae8 0%,#00c4cc 100%);">'
    '<div class="hero-inner">'
    '<div class="hero-badge">PTA \u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb\uff08\u5225\u30b5\u30fc\u30d3\u30b9\uff09</div>'
    '<h1>&#127912; Canva\uff08\u30ad\u30e3\u30f3\u30d0\uff09<br><span>\u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9</span></h1>'
    '<p class="hero-sub">\u30d7\u30ed\u4e26\u307f\u306e\u304a\u4fbf\u308a\u3084\u30c1\u30e9\u30b7\u304c\u6570\u5206\u3067\u4f5c\u308c\u307e\u3059\u3002\u8c4a\u5bcc\u306a\u30c6\u30f3\u30d7\u30ec\u30fc\u30c8\u3092\u9078\u3076\u3060\u3051\u3002</p>'
    '<div class="hero-chips">'
    '<span class="chip">\u2705 \u30c1\u30e9\u30b7\u4f5c\u6210</span>'
    '<span class="chip">\u2705 \u5171\u540c\u7de8\u96c6</span>'
    '<span class="chip">\u2705 \u7121\u6599\u30c6\u30f3\u30d7\u30ec\u30fc\u30c8</span>'
    '</div></div></header>'
    '<main style="max-width:900px;margin:0 auto;padding:48px 20px;">'
)
canva_footer = (
    '<div class="finish-banner">'
    '<div style="font-size:56px;margin-bottom:16px;">&#127881;</div>'
    '<h2>\u304a\u75b2\u308c\u3055\u307e\u3067\u3057\u305f\uff01</h2>'
    '<p>Canva\u3092\u4f7f\u3048\u3070\u3001\u3082\u3046\u4ee5\u524d\u306e\u304a\u4fbf\u308a\u4f5c\u6210\u306b\u306f\u623b\u308c\u307e\u305b\u3093\u3002<br>'
    '\u305c\u3072\u6b21\u306e\u30a4\u30d9\u30f3\u30c8\u544a\u77e5\u3067\u4f55\u304b1\u3064\u4f5c\u3063\u3066\u307f\u3066\u304f\u3060\u3055\u3044\u3002</p>'
    '</div></main>'
    '<footer><p>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9 | PTA \u30c7\u30b8\u30bf\u30eb\u63a8\u9032\u59d4\u54e1\u4f1a</p></footer>'
)
build('canva.html', 'Canva \u6d3b\u7528\u30ac\u30a4\u30c9 | PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb', '#7d2ae8', canva_hero + canva_body + canva_footer)

# ===================================================
# chouseisan.html
# ===================================================
chouseisan_body = read('chouseisan_body.html')
chouseisan_hero = (
    '<header class="hero" style="background:linear-gradient(135deg,#00897b 0%,#4db6ac 100%);">'
    '<div class="hero-inner">'
    '<div class="hero-badge">PTA \u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb\uff08\u5225\u30b5\u30fc\u30d3\u30b9\uff09</div>'
    '<h1>&#128197; \u8abf\u6574\u3055\u3093<br><span>\u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9</span></h1>'
    '<p class="hero-sub">\u9762\u5012\u306a\u4f1a\u8b70\u306e\u65e5\u7a0b\u8abf\u6574\u304c\u30ea\u30f3\u30af\u3092\u9001\u308b\u3060\u3051\u3067\u5b8c\u4e86\u3002\u56de\u7b54\u306f\u81ea\u52d5\u3067\u96c6\u8a08\u3055\u308c\u307e\u3059\u3002</p>'
    '<div class="hero-chips">'
    '<span class="chip">\u2705 \u65e5\u7a0b\u8abf\u6574</span>'
    '<span class="chip">\u2705 \u4f1a\u54e1\u767b\u9332\u4e0d\u8981</span>'
    '<span class="chip">\u2705 0\u5186</span>'
    '</div></div></header>'
    '<main style="max-width:900px;margin:0 auto;padding:48px 20px;">'
)
chouseisan_footer = (
    '<div class="finish-banner">'
    '<div style="font-size:56px;margin-bottom:16px;">&#127881;</div>'
    '<h2>\u304a\u75b2\u308c\u3055\u307e\u3067\u3057\u305f\uff01</h2>'
    '<p>\u8abf\u6574\u3055\u3093\u3092\u4f7f\u3048\u3070\u3001LINE\u304c\u65e5\u7a0b\u8abf\u6574\u306e\u6295\u7a3f\u3067\u57cb\u307e\u308b\u3053\u3068\u306f\u3042\u308a\u307e\u305b\u3093\u3002<br>'
    '\u305c\u3072\u6b21\u306e\u5f79\u54e1\u4f1a\u3067\u4f7f\u3063\u3066\u307f\u3066\u304f\u3060\u3055\u3044\u3002</p>'
    '</div></main>'
    '<footer><p>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9 | PTA \u30c7\u30b8\u30bf\u30eb\u63a8\u9032\u59d4\u54e1\u4f1a</p></footer>'
)
build('chouseisan.html', '\u8abf\u6574\u3055\u3093 \u6d3b\u7528\u30ac\u30a4\u30c9 | PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb', '#00897b', chouseisan_hero + chouseisan_body + chouseisan_footer)

print('\nAll done!')
