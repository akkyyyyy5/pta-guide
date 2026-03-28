import os

# ----------------------------------------------------------------
# 1. 各ツールの基本データ
# ----------------------------------------------------------------
TOOLS = {
    "forms": {
        "title": "Googleフォーム",
        "icon": "📋",
        "color": "#EC407A",
        "url": "https://forms.google.com"
    },
    "docs": {
        "title": "Googleドキュメント",
        "icon": "📝",
        "color": "#1565c0",
        "url": "https://docs.google.com"
    },
    "drive": {
        "title": "Googleドライブ",
        "icon": "📁",
        "color": "#FFB300",
        "url": "https://drive.google.com"
    },
    "lineworks": {
        "title": "LINE WORKS",
        "icon": "💬",
        "color": "#00a800",
        "url": "https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2"
    },
    "sheets": {
        "title": "スプレッドシート",
        "icon": "📊",
        "color": "#1b5e20",
        "url": "https://docs.google.com"
    },
    "meet": {
        "title": "Google Meet",
        "icon": "📹",
        "color": "#0277bd",
        "url": "https://meet.google.com"
    },
    "canva": {
        "title": "Canva",
        "icon": "🎨",
        "color": "#7d2ae8",
        "url": "https://canva.com"
    },
    "chouseisan": {
        "title": "調整さん",
        "icon": "📅",
        "color": "#00897b",
        "url": "https://chouseisan.com"
    }
}

# ----------------------------------------------------------------
# 2. 各エディションの「枠組み（Shell）」
# ----------------------------------------------------------------

def get_modern_shell(tool_id, body_html):
    t = TOOLS[tool_id]
    nav_links = "".join([f'<a href="modern_{k}.html">{"💬" if k=="lineworks" else TOOLS[k]["icon"]} {TOOLS[k]["title"].split()[0]}</a>' for k in TOOLS])
    
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{t['title']} 活用ガイド | PTAデジタルツール | Modern Edition</title>
<link rel="stylesheet" href="modern.css">
</head>
<body>

<nav class="toc">
    <div class="toc-inner">
        <a href="modern.html" style="color:var(--orange-primary);font-weight:900;">← 戻る</a>
        {nav_links}
    </div>
</nav>

<main class="container">
{body_html}
<div class="finish-banner"><div style="font-size:56px;margin-bottom:16px;">&#127881;</div><h2>お疲れさまでした！</h2><p>{t['title']}を活用して、PTA運営をスマートに改善しましょう。</p></div>
</main>

<footer>
    <p>柿生小学校PTA デジタル活用ガイド</p>
    <p style="margin-top:6px;opacity:0.6;">Designed by Apple-style Modern UI for PTA</p>
</footer>

<script>
    const observer = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
            if (entry.isIntersecting) {{
                entry.target.classList.add('reveal');
            }}
        }});
    }}, {{ threshold: 0.1 }});
    document.querySelectorAll('.step-section, .intro-box, .mockup-wrap, .finish-banner, .point-box, .annotation, .warn-box').forEach(el => {{
        el.classList.add('reveal');
        observer.observe(el);
    }});
</script>
</body>
</html>'''

def get_kawaii_shell(tool_id, body_html):
    t = TOOLS[tool_id]
    nav_links = "".join([f'<a href="kawaii_{k}.html">{TOOLS[k]["icon"]} {TOOLS[k]["title"].split()[0]}</a>' for k in TOOLS])
    
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{t['title']} 活用ガイド | PTAデジタルツール | Kawaii Edition</title>
<link rel="stylesheet" href="kawaii.css">
</head>
<body>

<nav class="toc">
    <div class="toc-inner">
        <a href="kawaii.html" style="color:var(--orange-soft);font-weight:900;">← 戻る</a>
        {nav_links}
    </div>
</nav>

<main class="container">
{body_html}
<div class="finish-banner"><div style="font-size:56px;margin-bottom:16px;">&#127881;</div><h2>お疲れさまでした！</h2><p>{t['title']}を使って、楽しくラクにPTA活動を進めていきましょう♪</p></div>
</main>

<footer>
    <p>柿生小学校PTA デジタル活用ガイド</p>
    <p style="margin-top:6px;opacity:0.6;">Designed by Sweet & Friendly UI for PTA Moms</p>
</footer>

<script>
    const observer = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
            if (entry.isIntersecting) {{
                entry.target.classList.add('reveal');
            }}
        }});
    }}, {{ threshold: 0.1 }});
    document.querySelectorAll('.step-section, .intro-box, .mockup-wrap, .finish-banner, .point-box, .annotation, .warn-box').forEach(el => {{
        el.classList.add('reveal');
        observer.observe(el);
    }});
</script>
</body>
</html>'''

def build():
    # 各ツールの「本文」を読み込む
    for tid in TOOLS:
        body_file = f"{tid}_body.html"
        if tid == "lineworks": body_file = "lw_body.html"
        
        if not os.path.exists(body_file):
            print(f"Warning: {body_file} not found.")
            continue
        
        with open(body_file, 'r', encoding='utf-8') as f:
            body = f.read()
            
        # 簡易版がある場合（formsなど）
        quick_body_file = f"{tid}_quick_body.html"
        if os.path.exists(quick_body_file):
             # 簡易版のビルドは別途ロジックが必要だが、現状は個別ファイルで管理
             pass

        # Build Modern
        out_modern = os.path.abspath(f"modern_{tid}.html")
        with open(out_modern, "w", encoding='utf-8') as f:
            f.write(get_modern_shell(tid, body))
        print(f"Generated: {out_modern}")
            
        # Build Kawaii
        out_kawaii = os.path.abspath(f"kawaii_{tid}.html")
        with open(out_kawaii, "w", encoding='utf-8') as f:
            f.write(get_kawaii_shell(tid, body))
        print(f"Generated: {out_kawaii}")

if __name__ == "__main__":
    build()
