
import os
import re

files_info = {
    'es/index.html': {
        'lang': 'es',
        'email': 'Correo Electrónico Profesional',
        'material': 'Material Principal',
        'vision': 'Visión del Proyecto',
        'upload': 'Subir Diseños / Referencias (Máx. 10MB)',
        'btn': 'Enviar Resumen del Proyecto',
        'select': 'Seleccione el Material de Interés',
        'ss': 'Acero Inoxidable (SUS304 / SUS316)',
        'silver': 'Plata de Ley 925 (S925)',
        'gold': 'Oro K Sólido (9K/14K/18K)',
        'thank_you': 'https://www.aizjewelry.com/es/thank-you.html',
        'placeholder_email': 'Correo Electrónico Profesional de Negocios',
        'placeholder_vision': 'Cuéntenos sobre su visión de marca y sus necesidades de producción por lotes...',
        'guarantee': 'Confidencialidad estricta garantizada. Evaluamos todas las consultas en un plazo de 12 horas.'
    },
    'fr/index.html': {
        'lang': 'fr',
        'email': 'E-mail Professionnel',
        'material': 'Matériau Principal',
        'vision': 'Vision du Projet',
        'upload': 'Télécharger Designs / Références (Max 10Mo)',
        'btn': 'Envoyer le Brief du Projet',
        'select': 'Sélectionner l\'intérêt pour le matériau',
        'ss': 'Acier Inoxydable (SUS304 / SUS316)',
        'silver': 'Argent Sterling 925 (S925)',
        'gold': 'Or K Massif (9K/14K/18K)',
        'thank_you': 'https://www.aizjewelry.com/fr/thank-you.html',
        'placeholder_email': 'E-mail professionnel',
        'placeholder_vision': 'Parlez-nous de votre vision de marque et de vos besoins de production...',
        'guarantee': 'Confidentialité stricte garantie. Nous évaluons toutes les demandes sous 12 heures.'
    },
    'de/index.html': {
        'lang': 'de',
        'email': 'Geschäftliche E-Mail',
        'material': 'Kernmaterial',
        'vision': 'Projektvision',
        'upload': 'Designs / Referenzen hochladen (Max. 10MB)',
        'btn': 'Projekt-Briefing senden',
        'select': 'Materialinteresse auswählen',
        'ss': 'Edelstahl (SUS304 / SUS316)',
        'silver': '925 Sterlingsilber (S925)',
        'gold': 'Massives K-Gold (9K/14K/18K)',
        'thank_you': 'https://www.aizjewelry.com/de/thank-you.html',
        'placeholder_email': 'Geschäftliche E-Mail-Adresse',
        'placeholder_vision': 'Erzählen Sie uns von Ihrer Markenvision und Ihrem Produktionsbedarf...',
        'guarantee': 'Strenge Vertraulichkeit garantiert. Wir prüfen alle Anfragen innerhalb von 12 Stunden.'
    },
    'pt/index.html': {
        'lang': 'pt',
        'email': 'E-mail Profissional',
        'material': 'Material Principal',
        'vision': 'Visão do Projeto',
        'upload': 'Carregar Designs / Referências (Máx. 10MB)',
        'btn': 'Enviar Resumo do Projeto',
        'select': 'Selecionar Interesse de Material',
        'ss': 'Aço Inoxidável (SUS304 / SUS316)',
        'silver': 'Prata de Lei 925 (S925)',
        'gold': 'Ouro K Sólido (9K/14K/18K)',
        'thank_you': 'https://www.aizjewelry.com/pt/thank-you.html',
        'placeholder_email': 'E-mail profissional de negócios',
        'placeholder_vision': 'Conte-nos sobre sua visão de marca e necessidades de produção...',
        'guarantee': 'Confidencialidade estrita garantida. Avaliamos todas as consultas em até 12 horas.'
    },
    'jp/index.html': {
        'lang': 'jp',
        'email': 'ビジネスメール',
        'material': '主要素材',
        'vision': 'プロジェクトのビジョン',
        'upload': 'デザイン/参考資料をアップロード (最大10MB)',
        'btn': 'プロジェクト概要を送信',
        'select': '素材を選択',
        'ss': 'ステンレス鋼 (SUS304 / SUS316)',
        'silver': '925スターリングシルバー (S925)',
        'gold': 'ソリッドKゴールド (9K/14K/18K)',
        'thank_you': 'https://www.aizjewelry.com/jp/thank-you.html',
        'placeholder_email': 'プロフェッショナルなビジネスメール',
        'placeholder_vision': 'ブランドのビジョンや生産ニーズについてお聞かせください...',
        'guarantee': '厳格な機密保持を保証します。すべての問い合わせを12時間以内に評価します。'
    },
    'kr/index.html': {
        'lang': 'kr',
        'email': '비즈니스 이메일',
        'material': '주요 소재',
        'vision': '프로젝트 비전',
        'upload': '디자인 / 참고 자료 업로드 (최대 10MB)',
        'btn': '프로젝트 브리프 전송',
        'select': '관심 소재 선택',
        'ss': '스테인리스 스틸 (SUS304 / SUS316)',
        'silver': '925 스털링 실버 (S925)',
        'gold': '솔리드 K-골드 (9K/14K/18K)',
        'thank_you': 'https://www.aizjewelry.com/kr/thank-you.html',
        'placeholder_email': '비즈니스 이메일 주소',
        'placeholder_vision': '귀하의 브랜드 비전과 생산 요구 사항에 대해 알려주세요...',
        'guarantee': '엄격한 기밀 유지를 보장합니다. 모든 문의는 12시간 이내에 검토됩니다.'
    }
}

