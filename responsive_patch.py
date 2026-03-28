"""
responsive_patch.py
_css.txt にモバイルレスポンシブCSSを追加するパッチスクリプト
"""

RESPONSIVE_CSS = '''
        /* =============================================
           レスポンシブ対応 (スマホ・タブレット)
           ============================================= */

        /* --- タブレット (768px以下) --- */
        @media (max-width: 768px) {
            .hero {
                padding: 40px 16px 56px;
            }
            .hero h1 {
                font-size: 26px;
            }
            .hero-chips {
                gap: 6px;
            }
            .chip {
                font-size: 11px;
                padding: 4px 12px;
            }
            main {
                padding: 32px 16px !important;
            }
            .toc a {
                padding: 12px 12px;
                font-size: 12px;
                gap: 4px;
            }
            .step-number {
                width: 44px;
                height: 44px;
                font-size: 18px;
            }
            .step-title-group h2 {
                font-size: 18px;
            }
            .mockup-wrap {
                margin: 16px -4px;
            }
            .divider {
                margin: 32px 0;
            }
            .finish-banner {
                padding: 36px 20px;
            }
            .finish-banner h2 {
                font-size: 22px;
            }
            .point-box, .warn-box {
                font-size: 13px;
                padding: 12px 14px;
            }
            table {
                font-size: 12px;
            }
            td, th {
                padding: 6px 8px !important;
            }
        }

        /* --- スマホ (480px以下) --- */
        @media (max-width: 480px) {
            .hero {
                padding: 32px 16px 48px;
            }
            .hero h1 {
                font-size: 22px;
                line-height: 1.4;
            }
            .hero h1 span {
                font-size: 16px;
            }
            .hero p {
                font-size: 13px;
                margin-bottom: 20px;
            }
            .hero-badge {
                font-size: 11px;
                padding: 4px 14px;
                margin-bottom: 14px;
            }
            .hero-chips {
                flex-wrap: wrap;
                gap: 6px;
                justify-content: center;
            }
            .chip {
                font-size: 11px;
                padding: 4px 10px;
            }
            .toc-inner {
                gap: 0;
                padding: 0 4px;
            }
            .toc a {
                padding: 10px 10px;
                font-size: 11px;
                gap: 3px;
                white-space: nowrap;
            }
            .step-section {
                margin-bottom: 48px;
            }
            .step-header {
                gap: 12px;
                margin-bottom: 16px;
            }
            .step-number {
                width: 40px;
                height: 40px;
                font-size: 16px;
                flex-shrink: 0;
            }
            .step-title-group h2 {
                font-size: 17px;
                line-height: 1.3;
            }
            .step-title-group p {
                font-size: 12px;
            }
            .step-body {
                padding-left: 0;
            }
            .instruction-text {
                font-size: 14px;
                padding: 14px 16px;
            }
            .point-box, .warn-box {
                font-size: 12px;
                padding: 12px 14px;
                margin: 12px 0;
            }
            .annotation {
                gap: 10px;
                margin: 14px 0;
            }
            .annotation-circle {
                width: 24px;
                height: 24px;
                font-size: 11px;
                flex-shrink: 0;
            }
            .annotation-text {
                font-size: 13px;
            }
            .mockup-wrap {
                margin: 12px -4px;
                border-radius: 8px;
            }
            .browser-bar {
                padding: 6px 8px;
            }
            .address-bar {
                font-size: 10px;
                padding: 3px 8px;
            }
            .browser-content {
                overflow-x: auto;
            }
            table {
                font-size: 11px;
                min-width: 320px;
            }
            td, th {
                padding: 5px 6px !important;
            }
            .divider {
                margin: 28px 0;
            }
            .finish-banner {
                padding: 32px 16px;
                border-radius: 12px;
                margin-top: 24px;
            }
            .finish-banner h2 {
                font-size: 20px;
                margin-bottom: 10px;
            }
            .finish-banner p {
                font-size: 13px;
                line-height: 1.7;
            }
            .gf-body {
                padding: 20px 12px;
            }
            .gf-editor-body {
                padding: 16px 10px;
            }
            .form-card, .question-card, .response-summary {
                margin-left: 0;
                margin-right: 0;
            }
            .gf-send-modal {
                margin: 12px;
            }
            .intro-box {
                padding: 18px 16px;
                margin-bottom: 32px;
            }
            .intro-box h2 {
                font-size: 16px;
            }
            footer {
                padding: 24px 16px;
                font-size: 11px;
            }
        }

        /* --- 極小スマホ (360px以下) --- */
        @media (max-width: 360px) {
            .hero h1 {
                font-size: 19px;
            }
            .toc a {
                padding: 10px 8px;
                font-size: 10px;
            }
            .step-number {
                width: 36px;
                height: 36px;
                font-size: 14px;
            }
            .step-title-group h2 {
                font-size: 15px;
            }
        }

'''

p = r'f:\Antigravity\ニュースを自動で収集\pta-guide\_css.txt'
d = open(p, encoding='utf-8').read()

# Already patched?
if '@media (max-width: 768px)' in d:
    print('Already has responsive CSS, skipping.')
else:
    # Insert before </style>
    d = d.replace('    </style>', RESPONSIVE_CSS + '    </style>', 1)
    open(p, 'w', encoding='utf-8').write(d)
    print('Responsive CSS added successfully!')
    print(f'New file size: {len(d)} chars')
