# -*- coding: utf-8 -*-
"""
LINE WORKS / Spreadsheet / Meet セクションをHTMLに追加
エンコーディング: BOM付きUTF-8で正しく読み書き
"""

FINISH_MARKER = '        <!-- 完了 -->'

NEW_SECTIONS = r"""
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
        LINE WORKSは、普段使いのLINEに似た操作感で使えるビジネス向けチャットツールです。<strong>非営利団体（PTAを含む）は無料で利用できる「フリープラン」</strong>が用意されており、メンバー間の連絡・グループトーク・ファイル共有をプライベートのLINEアカウントと混ぜずにすっきり管理できます。
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
          <div style="display:flex;min-height:320px;font-family:'Noto Sans JP',sans-serif;">
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
                  <div style="font-size:13px;font-weight:700;color:#202124;">&#x1F4CC; 2025年度 ミーティング</div>
                  <div style="font-size:11px;color:#9e9e9e;">田中さん：了解しました！</div>
                </div>
              </div>
              <div style="padding:10px 14px;display:flex;gap:10px;align-items:center;">
                <div style="width:36px;height:36px;background:#e3f2fd;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#1a73e8;font-size:14px;font-weight:700;flex-shrink:0;">&#x2B50;</div>
                <div>
                  <div style="font-size:13px;font-weight:700;color:#202124;">&#x1F31F; 星空観察 実行班</div>
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
              <div style="padding:10px 16px;border-bottom:1px solid #e0e0e0;font-size:13px;font-weight:700;color:#202124;display:flex;align-items:center;gap:8px;">
                <span>&#x1F4CC; 2025年度 ミーティング</span>
                <span style="font-size:11px;color:#9e9e9e;font-weight:400;">8名</span>
              </div>
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
                <input style="flex:1;border:1px solid #e0e0e0;border-radius:20px;padding:8px 14px;font-size:13px;font-family:inherit;outline:none;" placeholder="メッセージを入力..." readonly>
                <button style="background:#00c300;color:white;border:none;border-radius:50%;width:32px;height:32px;cursor:pointer;">&#x25B6;</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="annotation">
        <div class="annotation-circle" style="background:#00c300;">1</div>
        <div class="annotation-text"><strong>グループトーク</strong>: メンバー全体・係ごとなど複数のグループを作成可能。普段のLINEとは完全に分離できます。</div>
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
          <li>「管理者画面」からメンバーのメールアドレスを招待</li>
          <li>招待されたメンバーはスマホアプリをインストールしてログイン</li>
        </ol>
      </div>
      <div class="point-box">
        <div class="label">&#x1F4A1; フリープランでできること</div>
        メッセージ送受信・グループトーク・ファイル共有（1GB）・カレンダー共有・アンケート機能など、PTAの日常業務に必要な機能はほぼ無料で使えます。
      </div>
      <div class="warn-box">
        <div class="label">&#x26A0;&#xFE0F; 個人LINEとは別物です</div>
        LINE WORKSは普段のLINEとは別のアプリです。メンバーのプライベートLINEアカウントに連絡が届くことはなく、業務と私生活をきっちり分離できます。
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
        GoogleスプレッドシートはExcelのオンライン版です。<strong>メンバー名簿・会計帳簿・イベント進捗表など、PTAの管理業務に必須の表計算</strong>をクラウド上で管理できます。Googleフォームの回答が自動的にスプレッドシートに集まるため、集計の手間がゼロになります。
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
            <div style="width:28px;height:28px;background:linear-gradient(135deg,#1b5e20,#43a047);border-radius:4px;display:flex;align-items:center;justify-content:center;">
              <span style="color:white;font-size:14px;font-weight:700;">S</span>
            </div>
            <div>
              <div style="font-size:14px;color:#202124;font-weight:500;">2025年度PTA 管理シート</div>
              <div style="font-size:10px;color:#5f6368;">&#x2601;&#xFE0F; 保存済み</div>
            </div>
          </div>
          <div style="background:white;border-bottom:1px solid #e0e0e0;padding:4px 16px;display:flex;gap:16px;font-size:12px;color:#5f6368;">
            <span>ファイル</span><span>編集</span><span>表示</span><span>挿入</span><span>書式</span><span style="color:#43a047;font-weight:700;">データ</span>
          </div>
          <div style="background:#f8f9fc;border-bottom:1px solid #e0e0e0;padding:0 16px;display:flex;gap:0;overflow-x:auto;">
            <div style="padding:8px 16px;font-size:12px;background:white;border:1px solid #e0e0e0;border-bottom:none;border-radius:4px 4px 0 0;color:#43a047;font-weight:700;white-space:nowrap;">&#x1F465; メンバー名簿</div>
            <div style="padding:8px 16px;font-size:12px;color:#5f6368;white-space:nowrap;">&#x1F4B0; 会計</div>
            <div style="padding:8px 16px;font-size:12px;color:#5f6368;white-space:nowrap;">&#x1F31F; イベント進捗</div>
            <div style="padding:8px 16px;font-size:12px;color:#5f6368;white-space:nowrap;">&#x1F4CA; フォーム回答</div>
            <div style="padding:6px 12px;font-size:12px;color:#9e9e9e;">&#xFF0B;</div>
          </div>
          <div style="overflow-x:auto;">
            <table style="width:100%;border-collapse:collapse;font-size:12px;">
              <thead>
                <tr>
                  <th style="padding:8px 12px;border:1px solid #c8e6c9;text-align:center;background:#43a047;color:white;">お名前</th>
                  <th style="padding:8px 12px;border:1px solid #c8e6c9;text-align:left;background:#43a047;color:white;">担当</th>
                  <th style="padding:8px 12px;border:1px solid #c8e6c9;text-align:left;background:#43a047;color:white;">学年</th>
                  <th style="padding:8px 12px;border:1px solid #c8e6c9;text-align:left;background:#43a047;color:white;">連絡先(Gmail)</th>
                  <th style="padding:8px 12px;border:1px solid #c8e6c9;text-align:left;background:#43a047;color:white;">備考</th>
                </tr>
              </thead>
              <tbody>
                <tr style="background:#f1f8e9;">
                  <td style="padding:6px 12px;border:1px solid #dcedc8;font-weight:700;">田中 花子</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"><span style="background:#e8f5e9;color:#2e7d32;border-radius:4px;padding:2px 8px;font-size:11px;">会長</span></td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;">3年</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;color:#1a73e8;">hanako@xxx.com</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"></td>
                </tr>
                <tr>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;font-weight:700;">山田 太郎</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"><span style="background:#e3f2fd;color:#1565c0;border-radius:4px;padding:2px 8px;font-size:11px;">副会長</span></td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;">5年</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;color:#1a73e8;">taro@xxx.com</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"></td>
                </tr>
                <tr style="background:#f1f8e9;">
                  <td style="padding:6px 12px;border:1px solid #dcedc8;font-weight:700;">鈴木 良子</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"><span style="background:#fff8e1;color:#f57f17;border-radius:4px;padding:2px 8px;font-size:11px;">会計</span></td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;">1年</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;color:#1a73e8;">yoshiko@xxx.com</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;">経理経験あり</td>
                </tr>
                <tr>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;font-weight:700;">佐藤 祐一</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"><span style="background:#fce4ec;color:#c62828;border-radius:4px;padding:2px 8px;font-size:11px;">書記</span></td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;">2年</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;color:#1a73e8;">yuichi@xxx.com</td>
                  <td style="padding:6px 12px;border:1px solid #dcedc8;"></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <div class="annotation">
        <div class="annotation-circle" style="background:#43a047;">&#x1F4A1;</div>
        <div class="annotation-text">シートを複数タブに分けると管理が楽です。<strong>「メンバー名簿」「会計」「イベント進捗」「フォーム回答」</strong>の4シートで一本化するのがおすすめです。</div>
      </div>

      <div class="point-box">
        <div class="label">&#x1F4A1; おすすめのシート構成</div>
        <table style="width:100%;border-collapse:collapse;margin-top:8px;font-size:13px;">
          <tr><th style="text-align:left;padding:6px 8px;background:#f5f5f5;border:1px solid #e0e0e0;">シート名</th><th style="text-align:left;padding:6px 8px;background:#f5f5f5;border:1px solid #e0e0e0;">管理する内容</th></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">&#x1F465; メンバー名簿</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">氏名・担当・学年・連絡先</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">&#x1F4B0; 会計</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">収支・領収書番号・残高（SUM関数で自動計算）</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">&#x1F31F; イベント進捗</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">準備タスク・担当者・期限・完了チェックボックス</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">&#x1F4CA; フォーム回答</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">Googleフォームから自動で流れ込む回答データ</td></tr>
        </table>
      </div>
      <div class="point-box">
        <div class="label">&#x1F4A1; Googleフォームと連携するには？</div>
        フォームの「回答」タブ &#x2192; 「&#x1F4CA; スプレッドシートで表示」を押すだけ。回答が届くたびに自動でシートに追記されます。集計グラフも自動生成されます。
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
        <p>学校に行かなくてもいい。自宅から5分で会議</p>
      </div>
    </div>
    <div class="step-body">
      <div class="instruction-text">
        Google Meetは、Googleが提供する無料のビデオ会議ツールです。<strong>Gmailアカウントがあれば今すぐ使えます</strong>。会議・打ち合わせを完全オンラインにするだけで、「子どものお迎えがある」「仕事が終わらない」といった参加ハードルが一気に下がります。星空観察イベントの事前打ち合わせにも最適です。
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
            <div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:4px;padding:8px;background:#202124;">
              <div style="background:#3c4043;border-radius:8px;padding:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;min-height:100px;">
                <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#1a73e8,#4285f4);display:flex;align-items:center;justify-content:center;color:white;font-size:20px;font-weight:700;">田</div>
                <div style="color:white;font-size:12px;">田中さん（会長）</div>
                <span style="background:rgba(255,255,255,0.1);border-radius:4px;padding:2px 8px;font-size:10px;color:rgba(255,255,255,0.7);">&#x1F399;&#xFE0F; 話し中</span>
              </div>
              <div style="background:#3c4043;border-radius:8px;padding:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;min-height:100px;">
                <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,#e91e63,#f06292);display:flex;align-items:center;justify-content:center;color:white;font-size:20px;font-weight:700;">山</div>
                <div style="color:white;font-size:12px;">山田さん</div>
                <span style="background:rgba(255,87,34,0.3);border-radius:4px;padding:2px 8px;font-size:10px;color:#ff7043;">&#x1F507; ミュート中</span>
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
              <button style="width:44px;height:44px;border-radius:50%;background:#ea4335;border:none;color:white;font-size:18px;cursor:pointer;">&#x1F399;&#xFE0F;</button>
              <button style="width:44px;height:44px;border-radius:50%;background:#5f6368;border:none;color:white;font-size:18px;cursor:pointer;">&#x1F4F9;</button>
              <button style="width:44px;height:44px;border-radius:50%;background:#5f6368;border:none;color:white;font-size:18px;cursor:pointer;">&#x1F4CB;</button>
              <button style="width:44px;height:44px;border-radius:50%;background:#5f6368;border:none;color:white;font-size:18px;cursor:pointer;">&#x1F4AC;</button>
              <button style="width:44px;height:44px;border-radius:50%;background:#ea4335;border:none;color:white;font-size:18px;cursor:pointer;">&#x1F4F5;</button>
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
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">会議（月1回）</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">全員オンラインで30分以内に終わらせる</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">イベント打ち合わせ</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">スプレッドシート進捗表を画面共有しながら確認</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">急ぎの相談</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">LINE WORKSでリンクを送り、即席でMeet開始</td></tr>
          <tr><td style="padding:6px 8px;border:1px solid #e0e0e0;">新メンバーへの引き継ぎ</td><td style="padding:6px 8px;border:1px solid #e0e0e0;">画面共有しながら操作説明を録画して保存</td></tr>
        </table>
      </div>
      <div class="point-box">
        <div class="label">&#x1F4A1; 無料で使える時間は？</div>
        Googleアカウントがあれば、<strong>1対1の会議は無制限</strong>、3人以上も<strong>60分まで無料</strong>（2024年現在）。PTAの会議（30分程度）なら問題なく無料で使えます。
      </div>
    </div>
  </section>

"""

