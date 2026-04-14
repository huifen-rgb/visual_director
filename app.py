import streamlit as st
from PIL import Image, ImageDraw
from streamlit_cropper import st_cropper # 🛑 requirements.txt 必須包含此項
import io

# ==========================================
# 1. 視覺風格庫 (旗艦 10 大全規格：拒絕精簡，細節全數歸位)
# ==========================================
STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {"theme": "Consumer TRENDS, Fluid & Advanced", "ui": "Organic shapes, Frosted glass panels, Color overlays", "palette": "Soft Beige, Lifestyle Blue, Clear Red", "highlight": "Vibrant Sunburst Orange"},
    "社會案件 (Justice Alert)": {"theme": "Crime Scene Noir, Legal Justice", "ui": "CCTV grain, Map data overlays, Forensic lighting textures", "palette": "Concrete Grey, Caution Yellow, Police Blue", "highlight": "Safety Orange"},
    "體育競技 (Victory Orange)": {"theme": "High-Energy Sports Broadcast", "ui": "Carbon fiber textures, Kinetic speed lines, Stadium spotlights", "palette": "Electric Orange, Graphite Grey, Stark White", "highlight": "Vivid Neon Yellow"},
    "全球財經 (Elite Obsidian)": {"theme": "High-end Financial Dashboard", "ui": "Anodized Aluminum frames, Holographic streams, Glass refractions", "palette": "Deep Navy, Gold, Cyan Data Lines", "highlight": "Electric Cyan"},
    "突發重磅 (Breaking Alert)": {"theme": "Emergency Alert, High-Gloss Crimson", "ui": "Radial Motion Blur, Glassy UI panels, Red internal glow", "palette": "Signal Red, Stark White, Pure Black", "highlight": "Bright Vivid Yellow"},
    "選情政論 (Democracy Grey)": {"theme": "Political Election Studio", "ui": "Matte Metallic, Star patterns, Studio spotlighting, Marble textures", "palette": "Slate Grey, Navy Blue, Crimson", "highlight": "Vibrant Scarlet Red"},
    "科技政策 (Cyber Policy)": {"theme": "Digital Policy Hub", "ui": "Poly-grid overlays, Ray-traced refraction, Semi-transparent glass", "palette": "Steel Blue, Neon Cyan, Silver", "highlight": "Neon Lime Green"},
    "綠能永續 (Eco-Future)": {"theme": "Sustainability & ESG", "ui": "Natural leaf textures, Soft-focus outdoor bokeh, Organic glass", "palette": "Emerald Green, Leaf Green, Soft White", "highlight": "Sunlight Gold"},
    "現代民俗 (Modern Festive)": {"theme": "Modern Folk, Rich Vermilion", "ui": "Lacquered Wood finish, Silk texture, Traditional cloud patterns", "palette": "Vermilion Red, Gold, Deep Charcoal", "highlight": "Imperial Gold"},
    "生醫科技 (Clinical White)": {"theme": "Medical & Bio-Tech", "ui": "Sanitized clinical surfaces, DNA helix motifs, Hexagonal grid", "palette": "Pristine White, Sky Blue, Navy", "highlight": "Bright Sky Blue"}
}

# ==========================================
# 2. 核心組裝引擎 (符號矩陣、588x90 避讓、AI 主權)
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, layout, icon_style, ai_autonomy):
    style = STYLE_CONFIG[style_name]
    
    # 權重 1: 588x90 避讓區
    TICKER_VOID = "[ABSOLUTE VOID] Bottom-Right ($1332 < X < 1920$, $990 < Y < 1080$) for Ticker. No content."
    
    # 權重 2: 符號矩陣
    SYMBOL_MATRIX = f"""
[SYMBOL TRANSFORMATION]
1. Quotes (" "): Color per Highlight, REMOVE symbols.
2. Brackets (【 】): Deep Blue Block, REMOVE symbols.
3. Parentheses (( )): KEEP as is.
"""
    # 權重 3: AI 配色主權
    color_logic = f"AI_COLOR: Dynamic based on '{title}' sentiment." if ai_autonomy else f"FIXED: {style['palette']}, Highlight: {style['highlight']}"

    return f"""
[SYSTEM V9.9: FULL SPEC] CANVAS: 1920x1080. {TICKER_VOID}
{SYMBOL_MATRIX}
[ASSET LOCK] UPLOADED PHOTOS ARE RAW MATTER. NO REDRAWING POSES.
STYLE: {style_name} | THEME: {style['theme']} | UI: {style['ui']}
{color_logic} | LAYOUT: {layout} | ICON: {icon_style}
[CONTENT] TITLE: {title} | DATA_A: {left_in} | DATA_B: {right_in}
[STRICT] Traditional Chinese ONLY. High-end global tech-finance aesthetic.
"""

