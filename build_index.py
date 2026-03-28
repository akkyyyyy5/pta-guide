"""build_index.py -- index.htmlをビルド（簡易ポータル版）"""
import os
base = r'f:\Antigravity\ニュースを自動で収集\pta-guide'

def r(name):
    with open(os.path.join(base, name), encoding='utf-8') as f:
        return f.read()

css = r('_css.txt')
body = r('idx_body.html')

js = """<script defer>
  // カードのホバーアニメーションはインラインで設定済み
</script>"""

html = (
    '<!DOCTYPE html>\n<html lang="ja">\n<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width,initial-scale=1.0">\n'
    '<title>PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9 | PTA\u30c7\u30b8\u30bf\u30eb\u63a8\u9032</title>\n'
    '<meta name="description" content="PTA\u5f79\u54e1\u5411\u3051 PTA\u30c7\u30b8\u30bf\u30eb\u30c4\u30fc\u30eb \u304b\u3093\u305f\u3093\u6d3b\u7528\u30ac\u30a4\u30c9\u3002\u30d5\u30a9\u30fc\u30e0\u30fb\u30c9\u30ad\u30e5\u30e1\u30f3\u30c8\u30fb\u30c9\u30e9\u30a4\u30d6\u30fbLINE WORKS\u30fb\u30b9\u30d7\u30ec\u30c3\u30c9\u30b7\u30fc\u30c8\u30fbMeet\u3092\u89e3\u8aac\u3002">\n'
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">\n'
    + css + '\n</head>\n<body>\n' + body + '\n' + js + '\n</body>\n</html>'
)

out = os.path.join(base, 'index.html')
with open(out, 'wb') as f:
    f.write(b'\xef\xbb\xbf')
    f.write(html.encode('utf-8'))
print('index.html done!', len(html), 'chars')
