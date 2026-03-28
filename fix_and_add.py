# -*- coding: utf-8 -*-
"""
最終修正スクリプト
文字化け修正 + 3セクション追加 + ナビ追加を一括で実施

文字化けの根本原因: 
  元のファイル(UTF-8)が、CP932で読まれ、UTF-8で書き直された。
  → encode('cp932' errors='surrogateescape').decode('utf-8') で修正可能
  
注意: errors='ignore' ではなく errors='surrogateescape' を使い
      絵文字等のCP932外文字が消えないようにする
"""

import sys

filepath = r'f:\Antigravity\ニュースを自動で収集\pta-guide\index.html'

# ---------- STEP 1: ファイルを読み込む ----------
with open(filepath, 'rb') as f:
    raw = f.read()

if raw[:3] == b'\xef\xbb\xbf':
    garbled_text = raw[3:].decode('utf-8', errors='surrogatepass')
else:
    garbled_text = raw.decode('utf-8', errors='surrogatepass')

print(f"Read {len(garbled_text)} chars")

# ---------- STEP 2: 文字化けチェック ----------
# 「完了」が文字化けしているか確認
if '完亁E' in garbled_text or '繝輔ぃ' in garbled_text:
    print("Mojibake detected, attempting fix...")
    # Fix: utf-8で読んだ文字 -> cp932でバイト化 -> utf-8として解釈
    # surrogatepassを使って絵文字などの非CP932文字もバイトとして扱う
    try:
        fixed_bytes = garbled_text.encode('cp932', errors='surrogateescape')
        fixed_text = fixed_bytes.decode('utf-8', errors='replace')
        print(f"Fixed {len(fixed_text)} chars")
    except Exception as e:
        print(f"Fix failed: {e}")
        # fallback: ignore errors
        fixed_bytes = garbled_text.encode('cp932', errors='ignore')
        fixed_text = fixed_bytes.decode('utf-8', errors='replace')
        print(f"Fixed with ignore: {len(fixed_text)} chars")
else:
    print("No mojibake detected, using as-is")
    fixed_text = garbled_text

# タイトル確認
t_s = fixed_text.find('<title>')
t_e = fixed_text.find('</title>')
print(f"Title: {fixed_text[t_s:t_e+8]}")

# 完了バナー確認
fb_idx = fixed_text.find('finish-banner')
print(f"finish-banner at: {fb_idx}")
if fb_idx >= 0:
    print(f"Context: {fixed_text[fb_idx-50:fb_idx+100]}")