# ==========================================
# 3. Streamlit 介面 (全疊加布局)
# ==========================================
st.set_page_config(page_title="Visual Director v9.9", layout="wide")
st.title("🎬 Visual Director v9.9 - 旗艦全功能完全體")
st.caption("Producer Huifen Edition | 拒絕精簡，全規格疊加鎖定")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    # --- A. 底圖與文字資產 ---
    st.subheader("🖼️ 1. 底圖與文字資產")
    bg_ref_file = st.file_uploader("上傳 AI 生成的背景圖 (1920x1080)", type=["png", "jpg"])
    title_in = st.text_input("新聞主標 (AI 高亮對象)")
    c_a, c_b = st.columns(2)
    with c_a: left_in = st.text_area("區塊 A 內文", height=100)
    with c_b: right_in = st.text_area("區塊 B 補充", height=100)

    # --- B. 自由排版與視覺裁切 (重點疊加：手動調整 X/Y/W/H) ---
    st.divider()
    st.subheader("📸 2. 自由版面設計 (手動座標與拖曳)")
    uploaded_files = st.file_uploader("上傳欲硬合的照片 (支援 1-4 張)", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    processed_assets = []
    if uploaded_files:
        for idx, file in enumerate(uploaded_files):
            with st.expander(f"📍 配置照片 {idx+1}：座標與大小", expanded=(idx == 0)):
                # 手動座標與大小控制
                p1, p2, p3, p4 = st.columns(4)
                with p1: tx = st.number_input(f"X (左距)", 0, 1920, 451, key=f"tx{idx}")
                with p2: ty = st.number_input(f"Y (頂距)", 0, 1080, 250, key=f"ty{idx}")
                with p3: tw = st.number_input(f"寬度", 100, 1920, 800, key=f"tw{idx}")
                with p4: th = st.number_input(f"高度", 100, 1080, 500, key=f"th{idx}")

                raw_img = Image.open(file).convert("RGB")
                st.write("🔍 視覺化裁切焦點 (比例已隨寬高鎖定)：")
                
                # 🛑 視覺化拖曳裁切 (修復 aspect_ratio 報錯)
                cropped = st_cropper(raw_img, aspect_ratio=(tw, th), box_color='#FF0000', key=f"cr_{idx}")
                final_p = cropped.resize((tw, th), Image.Resampling.LANCZOS)
                
                # 即時襯底對位預覽
                if bg_ref_file:
                    bg_ref = Image.open(bg_ref_file).convert("RGBA")
                    mockup = bg_ref.copy()
                    draw = ImageDraw.Draw(mockup)
                    # 畫出物理框架邊界
                    draw.rectangle([tx, ty, tx+tw, ty+th], outline="#FF0000", width=4)
                    mockup.paste(final_p.convert("RGBA"), (tx, ty), final_p.convert("RGBA"))
                    st.image(mockup, caption=f"照片 {idx+1} 插入對位預覽", use_column_width=True)
                else:
                    st.image(final_p, caption=f"照片 {idx+1} 裁切結果", width=300)
                
                processed_assets.append({'img': final_p, 'pos': (tx, ty)})

with col_out:
    # --- C. 視覺規格 (保留不刪減) ---
    st.subheader("🛠️ 3. 視覺規格設定")
    s_style = st.selectbox("旗艦風格庫 (10 大清單)", list(STYLE_CONFIG.keys()))
    ai_sovereignty = st.toggle("✨ 啟動 AI 視覺主權 (自主配色)", value=True)
    r1, r2 = st.columns(2)
    with r1: s_layout = st.radio("排版佈局模式", ["GRID", "DYNAMIC"])
    with r2: s_icon = st.radio("物件質感選擇", ["Flat", "Volumetric"])

    st.divider()
    st.subheader("🚀 第一產出：AI 繪圖指令")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, s_layout, s_icon, ai_autonomy=ai_sovereignty)
        st.code(final_cmd, language="markdown")
    
    st.divider()
    st.subheader("🔥 第二產出：物理硬合成成品")
    if bg_ref_file and processed_assets:
        if st.button("執行最終硬合成並導出"):
            final_canvas = Image.open(bg_ref_file).convert("RGBA")
            for asset in processed_assets:
                # 執行像素級硬貼合
                final_canvas.paste(asset['img'].convert("RGBA"), asset['pos'], asset['img'].convert("RGBA"))
            
            st.image(final_canvas, use_column_width=True)
            buf = io.BytesIO()
            final_canvas.save(buf, format="PNG")
            st.download_button("💾 下載 1920x1080 成品圖", data=buf.getvalue(), file_name="Final_News_CG.png", mime="image/png")
    else:
        st.info("上傳背景圖與照片以開始合成。")
