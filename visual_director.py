import streamlit as st

# ==========================================
# 1. 視覺風格庫 (10 大專業風格全回歸 - 絕無刪減)
# ==========================================
STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {
        "theme": "Consumer TRENDS, Fluid & Advanced",
        "ui": "Smooth organic shapes background, Gradational color overlays, Frosted glass panels",
        "palette": "Soft Beige, Lifestyle Blue, Clear Red",
        "highlight_color": "Vibrant Sunburst Orange",
        "layout_mode": "DYNAMIC"
    },
    "社會案件 (Justice Alert)": {
        "theme": "Crime Scene Noir, Legal Justice",
        "ui": "CCTV grain effects, Map data overlays, Forensic lighting textures",
        "palette": "Concrete Grey, Caution Yellow, Police Blue",
        "highlight_color": "Safety Orange",
        "layout_mode": "GRID"
    },
    "體育競技 (Victory Orange)": {
        "theme": "High-Energy Sports Broadcast",
        "ui": "Carbon fiber textures, Kinetic speed lines, Motion-blurred stadium spotlights",
        "palette": "Electric Orange, Graphite Grey, Stark White",
        "highlight_color": "Vivid Neon Yellow",
        "layout_mode": "GRID"
    },
    "全球財經 (Elite Obsidian)": {
        "theme": "High-end Financial Dashboard",
        "ui": "Anodized Aluminum frames, Holographic data streams, Glass refractions",
        "palette": "Deep Navy, Gold, Cyan Data Lines",
        "highlight_color": "Electric Cyan",
        "layout_mode": "GRID"
    },
    "突發重磅 (Breaking Alert)": {
        "theme": "Emergency Alert, High-Gloss Crimson",
        "ui": "Radial Motion Blur, Glassy UI panels with Red internal glow",
        "palette": "Signal Red, Stark White, Pure Black",
        "highlight_color": "Bright Vivid Yellow",
        "layout_mode": "GRID"
    },
    "選情政論 (Democracy Grey)": {
        "theme": "Political Election Studio",
        "ui": "Matte Metallic surfaces, Subtle star patterns, Studio spotlighting",
        "palette": "Slate Grey, Navy Blue, Crimson",
        "highlight_color": "Vibrant Scarlet Red",
        "layout_mode": "GRID"
    },
    "科技政策 (Cyber Policy)": {
        "theme": "Digital Policy Hub",
        "ui": "Poly-grid overlays, Ray-traced refraction, Semi-transparent frosted glass",
        "palette": "Steel Blue, Neon Cyan, Silver",
        "highlight_color": "Neon Lime Green",
        "layout_mode": "DYNAMIC"
    },
    "綠能永續 (Eco-Future)": {
        "theme": "Sustainability & ESG",
        "ui": "Natural leaf textures, Soft-focus outdoor bokeh, Organic glass shapes",
        "palette": "Emerald Green, Leaf Green, Soft White",
        "highlight_color": "Sunlight Gold",
        "layout_mode": "GRID"
    },
    "現代民俗 (Modern Festive)": {
        "theme": "Modern Folk, Rich Vermilion",
        "ui": "Lacquered Wood finish, Silk texture, Traditional cloud patterns",
        "palette": "Vermilion Red, Gold, Deep Charcoal",
        "highlight_color": "Imperial Gold",
        "layout_mode": "GRID"
    },
    "生醫科技 (Clinical White)": {
        "theme": "Medical & Bio-Tech",
        "ui": "Sanitized clinical surfaces, DNA helix motifs, Soft internal light-diffuse",
        "palette": "Pristine White, Sky Blue, Navy",
        "highlight_color": "Bright Sky Blue",
        "layout_mode": "DYNAMIC"
    }
}

