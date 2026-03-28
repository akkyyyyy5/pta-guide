# -*- coding: utf-8 -*-
import sys

filepath = r'f:\Antigravity\ニュースを自動で収集\pta-guide\index.html'

with open(filepath, 'rb') as f:
    raw = f.read()

print(f"File size: {len(raw)} bytes")
print(f"First 6 bytes: {raw[:6].hex()}")

# BOM check
if raw[:3] == b'\xef\xbb\xbf':
    print("Has UTF-8 BOM")
    content_bytes = raw[3:]
else:
    print("No BOM")
    content_bytes = raw

# Grab a known string area (title tag area)
sample = content_bytes[200:400]
print(f"\n--- Sample bytes (200-400) hex ---")
print(sample.hex())

# Try various decoding strategies and show the title
strategies = [
    ('utf-8', None),
    ('cp932', None),
    ('utf-8-sig', None),
    # Mojibake fix: bytes were originally UTF-8, got decoded as CP932, then re-encoded as UTF-8
    ('utf-8', 'cp932'),  # read as utf-8, encode as cp932 -> gives back original UTF-8 bytes
]

for read_enc, fix_enc in strategies:
    try:
        text = content_bytes.decode(read_enc, errors='replace')
        if fix_enc:
            # Re-encode as fix_enc to get original bytes, then decode as utf-8
            text = text.encode(fix_enc, errors='replace').decode('utf-8', errors='replace')
            label = f"decode({read_enc}) then encode({fix_enc}) then decode(utf-8)"
        else:
            label = f"decode({read_enc})"
        # Show title
        start = text.find('<title>')
        end = text.find('</title>')
        if start >= 0 and end >= 0:
            print(f"\n[{label}]")
            print(f"  title: {text[start:end+8]}")
        else:
            print(f"\n[{label}] - no title found")
    except Exception as e:
        print(f"\n[{read_enc}/{fix_enc}] ERROR: {e}")
