import streamlit as st
from PIL import Image
import io

# ==========================================
# 1. 視覺風格庫 (10 大旗艦風格：全細節回歸)
# ==========================================
STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {"theme": "Consumer TRENDS", "ui": "Organic shapes, Frosted glass", "palette": "Beige, Blue, Red", "highlight_color": "Vibrant Sunburst Orange", "header_style": "Bold Modern"},
    "社會案件 (Justice Alert)": {"theme": "Crime Scene Noir", "ui": "CCTV grain, Map overlays", "palette": "Grey, Yellow, Police Blue", "highlight_color": "Safety Orange", "header_style": "Impact Industrial"},
    "體育競技 (Victory Orange)": {"theme": "Sports High-Energy", "ui": "Carbon fiber, Speed lines", "palette": "Orange, Graphite", "highlight_color": "Vivid Neon Yellow", "header_style": "Italic Dynamic"},
    "全球財經 (Elite Obsidian)": {"theme": "Financial Dashboard", "ui": "Aluminum, Data streams", "palette": "Navy, Gold, Cyan", "highlight_color": "Electric Cyan", "header_style": "Luxury Serif"},
    "突發重磅 (Breaking Alert)": {"theme": "Emergency Crimson", "ui": "Radial Blur, Red glow", "palette": "Signal Red, White, Black", "highlight_color": "Bright Vivid Yellow", "header_style": "Ultra-Bold"},
    "選情政論 (Democracy Grey)": {"theme": "Political Studio", "ui": "Matte Metallic, Star patterns", "palette": "Slate Grey, Navy, Crimson", "highlight_color": "Vibrant Scarlet Red", "header_style": "Classic Formal"},
    "科技政策 (Cyber Policy)": {"theme": "Digital Hub", "ui": "Poly-grid, Frosted glass", "palette": "Steel Blue, Cyan, Silver", "highlight_color": "Neon Lime Green", "header_style": "Cybernetic"},
    "綠能永續 (Eco-Future)": {"theme": "Sustainability", "ui": "Natural textures, Bokeh", "palette": "Emerald Green, Leaf Green, White", "highlight_color": "Sunlight Gold", "header_style": "Clean Eco"},
    "現代民俗 (Modern Festive)": {"theme": "Modern Folk", "ui": "Lacquered Wood, Silk", "palette": "Vermilion Red, Gold, Charcoal", "highlight_color": "Imperial Gold", "header_style": "Traditional Elegant"},
    "生醫科技 (Clinical White)": {"theme": "Bio-Tech", "ui": "Clinical surfaces, DNA helix", "palette": "Pristine White, Sky Blue, Navy", "highlight_color": "Bright Sky Blue", "header_style": "Minimalist Prof"}
}

# 物理框架規格 (1/2/3 多圖配置)
LAYOUT_SPECS = {
    1: [{"pos": (451, 142), "size": (1018, 708)}],
    2: [{"pos": (120, 200), "size": (800, 550)}, {"pos": (1000, 200), "size": (800, 550)}],
    3: [{"pos": (50, 250), "size": (580, 450)}, {"pos": (670, 250), "size": (580, 450)}, {"pos": (1290, 250), "size": (580, 450)}]
}

# ==========================================
# 2. 核心邏輯：AI 指令組裝 (保留所有遺失細節)
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, layout, icon_style, has_image=False):
    style = STYLE_CONFIG[style_name]
    ticker_void = "[ABSOLUTE VOID] Bottom-Right ($588 x 90$ px) for Ticker. Content must NOT overlap."
    pixel_lock = "[ULTIMATE PIXEL LOCK] RAW PHYSICAL MATTER. NO REDRAWING. HARD-COMPOSITE ONLY." if has_image else ""
    
    symbol_matrix = f"""
[SYMBOL MATRIX]
1. Quotes: {style['highlight_color']}, REMOVE symbols.
2. Brackets: Blue Block, REMOVE symbols.
3. Parentheses: KEEP exactly.
"""
    return f"""
[SYSTEM V8.7] CANVAS: 1920x1080 (16:9). {ticker_void}
{pixel_lock} {symbol_matrix}
STYLE: {style_name} | THEME: {style['theme']} | UI: {style['ui']} | PALETTE: {style['palette']}
LAYOUT: {layout} | ICON: {icon_style}
[CONTENT] TITLE: {title} | DATA_A: {left_in} | DATA_B: {right_in}
[STRICT] Traditional Chinese. No pose alteration. Background blends into ticker zone.
"""

