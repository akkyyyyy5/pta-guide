import os
import re

LW_BODY_PATH = r"f:\Antigravity\ニュースを自動で収集\pta-guide\lw_body.html"
P4_BODY_PATH = r"f:\Antigravity\ニュースを自動で収集\pta-guide\body_p4.html"

new_box = """        <div class="point-box" style="background:#fff8e1;border-left:4px solid #ffb300;margin-top:24px;box-shadow:0 4px 12px rgba(255,179,0,0.15);">
            <div class="label" style="color:#f57f17;font-size:16px;">🎁 非営利団体様向け特別プラン（期間限定）</div>
            <div style="font-size:14px;color:#333;margin-bottom:12px;line-height:1.6;">
                LINE WORKSフリープランの機能に加えて、以下をご利用になれます。<br>
                <span style="font-size:12px;color:#d32f2f;font-weight:700;">※下記のアップデート以外の機能はフリープランと同様のプランです。</span>
            </div>
            <ul style="padding-left:0;list-style:none;margin-bottom:16px;font-size:14px;color:#444;">
                <li style="margin-bottom:12px;background:#fff;padding:12px;border-radius:8px;border:1px solid #ffe082;">
                    <div style="color:#f57f17;font-weight:900;font-size:15px;margin-bottom:4px;">👥 最大1,000人で利用可能</div>
                    フリープランでは最大30人上限のところ、<strong>最大1,000人まで無料</strong>で利用できます。
                </li>
                <li style="background:#fff;padding:12px;border-radius:8px;border:1px solid #ffe082;">
                    <div style="color:#f57f17;font-weight:900;font-size:15px;margin-bottom:4px;">💾 50GBのストレージ容量で利用可能</div>
                    フリープランでは5GBが提供されるデータ容量ですが、本特別プランでは<strong>50GBのストレージ容量</strong>でサービスを利用できます。
                </li>
            </ul>
            <div style="background:#ffebee;border-left:4px solid #f44336;padding:12px;border-radius:0 8px 8px 0;font-size:13px;color:#c62828;margin-bottom:16px;">
                <strong>⚠️ ご注意</strong><br>
                既にLINE WORKSをお使いの場合、使用中のLINE WORKSに非営利団体プランを適用することはできません。<br>
                非営利団体プラン開設 ▶︎▶︎ <strong>専用ページから新しく開設</strong>いただく必要がございます。
            </div>
            <div style="text-align:center;">
                <a href="http://works.do/FUpYVNS" target="_blank" style="display:inline-block;background:linear-gradient(135deg, #ff9800, #f57f17);color:white;font-weight:900;padding:14px 28px;border-radius:12px;text-decoration:none;font-size:16px;box-shadow:0 4px 12px rgba(245,127,23,0.3);">👉 専用ページから新しく開設する</a>
                <div style="font-size:12px;color:#9e9e9e;margin-top:8px;">専用リンク：http://works.do/FUpYVNS</div>
            </div>
        </div>"""

# Modify lw_body.html
with open(LW_BODY_PATH, "r", encoding="utf-8") as f:
    lw_content = f.read()

# Add standard link disclaimers to lw_body.html
lw_content = lw_content.replace(
    '<div class="label" style="color:#00a800;">💡 <a href="https://jp2-pay.worksmobile.com',
    '<div class="label" style="color:#00a800;">💡 <a href="https://jp2-pay.worksmobile.com'
)
if "※上記リンク先は一般のLINE WORKSのページです" not in lw_content:
    lw_content = lw_content.replace(
        '<strong>PTAなどの非営利団体は、専用のプランによって大容量が無料で利用できます。</strong>',
        '<strong>PTAなどの非営利団体は、専用のプランによって大容量が無料で利用できます。</strong>\n    <p style="font-size:12px;color:#777;margin-top:8px;font-weight:700;">※記載の既存リンク（line.worksmobile.com等）は一般のLINE WORKSのリンクです。「非営利団体様向け特別プラン」をご希望の場合は、ページ下部の専用リンクをご利用ください。</p>'
    )
if "一般のLINE WORKSのリンク" not in lw_content.split('instruction-text')[1]:
    lw_content = lw_content.replace(
        '選ぶと無料プランが適用されます。',
        '選ぶと無料プランが適用されます。<br><span style="color:#d32f2f;font-weight:bold;font-size:12px;">（※こちらは一般のLINE WORKSのリンクです。特別プランをご希望の場合は下の専用リンクをご利用ください）</span>'
    )

# Insert new_box into lw_body.html right before <div class="point-box"> 💡 登録の流れ
if "🎁 非営利団体様向け特別プラン" not in lw_content:
    lw_content = lw_content.replace(
        '        <div class="point-box">\n            <div class="label">💡 登録の流れ（約5分）',
        new_box + '\n        <div class="point-box">\n            <div class="label">💡 登録の流れ（約5分）'
    )

with open(LW_BODY_PATH, "w", encoding="utf-8") as f:
    f.write(lw_content)


# Modify body_p4.html
with open(P4_BODY_PATH, "r", encoding="utf-8") as f:
    p4_content = f.read()

old_p4_box = """        <div class="point-box" style="background:#e8f5e9;border-left:4px solid #00c300;">
            <div class="label" style="color:#00a800;">ℹ️ 特別プランの仕様と免責</div>
            ストレージ <strong>50GB</strong> / 最大 <strong>1,000人</strong> まで無料です。
            <div style="font-size:11px;color:#666;margin-top:4px;">
                ※動画の多用にはご注意ください。ルール変更の可能性があるため、最新情報は必ず <a href="https://jp2-pay.worksmobile.com/oneapp/join?campaignKey=81bb874d91f3a982cbf65441e4c0b4ae3a6d9eb6e89d285cdd4ea564bd89671e67eb70d4706eabdee020691f537812d2" target="_blank" class="text-link"
                    style="color:#00a800;">公式HP</a> をご確認ください。
            </div>
        </div>"""

if "🎁 非営利団体様向け特別プラン" not in p4_content:
    # We might need regex if exact whitespace differs due to my previous auto quote fix script
    p4_content = re.sub(
        r'<div class="point-box"[^>]*>.*?ℹ️ 特別プランの仕様と免責.*?</div>\s*</div>', 
        new_box + '\n    </div>', 
        p4_content, 
        flags=re.DOTALL
    )

# Fix quick guide links note
if "※記載の既存リンク" not in p4_content:
    p4_content = p4_content.replace(
        'プライベートのLINEアカウントと混ぜずにすっきり管理できます。',
        'プライベートのLINEアカウントと混ぜずにすっきり管理できます。<br><span style="font-size:12px;color:#d32f2f;font-weight:700;">※記載の既存リンク（line.worksmobile.com等）は一般のLINE WORKSのリンクです。</span>'
    )

with open(P4_BODY_PATH, "w", encoding="utf-8") as f:
    f.write(p4_content)

print("Done editing HTML templates.")
