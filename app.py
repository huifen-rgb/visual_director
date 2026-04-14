import streamlit as st
from PIL import Image

# ==========================================
# 1. 視覺風格庫 (10 大旗艦風格：完整美學參數)
# ==========================================
# 拒絕簡化，保留所有細節描述，確保 AI 抓得到質感
STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {
        "theme": "Consumer TRENDS, Fluid & Advanced",
        "ui": "Smooth organic shapes background, Gradational color overlays, Frosted glass panels",
        "palette": "Soft Beige, Lifestyle Blue, Clear Red",
        "highlight_color": "Vibrant Sunburst Orange",
        "header_style": "Bold Modern Sans-serif"
    },
    "社會案件 (Justice Alert)": {
        "theme": "Crime Scene Noir, Legal Justice",
        "ui": "CCTV grain effects, Map data overlays, Forensic lighting textures",
        "palette": "Concrete Grey, Caution Yellow, Police Blue",
        "highlight_color": "Safety Orange",
        "header_style": "Impact Industrial"
    },
    "體育競技 (Victory Orange)": {
        "theme": "High-Energy Sports Broadcast",
        "ui": "Carbon fiber textures, Kinetic speed lines, Motion-blurred stadium spotlights",
        "palette": "Electric Orange, Graphite Grey, Stark White",
        "highlight_color": "Vivid Neon Yellow",
        "header_style": "Italic Dynamic Sans"
    },
    "全球財經 (Elite Obsidian)": {
        "theme": "High-end Financial Dashboard",
        "ui": "Anodized Aluminum frames, Holographic data streams, Glass refractions",
        "palette": "Deep Navy, Gold, Cyan Data Lines",
        "highlight_color": "Electric Cyan",
        "header_style": "Luxury Serif"
    },
    "突發重磅 (Breaking Alert)": {
        "theme": "Emergency Alert, High-Gloss Crimson",
        "ui": "Radial Motion Blur, Glassy UI panels with Red internal glow, High-speed light streaks",
        "palette": "Signal Red, Stark White, Pure Black",
        "highlight_color": "Bright Vivid Yellow",
        "header_style": "Ultra-Bold Heavy"
    },
    "選情政論 (Democracy Grey)": {
        "theme": "Political Election Studio",
        "ui": "Matte Metallic surfaces, Subtle star patterns, Studio spotlighting, Polished marble textures",
        "palette": "Slate Grey, Navy Blue, Crimson",
        "highlight_color": "Vibrant Scarlet Red",
        "header_style": "Classic Formal Sans"
    },
    "科技政策 (Cyber Policy)": {
        "theme": "Digital Policy Hub",
        "ui": "Poly-grid overlays, Ray-traced refraction, Semi-transparent frosted glass, Circuit patterns",
        "palette": "Steel Blue, Neon Cyan, Silver",
        "highlight_color": "Neon Lime Green",
        "header_style": "Cybernetic Monospace"
    },
    "綠能永續 (Eco-Future)": {
        "theme": "Sustainability & ESG",
        "ui": "Natural leaf textures, Soft-focus outdoor bokeh, Organic glass shapes, Solar panel patterns",
        "palette": "Emerald Green, Leaf Green, Soft White",
        "highlight_color": "Sunlight Gold",
        "header_style": "Clean Eco Sans"
    },
    "現代民俗 (Modern Festive)": {
        "theme": "Modern Folk, Rich Vermilion",
        "ui": "Lacquered Wood finish, Silk texture, Traditional cloud patterns, Paper lantern glow",
        "palette": "Vermilion Red, Gold, Deep Charcoal",
        "highlight_color": "Imperial Gold",
        "header_style": "Traditional Elegant Calligraphy-style Sans"
    },
    "生醫科技 (Clinical White)": {
        "theme": "Medical & Bio-Tech",
        "ui": "Sanitized clinical surfaces, DNA helix motifs, Soft internal light-diffuse, Hexagonal grid",
        "palette": "Pristine White, Sky Blue, Navy",
        "highlight_color": "Bright Sky Blue",
        "header_style": "Minimalist Professional"
    }
}

# 物理框架與避讓規格 (絕對數值)
FRAME_W, FRAME_H = 1018, 708
FRAME_POS = (451, 142)
TICKER_X, TICKER_Y = 1332, 990
TICKER_W, TICKER_H = 588, 90