# ==========================================
# 3. Streamlit 介面 (疊加優化布局)
# ==========================================
st.set_page_config(page_title="Visual Director v8.7", layout="wide")
st.title("🎬 Visual Director v8.7 - 旗艦功能全回歸版")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    # --- 原本功能：文字內容區 ---
    st.subheader("📋 1. 新聞文字資產")
    title_in = st.text_input("新聞主標", placeholder="輸入標題...")
    c_a, c_b = st.columns(2)
    with c_a: left_in = st.text_area("區塊 A 內文", height=100)
    with c_b: right_in = st.text_area("區塊 B 補充", height=100)
    
    # --- 新增功能：多圖焦點處理 (疊加預覽) ---
    st.divider()
    st.subheader("📸 2. 照片焦點處理 (多圖支援)")
    uploaded_photos = st.file_uploader("上傳新聞照片 (可多選)", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    processed_assets = []
    if uploaded_photos:
        photo_count = len(uploaded_photos)
        for idx, file in enumerate(uploaded_photos):
            with st.expander(f"焦點調整：照片 {idx+1}", expanded=(idx==0)):
                raw_img = Image.open(file).convert("RGB")
                w, h = raw_img.size
                
                s1, s2, s3 = st.columns(3)
                with s1: z = st.slider(f"縮放 {idx+1}", 0.1, 2.0, 1.0, key=f"z{idx}")
                with s2: ox = st.slider(f"X 中心 {idx+1}", 0, w, w//2, key=f"x{idx}")
                with s3: oy = st.slider(f"Y 中心 {idx+1}", 0, h, h//2, key=f"y{idx}")
                
                # 計算裁切與預覽 (根據多圖配置自動適配框架尺寸)
                current_spec = LAYOUT_SPECS.get(photo_count, LAYOUT_SPECS[1])[min(idx, 2)]
                tw, th = current_spec['size']
                cw, ch = int(tw * z), int(th * z)
                box = (max(0, ox-cw//2), max(0, oy-ch//2), min(w, ox+cw//2), min(h, oy+ch//2))
                
                preview_img = raw_img.crop(box).resize((tw, th), Image.Resampling.LANCZOS)
                st.image(preview_img, caption=f"預視圖 {idx+1}", use_column_width=True)
                processed_assets.append({'img': preview_img, 'pos': current_spec['pos']})

    # --- 原本功能：規格與風格 ---
    st.divider()
    st.subheader("🛠️ 3. 視覺規格設定")
    s_style = st.selectbox("視覺風格庫 (10 大清單已回歸)", list(STYLE_CONFIG.keys()))
    r1, r2 = st.columns(2)
    with r1: s_layout = st.radio("排版模式", ["固定網格 (GRID)", "動態流動 (DYNAMIC)"])
    with r2: s_icon = st.radio("物件質感", ["2D 簡約 (Flat)", "3D 立體 (Volumetric)"])

with col_out:
    # --- 生指令區 ---
    st.subheader("🚀 第一產出：AI 繪圖指令")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, s_layout, s_icon, has_image=(len(uploaded_photos) > 0))
        st.error("🚨 588x90 避讓與像素鎖定已鎖死")
        st.code(final_cmd, language="markdown")
    
    # --- 物理合成區 (一鍵出成品) ---
    st.divider()
    st.subheader("🔥 第二產出：物理硬合成成品")
    bg_file = st.file_uploader("📥 上傳 AI 生成的背景圖 (1920x1080)", type=["png", "jpg"])
    
    if bg_file and processed_assets:
        if st.button("執行硬合成並預覽成品"):
            bg_img = Image.open(bg_file).convert("RGBA")
            # 物理貼合邏輯
            for asset in processed_assets:
                bg_img.paste(asset['img'].convert("RGBA"), asset['pos'], asset['img'].convert("RGBA"))
            
            st.image(bg_img, caption="最終成品 (照片 100% 真實)", use_column_width=True)
            
            # 提供下載
            buf = io.BytesIO()
            bg_img.save(buf, format="PNG")
            st.download_button("💾 下載 1920x1080 成品圖", data=buf.getvalue(), file_name="CTS_News_CG.png", mime="image/png")
    else:
        st.info("上傳背景圖與照片即可生成最終成品。")