base_path = 'E:/AizJewelry_Project'

for f_rel_path, info in files_info.items():
    f_path = os.path.join(base_path, f_rel_path)
    if not os.path.exists(f_path): continue
    
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the inquiry form block
    # We look for the start of the form section and replace until the end of the section
    pattern = r'<div class="inquiry-form">.*?</div>\s*</div>\s*</div>\s*</section>'
    
    new_form = f'''<form class="inquiry-form" action="https://formsubmit.co/sales@aizjewelry.com" method="POST" enctype="multipart/form-data" onsubmit="gtag('event', 'form_submission_web', {{'event_category': 'Inquiry', 'event_label': 'FormSubmit'}});">
                    <!-- FormSubmit Configuration -->
                    <input type="hidden" name="_next" value="{info['thank_you']}">
                    <input type="hidden" name="_subject" value="New Jewelry Project Inquiry - AizJewelry.com">
                    <input type="hidden" name="_template" value="table">
                    <input type="hidden" name="_captcha" value="false">

                    <div class="form-group">
                        <label>{info['email']}</label>
                        <input type="email" name="email" id="form-email" placeholder="{info['placeholder_email']}" required>
                    </div>
                    <div class="form-group">
                        <label>{info['material']}</label>
                        <select name="material" id="form-material" required>
                            <option value="">{info['select']}</option>
                            <option value="Stainless Steel">{info['ss']}</option>
                            <option value="925 Silver">{info['silver']}</option>
                            <option value="Solid K-Gold">{info['gold']}</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label>{info['vision']}</label>
                        <textarea name="message" id="form-message" placeholder="{info['placeholder_vision']}" rows="4" required></textarea>
                    </div>
                    <div class="form-group">
                        <label>{info['upload']}</label>
                        <input type="file" name="attachment" accept="image/*,.pdf,.doc,.docx" class="file-input">
                    </div>
                    <button type="submit" class="btn primary">{info['btn']}</button>
                    <p style="font-size: 0.7rem; color: #888; text-align: center; margin-top: 20px;">{info['guarantee']}</p>
                </form>
            </div>
        </div>
    </section>'''
    
    content = re.sub(pattern, new_form, content, flags=re.DOTALL)
    
    # Also remove the sendInquiry JS function
    js_pattern = r'// .*?\n\s*function sendInquiry\(\) {{.*?}}\n'
    content = re.sub(js_pattern, '', content, flags=re.DOTALL)
    
    # Update script source for root vs subfolder
    if '/' in f_rel_path:
        content = content.replace('<script src="script.js"></script>', '<script src="../script.js"></script>')
    
    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {{f_path}}")
