"""build.py -- reads _css.txt + body_*.html parts, writes index.html (UTF-8 BOM)"""
import os
base = r'f:\Antigravity\ニュースを自動で収集\pta-guide'

def r(name):
    with open(os.path.join(base, name), encoding='utf-8') as f:
        return f.read()

css = r('_css.txt')
js  = r('_js.txt')
parts = ['body_p1.html','body_p2.html','body_p3.html','body_p4.html']
body  = '\n'.join(r(p) for p in parts)

html = f'<!DOCTYPE html>\n<html lang="ja">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width,initial-scale=1.0">\n<title>Google\u6d3b\u7528\u30ac\u30a4\u30c9\uff08\u30d5\u30a9\u30fc\u30e0\u30fb\u30c9\u30ad\u30e5\u30e1\u30f3\u30c8\u30fb\u30c9\u30e9\u30a4\u30d6\u30fbLINE WORKS\u30fb\u30b9\u30d7\u30ec\u30c3\u30c9\u30b7\u30fc\u30c8\u30fbMeet\uff09| PTA\u5411\u3051</title>\n<meta name="description" content="PTA\u306e\u5f79\u54e1\u30fb\u4fdd\u8b77\u8005\u5411\u3051\u306b\uff0cGoogle\u30c4\u30fc\u30eb\u306eIT\u6d3b\u7528\u30ac\u30a4\u30c9\u3002\u30d5\u30a9\u30fc\u30e0\u30fb\u30c9\u30ad\u30e5\u30e1\u30f3\u30c8\u30fb\u30c9\u30e9\u30a4\u30d6\u30fbLINE WORKS\u30fb\u30b9\u30d7\u30ec\u30c3\u30c9\u30fb Meet\u306e\u57fa\u672c\u3092\u89e3\u8aac\u3002">\n<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">\n{css}\n</head>\n<body>\n{body}\n{js}\n</body>\n</html>'

out = os.path.join(base, 'index.html')
with open(out, 'wb') as f:
    f.write(b'\xef\xbb\xbf')
    f.write(html.encode('utf-8'))
print('Done!', len(html), 'chars')