# ---------- STEP 3: セクションを挿入 ----------
NEW_SECTIONS = """
  <hr class="divider">

  <!-- LINE WORKS セクション -->
  <section class="step-section" id="step-lineworks">
    <div class="step-header">
      <div class="step-number" style="background:linear-gradient(135deg,#00c300,#00a800);box-shadow:0 4px 12px rgba(0,163,0,0.35);">&#x1F4AC;</div>
      <div class="step-title-group">
        <h2>LINE WORKS の活用（非営利団体プラン）</h2>
        <p>PTAにぴったり！無料で使えるビジネスLINE</p>
      </div>
    </div>
    <div class="step-body">
      <div class="instruction-text">
        LINE WORKSは、普段使いのLINEに似た操作感で使えるビジネス向けチャットツールです。<strong>非営利団体（PTAを含む）は無料で利用できる「フリープラン」</strong>が用意されており、役員間の連絡・グループトーク・ファイル共有をプライベートのLINEアカウントと混ぜずにすっきり管理できます。
      </div>
      <div class="mockup-wrap">
        <div class="browser-bar">
          <div class="browser-dots">
            <div class="browser-dot d-red"></div>
            <div class="browser-dot d-yellow"></div>
            <div class="browser-dot d-green"></div>
          </div>
          <div class="address-bar">&#x1F512; lineworks.naver.jp &mdash; LINE WORKS</div>
        </div>
        <div class="browser-content">
          <div style="display:flex;min-height:320px;">
            <div style="width:56px;background:#00c300;display:flex;flex-direction:column;align-items:center;padding:12px 0;gap:16px;">
              <div style="width:36px;height:36px;background:white;border-radius:8px;display:flex;align-items:center;justify-content:center;font-weight:900;color:#00c300;font-size:14px;">LW</div>
              <div style="color:rgba(255,255,255,0.7);font-size:20px;">&#x1F4AC;</div>
              <div style="color:rgba(255,255,255,0.7);font-size:20px;">&#x1F4C5;</div>
              <div style="color:rgba(255,255,255,0.7);font-size:20px;">&#x1F4C1;</div>
              <div style="color:rgba(255,255,255,0.7);font-size:20px;">&#x1F465;</div>
            </div>
            <div style="width:220px;background:#f7f7f7;border-right:1px solid #e0e0e0;">
              <div style="padding:12px 14px;font-size:13px;font-weight:700;color:#333;border-bottom:1px solid #e0e0e0;">トーク</div>
              <div style="padding:10px 14px;display:flex;gap:10px;align-items:center;background:white;border-left:3px solid #00c300;">
                <div style="width:36px;height:36px;background:linear-gradient(135deg,#00c300,#00a800);border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:14px;font-weight:700;flex-shrink:0;">PTA</div>
                <div>
                  <div style="font-size:13px;font-weight:700;color:#202124;">&#x1F4CC; 2025年度 役員会</div>
                  <div style="font-size:11px;color:#9e9e9e;">田中さん：了解しました！</div>
                </div>
              </div>
              <div style="padding:10px 14px;display:flex;gap:10px;align-items:center;">
                <div style="width:36px;height:36px;background:#e3f2fd;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#1a73e8;font-size:16px;flex-shrink:0;">&#x2B50;</div>
                <div>
                  <div style="font-size:13px;font-weight:700;color:#202124;">星空観察 実行班</div>
                  <div style="font-size:11px;color:#9e9e9e;">山田さん：望遠鏡の数は...</div>
                </div>
              </div>
              <div style="padding:10px 14px;display:flex;gap:10px;align-items:center;">
                <div style="width:36px;height:36px;background:#fce4ec;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#e91e63;font-size:12px;font-weight:700;flex-shrink:0;">会計</div>
                <div>
                  <div style="font-size:13px;font-weight:700;color:#202124;">&#x1F4B0; 会計担当グループ</div>
                  <div style="font-size:11px;color:#9e9e9e;">鈴木さん：領収書を送りました</div>
                </div>
              </div>
            </div>
            <div style="flex:1;display:flex;flex-direction:column;background:white;">
              <div style="padding:10px 16px;border-bottom:1px solid #e0e0e0;font-size:13px;font-weight:700;color:#202124;">&#x1F4CC; 2025年度 役員会 <span style="font-size:11px;color:#9e9e9e;font-weight:400;">8名</span></div>
              <div style="flex:1;padding:14px 16px;display:flex;flex-direction:column;gap:12px;overflow:hidden;">
                <div style="display:flex;gap:8px;">
                  <div style="width:28px;height:28px;background:#f06292;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:11px;font-weight:700;flex-shrink:0;">田</div>
                  <div>
                    <div style="font-size:10px;color:#9e9e9e;margin-bottom:3px;">田中さん 10:32</div>
                    <div style="background:#f1f3f4;border-radius:0 12px 12px 12px;padding:8px 12px;font-size:13px;max-width:220px;">星空観察の参加フォーム、みなさん確認できましたか？</div>
                  </div>
                </div>
                <div style="display:flex;gap:8px;">
                  <div style="width:28px;height:28px;background:#42a5f5;border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:11px;font-weight:700;flex-shrink:0;">山</div>
                  <div>
                    <div style="font-size:10px;color:#9e9e9e;margin-bottom:3px;">山田さん 10:35</div>
                    <div style="background:#f1f3f4;border-radius:0 12px 12px 12px;padding:8px 12px;font-size:13px;max-width:220px;">確認しました！望遠鏡は3台確保できました &#x1F52D;</div>
                  </div>
                </div>
                <div style="display:flex;justify-content:flex-end;">
                  <div style="background:#dcf8c6;border-radius:12px 0 12px 12px;padding:8px 12px;font-size:13px;max-width:220px;">了解です。当日の段取りをMeetで確認しませんか？</div>
                </div>
              </div>
              <div style="padding:8px 12px;border-top:1px solid #e0e0e0;display:flex;gap:8px;">
                <input style="flex:1;border:1px solid #e0e0e0;border-radius:20px;padding:8px 14px;font-size:13px;outline:none;" placeholder="メッセージを入力..." readonly>
                <button style="background:#00c300;color:white;border:none;border-radius:50%;width:32px;height:32px;cursor:pointer;">&#x25B6;</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="annotation">
        <div class="annotation-circle" style="background:#00c300;">1</div>
        <div class="annotation-text"><strong>グループトーク</strong>: 役員全体・係ごとなど複数のグループを作成可能。普段のLINEとは完全に分離できます。</div>
      </div>
      <div class="annotation">
        <div class="annotation-circle" style="background:#00c300;">2</div>
        <div class="annotation-text"><strong>既読表示・アナウンス</strong>: メッセージの既読人数が確認でき、重要なお知らせを「アナウンス」として固定表示できます。</div>
      </div>
      <div class="point-box">
        <div class="label">&#x1F4A1; 非営利団体プランの始め方</div>
        <ol style="padding-left:20px;margin-top:6px;">
          <li><a href="https://line.worksmobile.com/jp/" target="_blank" style="color:#1a73e8;">line.worksmobile.com</a> にアクセスして「無料で始める」をクリック</li>
          <li>PTAの代表者（会長）のメールアドレスでアカウント作成</li>
          <li>「管理者画面」から役員のメールアドレスを招待</li>
          <li>招待された役員はスマホアプリをインストールしてログイン</li>
        </ol>
      </div>
      <div class="point-box">
        <div class="label">&#x1F4A1; フリープランでできること</div>
        メッセージ送受信・グループトーク・ファイル共有（1GB）・カレンダー共有・アンケート機能など、PTAの日常業務に必要な機能はほぼ無料で使えます。
      </div>
      <div class="warn-box">
        <div class="label">&#x26A0;&#xFE0F; 個人LINEとは別物です</div>
        LINE WORKSは普段のLINEとは別のアプリです。役員のプライベートLINEアカウントに連絡が届くことはなく、業務と私生活をきっちり分離できます。
      </div>
    </div>
  </section>

  <hr class="divider">

  <!-- スプレッドシート セクション -->
  <section class="step-section" id="step-sheets">
    <div class="step-header">
      <div class="step-number" style="background:linear-gradient(135deg,#1b5e20,#43a047);box-shadow:0 4px 12px rgba(67,160,71,0.35);">&#x1F4CA;</div>
      <div class="step-title-group">
        <h2>Googleスプレッドシートで名簿・会計・進捗を管理</h2>
        <p>Excel感覚でクラウド管理。リアルタイムで全員が確認できる</p>
      </div>
    </div>
    <div class="step-body">
      <div class="instruction-text">
        GoogleスプレッドシートはExcelのオンライン版です。<strong>役員名簿・会計帳簿・イベント進捗表など、PTAの管理業務に必須の表計算</strong>をクラウド上で管理できます。Googleフォームの回答が自動的にスプレッドシートに集まるため、集計の手間がゼロになります。
      </div>
      <div class="mockup-wrap">
        <div class="browser-bar">
          <div class="browser-dots">
            <div class="browser-dot d-red"></div>
            <div class="browser-dot d-yellow"></div>
            <div class="browser-dot d-green"></div>
          </div>
          <div class="address-bar">&#x1F512; docs.google.com/spreadsheets/d/xxxxxxxxxx/edit</div>
        </div>
        <div class="browser-content">
          <div style="background:white;border-bottom:1px solid #e0e0e0;padding:8px 16px;display:flex;align-items:center;gap:10px;">
            <div style="width:28px;height:28px;background:linear-gradient(135deg,#1b5e20,#43a047);border-radius:4px;display:flex;align-items:center;justify-content:center;"><span style="color:white;font-size:14px;font-weight:700;">S</span></div>
            <div>
              <div style="font-size:14px;color:#202124;font-weight:500;">2025年度PTA 管理シート</div>
              <div style="font-size:10px;color:#5f6368;">&#x2601;&#xFE0F; 保存済み</div>
            </div>
          </div>
          <div style="background:#f8f9fc;border-bottom:1px solid #e0e0e0;padding:0 16px;display:flex;gap:0;overflow-x:auto;">
            <div style="padding:8px 16px;font-size:12px;background:white;border:1px solid #e0e0e0;border-bottom:none;border-radius:4px 4px 0 0;color:#43a047;font-weight:700;white-space:nowrap;">&#x1F465; 役員名簿</div>
            <div style="padding:8px 16px;font-size:12px;color:#5f6368;white-space:nowrap;">&#x1F4B0; 会計</div>
            <div style="padding:8px 16px;font-size:12px;color:#5f6368;white-space:nowrap;">&#x1F31F; イベント進捗</div>
            <div style="padding:8px 16px;font-size:12px;color:#5f6368;white-space:nowrap;">&#x1F4CA; フォーム回答</div>
          </div>
          <div style="overflow-x:auto;">
            <table style="width:100%;border-collapse:collapse;font-size:12px;">
              <thead>
                <tr>
                  <th style="padding:8px 12px;border:1px solid #c8e6c9;background:#43a047;color:white;text-align:left;">お名前</th>
                  <th style="padding:8px 12px;border:1px solid #c8e6c9;background:#43a047;color:white;text-align:left;">担当</th>
                  <th style="padding:8px 12px;border:1px solid #c8e6c9;background:#43a047;color:white;text-align:left;">学年</th>
                  <th style="padding:8px 12px;border:1px solid #c8e6c9;background:#43a047;color:white;text-align:left;">Gmail</th>
                </tr>
              </thead>
              <tbody>
                <tr style="background:#f1f8e9;">
                  <td style="padding:6px 12px;border:1px solid #dcedc8;font-weight:700;">田中 花子</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"><span style="background:#e8f5e9;color:#2e7d32;border-radius:4px;padding:2px 8px;font-size:11px;">会長</span></td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;">3年</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;color:#1a73e8;">hanako@xxx.com</td>
                </tr>
                <tr>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;font-weight:700;">山田 太郎</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"><span style="background:#e3f2fd;color:#1565c0;border-radius:4px;padding:2px 8px;font-size:11px;">副会長</span></td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;">5年</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;color:#1a73e8;">taro@xxx.com</td>
                </tr>
                <tr style="background:#f1f8e9;">
                  <td style="padding:6px 12px;border:1px solid #dcedc8;font-weight:700;">鈴木 良子</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"><span style="background:#fff8e1;color:#f57f17;border-radius:4px;padding:2px 8px;font-size:11px;">会計</span></td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;">1年</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;color:#1a73e8;">yoshiko@xxx.com</td>
                </tr>
                <tr>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;font-weight:700;">佐藤 祐一</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"><span style="background:#fce4ec;color:#c62828;border-radius:4px;padding:2px 8px;font-size:11px;">書記</span></td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;">2年</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;color:#1a73e8;">yuichi@xxx.com</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="annotation">
        <div class="annotation-circle" style="background:#43a047;">&#x1F4A1;</div>
        <div class="annotation-text">シートを複数タブに分けると管理が楽です。<strong>「役員名簿」「会計」「イベント進捗」「フォーム回答」</strong>の4シートで一本化するのがおすすめです。</div>
      </div>
      <div class="point-box">
        <div class="label">&#x1F4A1; おすすめのシート構成</div>
        <table style="width:100%;border-collapse:collapse;margin-top:8px;font-size:13px;">
          <tr><th style="text-align:left;padding:6px 8px;background:#f5f5f5;border:1px solid #e0e0e0;">シート名</th><th style="text-align:left;padding:6px 8px;background:#f5f5f5;border:1px solid #e0e0e0;">管理する内容</th></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">&#x1F465; 役員名簿</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">氏名・担当・学年・連絡先</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">&#x1F4B0; 会計</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">収支・領収書番号・残高（SUM関数で自動計算）</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">&#x1F31F; イベント進捗</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">準備タスク・担当者・期限・完了チェックボックス</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">&#x1F4CA; フォーム回答</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">Googleフォームから自動で流れ込む回答データ</td></tr>
        </table>
      </div>
      <div class="point-box">
        <div class="label">&#x1F4A1; Googleフォームと連携するには？</div>
        フォームの「回答」タブ &rarr; 「&#x1F4CA; スプレッドシートで表示」を押すだけ。回答が届くたびに自動でシートに追記されます。集計グラフも自動生成されます。
      </div>
    </div>
  </section>

  <hr class="divider">

  <!-- Google Meet セクション -->
  <section class="step-section" id="step-meet">
    <div class="step-header">
      <div class="step-number" style="background:linear-gradient(135deg,#0277bd,#039be5);box-shadow:0 4px 12px rgba(3,155,229,0.35);">&#x1F4F9;</div>
      <div class="step-title-group">
        <h2>Google Meet でオンライン会議を取り入れる</h2>
        <p>学校に行かなくてもいい。自宅から5分で役員会</p>
      </div>
    </div>
    <div class="step-body">
      <div class="instruction-text">
        Google Meetは、Googleが提供する無料のビデオ会議ツールです。<strong>Gmailアカウントがあれば今すぐ使えます</strong>。役員会・打ち合わせを完全オンラインにするだけで、「子どものお迎えがある」「仕事が終わらない」といった参加ハードルが一気に下がります。星空観察イベントの事前打ち合わせにも最適です。
      </div>
      <div class="mockup-wrap">
        <div class="browser-bar">
          <div class="browser-dots">
            <div class="browser-dot d-red"></div>
            <div class="browser-dot d-yellow"></div>
            <div class="browser-dot d-green"></div>
          </div>
          <div class="address-bar">&#x1F512; meet.google.com/abc-defg-hij</div>
        </div>
        <div class="browser-content" style="background:#202124;">
          <div style="min-height:300px;display:flex;flex-direction:column;">
            <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:4px;padding:8px;">
              <div style="background:#3c4043;border-radius:8px;padding:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;min-height:100px;">
                <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#1a73e8,#4285f4);display:flex;align-items:center;justify-content:center;color:white;font-size:20px;font-weight:700;">田</div>
                <div style="color:white;font-size:12px;">田中さん（会長）</div>
                <span style="background:rgba(255,255,255,0.1);border-radius:4px;padding:2px 8px;font-size:10px;color:rgba(255,255,255,0.7);">話し中</span>
              </div>
              <div style="background:#3c4043;border-radius:8px;padding:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;min-height:100px;">
                <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#e91e63,#f06292);display:flex;align-items:center;justify-content:center;color:white;font-size:20px;font-weight:700;">山</div>
                <div style="color:white;font-size:12px;">山田さん</div>
                <span style="background:rgba(255,87,34,0.3);border-radius:4px;padding:2px 8px;font-size:10px;color:#ff7043;">ミュート中</span>
              </div>
              <div style="background:#3c4043;border-radius:8px;padding:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;min-height:100px;">
                <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#f57f17,#ffa726);display:flex;align-items:center;justify-content:center;color:white;font-size:20px;font-weight:700;">鈴</div>
                <div style="color:white;font-size:12px;">鈴木さん</div>
                <span style="background:rgba(255,255,255,0.1);border-radius:4px;padding:2px 8px;font-size:10px;color:rgba(255,255,255,0.7);">&#x1F399;&#xFE0F;</span>
              </div>
              <div style="background:#2a2b2e;border-radius:8px;padding:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;border:2px dashed #5f6368;min-height:100px;">
                <div style="color:#9e9e9e;font-size:24px;">&#x1F464;</div>
                <div style="color:#9e9e9e;font-size:11px;">参加待ち…</div>
              </div>
            </div>
            <div style="background:#3c4043;padding:12px 20px;display:flex;justify-content:center;gap:16px;align-items:center;">
              <button style="width:44px;height:44px;border-radius:50%;background:#ea4335;border:none;color:white;font-size:16px;cursor:pointer;">&#x1F399;</button>
              <button style="width:44px;height:44px;border-radius:50%;background:#5f6368;border:none;color:white;font-size:16px;cursor:pointer;">&#x1F4F9;</button>
              <button style="width:44px;height:44px;border-radius:50%;background:#5f6368;border:none;color:white;font-size:16px;cursor:pointer;">&#x1F4CB;</button>
              <button style="width:44px;height:44px;border-radius:50%;background:#5f6368;border:none;color:white;font-size:16px;cursor:pointer;">&#x1F4AC;</button>
              <button style="width:44px;height:44px;border-radius:50%;background:#ea4335;border:none;color:white;font-size:16px;cursor:pointer;">&#x260F;</button>
            </div>
          </div>
        </div>
      </div>
      <div class="annotation">
        <div class="annotation-circle" style="background:#039be5;">1</div>
        <div class="annotation-text"><a href="https://meet.google.com" target="_blank" style="color:#1a73e8;"><strong>meet.google.com</strong></a> にアクセスして「新しい会議を作成」をクリックするだけ。リンクをコピーしてLINE WORKSやメールで送れば、相手はクリックするだけで参加できます。</div>
      </div>
      <div class="annotation">
        <div class="annotation-circle" style="background:#039be5;">2</div>
        <div class="annotation-text"><strong>画面共有</strong>: &#x1F4CB; ボタンから自分の画面を共有できます。スプレッドシートやドキュメントを見ながら進行できます。</div>
      </div>
      <div class="annotation">
        <div class="annotation-circle" style="background:#039be5;">3</div>
        <div class="annotation-text"><strong>Googleカレンダーと連携</strong>: カレンダーで予定を作ると、MeetリンクがURL付きで自動生成されます。招待状と同時に送れるので便利です。</div>
      </div>
      <div class="point-box">
        <div class="label">&#x1F4A1; よくある使い方パターン（PTA版）</div>
        <table style="width:100%;border-collapse:collapse;margin-top:8px;font-size:13px;">
          <tr><th style="text-align:left;padding:6px 8px;background:#f5f5f5;border:1px solid #e0e0e0;">場面</th><th style="text-align:left;padding:6px 8px;background:#f5f5f5;border:1px solid #e0e0e0;">活用方法</th></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">役員会（月1回）</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">全員オンラインで30分以内に終わらせる</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">イベント打ち合わせ</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">スプレッドシート進捗表を画面共有しながら確認</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">急ぎの相談</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">LINE WORKSでリンクを送り、即席でMeet開始</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">新役員への引き継ぎ</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">画面共有しながら操作説明を録画して保存</td></tr>
        </table>
      </div>
      <div class="point-box">
        <div class="label">&#x1F4A1; 無料で使える時間は？</div>
        Googleアカウントがあれば、<strong>1対1の会議は無制限</strong>、3人以上も<strong>60分まで無料</strong>（2024年現在）。PTAの役員会（30分程度）なら問題なく無料で使えます。
      </div>
    </div>
  </section>

"""