# ==========================================
# 2. 核心組裝邏輯 (疊加暴力避讓與物理貼合)
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, layout_mode, icon_style):
    style = STYLE_CONFIG[style_name]
    
    # --- 暴力避讓：針對右下角 588x90 的死守 ---
    TICKER_ZONE_ENFORCEMENT = """
[CRITICAL SYSTEM ERROR PREVENTION: TICKER ZONE]
- VOID AREA: The bottom-right corner ($X > 1332, Y > 990$, $588 x 90$ px) MUST BE PURE EMPTY BACKGROUND.
- FORBIDDEN: Any text, icons, UI panels, or decorative elements touching this zone is a FAILURE.
- BROADCAST RULE: This space belongs to the TV Ticker. Do NOT render anything here.
"""

    # --- 物理資產鎖死：禁止重繪 ---
    ASSET_LOCK_PROTOCOL = """
[ULTIMATE ASSET PROTECTION]
- UPLOADED FILE: Treat as an "Immutable Physical Object".
- HARD-PASTING RULE: Use the EXACT pixels. Do NOT redraw, Do NOT morph, Do NOT "beautify".
- AUTHENTICITY: The realism of the uploaded asset is the top priority.
"""

    SYMBOL_PROTOCOL = f"""
[SYMBOL TRANSFORMATION MATRIX]
1. QUOTE RULE (" "): Text color to {style['highlight_color']}. REMOVE quotes.
2. BRACKET RULE (【 】): Text on Deep Blue Color Block. REMOVE brackets.
3. PARENTHESES RULE (( )): Keep text AND parentheses. NO change to color.
"""

    l_cmd = f"[LAYOUT: {layout_mode.upper()}] Ensure visual void in ticker zone."
    i_cmd = f"[ASSET: {icon_style.upper()}]"

    final_prompt = f"""
[SYSTEM PROTOCOL: BROADCAST GRAPHIC V7.1]
CANVAS: Fixed 1920x1080 (Strict 16:9).
{TICKER_ZONE_ENFORCEMENT}
{ASSET_LOCK_PROTOCOL}
{SYMBOL_PROTOCOL}
{l_cmd}
{i_cmd}

[AESTHETIC: {style_name}]
- THEME: {style['theme']} | UI: {style['ui']}
- HEADER: {style['header_style'] if 'header_style' in style else 'Bold Sans-serif'} | PALETTE: {style['palette']}

[CONTENT DATA]
- TITLE: {title}
- DATA_A: {left_in}
- DATA_B: {right_in}

[STRICT GUARDRAILS]
- RENDER TRADITIONAL CHINESE ONLY.
- REMOVE labels like [日曆效果] or [圖].
- Physical integration and 16:9 ratio are SUPREME. 
- Right-bottom void is non-negotiable.
"""
    return final_prompt

# ==========================================
# 3. Streamlit 介面
# ==========================================
st.set_page_config(page_title="Visual Director v7.1", layout="wide")
st.title("🎬 Visual Director v7.1 - 旗艦功能全回歸版")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📋 內容編輯區")
    title_in = st.text_input("新聞主標", placeholder='輸入主標題...')
    left_in = st.text_area("區塊 A (內容)", height=150)
    right_in = st.text_area("區塊 B (補充)", height=150)
    
    st.divider()
    st.subheader("🛠️ 視覺與硬體規格")
    s_style = st.selectbox("1. 選擇視覺風格", list(STYLE_CONFIG.keys()))
    
    c1, c2 = st.columns(2)
    with c1:
        s_layout = st.radio("2. 排版模式", ["固定網格 (Fixed Grid)", "動態流動 (Dynamic Flow)"])
    with c2:
        s_icon = st.radio("3. 物件質感", ["2D 簡約 (Flat)", "3D 立體 (Volumetric)"])

with col_out:
    st.subheader("🚀 生成之 AI 繪圖指令")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, s_layout, s_icon)
        st.success(f"已就緒：{s_style} 方案")
        st.code(final_cmd, language="markdown")
        
        with st.expander("✅ 製作人檢查清單 (Checklist)", expanded=True):
            st.markdown(f"""
            - **風格確認**：{s_style} 已加載。
            - **避讓區鎖死**：右下角 $588 \\times 90$ px 強制淨空。
            - **硬貼合啟動**：禁止 AI 對照片進行「二次創作」。
            - **高亮設定**："{title_in}" 將變為 **{STYLE_CONFIG[s_style]['highlight_color']}**。
            """)
    else:
        st.info("請輸入標題開始組裝。")