# ==========================================
# 2. 指令組裝引擎 (權重疊加，拒絕簡化)
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, layout, icon_style, has_image=False):
    style = STYLE_CONFIG[style_name]
    
    # 權重 1: 播出安全區域 (Ticker Zone)
    TICKER_ZONE_MANDATE = f"""
[ABSOLUTE CONTENT EXCLUSION: TICKER ZONE]
- AREA: Bottom-Right corner (X > {TICKER_X}, Y > {TICKER_Y}).
- DIMENSION: {TICKER_W} x {TICKER_H} px.
- RULE: No text, no icons, no primary photos. This is a SACRED VOID for the TV Ticker.
- VISUAL: Background design must blend naturally, but content MUST NOT overlap.
"""

    # 權重 2: 像素級物理鎖定 (Immutable Asset)
    asset_protocol = ""
    if has_image:
        asset_protocol = f"""
[ULTIMATE PIXEL LOCK: NEWS INTEGRITY]
- UPLOADED FILE: This is RAW PHYSICAL MATTER. NO REDRAWING.
- HARD-COMPOSITE: Place original pixels EXACTLY into the frame at {FRAME_POS}.
- NO HALLUCINATION: If people's poses or faces change, it is a broadcast failure.
"""

    # 權重 3: 符號轉換矩陣 (全邏輯)
    SYMBOL_PROTOCOL = f"""
[SYMBOL TRANSFORMATION MATRIX]
1. QUOTE RULE (" "): Change text color to {style['highlight_color']}. REMOVE quotes from final render.
2. BRACKET RULE (【 】): Place text on a Deep Blue Color Block. REMOVE brackets.
3. PARENTHESES RULE (( )): KEEP text AND parentheses.
"""

    # 權重 4: 風格細節映射
    return f"""
[SYSTEM V8.5: FULL BROADCAST MASTER CONTROL]
CANVAS: Fixed 1920x1080 (16:9). 
{TICKER_ZONE_MANDATE}
{asset_protocol}
{SYMBOL_PROTOCOL}

[AESTHETIC: {style_name}]
- THEME: {style['theme']}
- UI ELEMENTS: {style['ui']}
- PALETTE: {style['palette']}
- HEADER FONT: {style['header_style']}

[SPECIFICATIONS]
- LAYOUT_MODE: {layout}
- ICON_TEXTURE: {icon_style}

[CONTENT DATA]
- MAIN_TITLE: {title}
- DATA_BLOCK_A: {left_in}
- DATA_BLOCK_B: {right_in}

[STRICT_GUARDRAILS]
- RENDER TRADITIONAL CHINESE ONLY.
- REMOVE technial labels like [圖] or [效果].
- Ensure physical realism of assets. 16:9 ratio is non-negotiable.
"""

# ==========================================
# 3. Streamlit 介面 (功能全數疊加，不求簡潔)
# ==========================================
st.set_page_config(page_title="Visual Director v8.5", layout="wide")
st.title("🎬 Visual Director v8.5 - 旗艦全規格版")
st.caption("Producer Huifen Edition | 新聞真實性與避讓規格絕對鎖死")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    # --- A. 內容編輯層 ---
    st.subheader("📋 1. 新聞內容輸入")
    title_in = st.text_input("新聞主標 (高亮將自動套用)", placeholder="輸入主標題...")
    c1, c2 = st.columns(2)
    with c1: left_in = st.text_area("區塊 A (內容)", height=120, placeholder="輸入主要內文...")
    with c2: right_in = st.text_area("區塊 B (補充)", height=120, placeholder="輸入補充數據...")
    
    # --- B. 資產與焦點裁切層 ---
    st.divider()
    st.subheader("📸 2. 照片資產與焦點處理")
    uploaded_file = st.file_uploader("上傳原始照片 (將執行像素鎖定)", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        raw_img = Image.open(uploaded_file).convert("RGB")
        w, h = raw_img.size
        st.info("🔍 調整下方滑桿，確保元首臉部位於 1018x708 框架中心")
        
        sl1, sl2, sl3 = st.columns(3)
        with sl1: zoom = st.slider("縮放倍率", 0.1, 2.0, 1.0)
        with sl2: off_x = st.slider("左右位置", 0, w, w//2)
        with sl3: off_y = st.slider("上下位置", 0, h, h//2)
        
        # 實時裁切預覽邏輯
        cw, ch = int(FRAME_W * zoom), int(FRAME_H * zoom)
        left, top = max(0, off_x - cw//2), max(0, off_y - ch//2)
        crop_box = (left, top, min(w, left + cw), min(h, top + ch))
        
        st.markdown("---")
        st.caption("✅ 預計硬貼合之焦點視窗 (1018x708)：")
        preview = raw_img.crop(crop_box).resize((FRAME_W, FRAME_H), Image.Resampling.LANCZOS)
        st.image(preview, caption="最終硬貼合效果預覽", use_column_width=True)

    # --- C. 規格與風格層 ---
    st.divider()
    st.subheader("🛠️ 3. 視覺規格設定")
    s_style = st.selectbox("視覺風格庫 (完整參數載入)", list(STYLE_CONFIG.keys()))
    
    r1, r2 = st.columns(2)
    with r1: s_layout = st.radio("排版佈局模式", ["固定網格 (GRID)", "動態流動 (DYNAMIC)"])
    with r2: s_icon = st.radio("物件質感規格", ["2D 簡約 (Flat)", "3D 立體 (Volumetric)"])

with col_out:
    st.subheader("🚀 最終 AI 生成指令 (全規格封裝)")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, s_layout, s_icon, has_image=(uploaded_file is not None))
        
        st.error("🚨 588x90 避讓、物理鎖定、符號矩陣已全數強制執行")
        st.code(final_cmd, language="markdown")
        
        with st.expander("📝 製作人校閱清單", expanded=True):
            st.markdown(f"""
            - **內文狀態**：標題、A、B 欄位全數編入。
            - **避讓區鎖定**：右下角 $588 \\times 90$ px 淨空協定已掛載。
            - **資產保護**：{'照片像素鎖死，禁止重繪' if uploaded_file else 'AI 自由生成物件'}。
            - **風格參數**：{s_style} 完整描述已載入。
            """)
    else:
        st.info("請輸入標題開始生產 CG 指令。")