import sys

filepath = r'f:\Antigravity\ニュースを自動で収集\pta-guide\index.html'

with open(filepath, 'rb') as f:
    raw = f.read()

if raw[:3] == b'\xef\xbb\xbf':
    content = raw[3:].decode('utf-8')
else:
    content = raw.decode('utf-8')

# 完了バナーの直前に挿入
if FINISH_MARKER in content:
    content = content.replace(FINISH_MARKER, NEW_SECTIONS + FINISH_MARKER, 1)
    print("Inserted before finish banner")
else:
    print("ERROR: finish marker not found!")
    print("Looking for alternatives...")
    idx = content.find('finish-banner')
    print(f"'finish-banner' found at: {idx}")
    sys.exit(1)

# ナビバーにリンク追加（重複しないよう確認してから）
NAV_LINK_DRIVE = '<a href="#step-drive">&#x1F4C1; &#x30C9;&#x30E9;&#x30A4;&#x30D6;</a>'
NAV_LINK_NEW = '''<a href="#step-lineworks">&#x1F4AC; LINE WORKS</a>
    <a href="#step-sheets">&#x1F4CA; &#x30B9;&#x30D7;&#x30EC;&#x30C3;&#x30C9;</a>
    <a href="#step-meet">&#x1F4F9; Meet</a>'''