# finish-bannerの直前に挿入（複数のパターンを試みる）
MARKERS = [
    '        <!-- 完了 -->',
    '        <!-- 完亁E-->',
    '<div class="finish-banner">',
]

inserted = False
for marker in MARKERS:
    if marker in fixed_text:
        fixed_text = fixed_text.replace(marker, NEW_SECTIONS + marker, 1)
        print(f"Inserted before: {repr(marker)}")
        inserted = True
        break

if not inserted:
    # ファイル末尾の</main>の直前に挿入
    print("Inserting before </main>")
    fixed_text = fixed_text.replace('</main>', NEW_SECTIONS + '</main>', 1)

# ナビバーの更新（step-lineworksがまだない場合）
if 'step-lineworks' not in fixed_text:
    # step-driveリンクを探す
    drive_idx = fixed_text.find('#step-drive')
    if drive_idx >= 0:
        end_a = fixed_text.find('</a>', drive_idx) + 4
        nav_addition = '\n    <a href="#step-lineworks">&#x1F4AC; LINE WORKS</a>\n    <a href="#step-sheets">&#x1F4CA; スプレッド</a>\n    <a href="#step-meet">&#x1F4F9; Meet</a>'
        fixed_text = fixed_text[:end_a] + nav_addition + fixed_text[end_a:]
        print("Added nav links")

# 完了バナーのテキストを更新
old_text = 'フォーム・ドキュメント・ドライブの3つを使いこなせば、'
new_text = 'フォーム・ドキュメント・ドライブ・LINE WORKS・スプレッドシート・Meetを<br>使いこなせば、'
if old_text in fixed_text:
    fixed_text = fixed_text.replace(old_text, new_text)
    print("Updated banner text")

# ---------- STEP 4: BOM付きUTF-8で保存 ----------
with open(filepath, 'wb') as f:
    f.write(b'\xef\xbb\xbf')
    f.write(fixed_text.encode('utf-8'))

print(f"\n=== Final check ===")
with open(filepath, 'rb') as f:
    final_raw = f.read()
final = final_raw[3:].decode('utf-8')
t_s = final.find('<title>')
t_e = final.find('</title>')
print(f"Title: {final[t_s:t_e+8]}")
print(f"step-lineworks: {'step-lineworks' in final}")
print(f"step-sheets: {'step-sheets' in final}")
print(f"step-meet: {'step-meet' in final}")
fb = final.find('finish-banner')
print(f"finish-banner at: {fb}, context: {final[fb:fb+80]}")
print(f"Total lines: {final.count(chr(10))}")