# 現在のナビを探す
if 'step-lineworks' not in content:
    # ドライブのナビリンクを探して後ろに追加
    # 様々なパターンを試す
    nav_patterns = [
        '>&#x1F4C1; &#x30C9;&#x30E9;&#x30A4;&#x30D6;</a>',
        '>📁 ドライブ</a>',
        'step-drive">',
    ]
    added = False
    for pat in nav_patterns:
        if pat in content:
            idx = content.find(pat)
            end_idx = content.find('</a>', idx) + 4
            before = content[:end_idx]
            after = content[end_idx:]
            content = before + '\n    <a href="#step-lineworks">&#x1F4AC; LINE WORKS</a>\n    <a href="#step-sheets">&#x1F4CA; スプレッド</a>\n    <a href="#step-meet">&#x1F4F9; Meet</a>' + after
            print(f"Added nav links after pattern: {pat}")
            added = True
            break
    if not added:
        print("WARNING: Could not find nav link insertion point")
else:
    print("Nav links already exist")

# 完了バナーのテキストを更新
old_banner_text = 'フォーム・ドキュメント・ドライブの3つを使いこなせば、'
new_banner_text = 'フォーム・ドキュメント・ドライブ・LINE WORKS・スプレッドシート・Meetを使いこなせば、'
if old_banner_text in content:
    content = content.replace(old_banner_text, new_banner_text)
    print("Updated finish banner text")

# BOM付きUTF-8で書き出す
with open(filepath, 'wb') as f:
    f.write(b'\xef\xbb\xbf')
    f.write(content.encode('utf-8'))

# 確認
print(f"\nFile saved. Total length: {len(content)}")
with open(filepath, 'rb') as f:
    check = f.read()
check_content = check[3:].decode('utf-8')
print(f"step-lineworks: {'step-lineworks' in check_content}")
print(f"step-sheets: {'step-sheets' in check_content}")
print(f"step-meet: {'step-meet' in check_content}")
t_s = check_content.find('<title>')
t_e = check_content.find('</title>')
print(f"Title: {check_content[t_s:t_e+8]}")
