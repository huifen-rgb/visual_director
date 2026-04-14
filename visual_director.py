import streamlit as st

# ==========================================
# 1. 視覺風格庫 (旗艦 8 大風格 - 數據流動美學優化)
# ==========================================
STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {
        "theme": "Consumer Livelihood TRENDS, Fluid & Advanced Daily Life",
        "ui": "Smoothly flowing organic shapes (blobs) background, Gradational color overlays, Ray-traced translucent frosted glass panels with subtle data flows behind panels",
        "header_style": "Friendly but Precise Rounded Sans-serif, Deep Blue",
        "palette": "Soft Beige gradients, Lifestyle Blue gradients, Clear Red accents",
        "highlight_color": "Sunburst Orange",
        "layout_mode": "DYNAMIC"
    },
    "社會案件 (Justice Alert)": {
        "theme": "Crime Scene Noir, Gritty Urban & Legal Justice",
        "ui": "Caution tape textures, CCTV grain effects, Map data overlays, Forensic lighting",
        "header_style": "Stencil Bold Typography with Danger Red glow",
        "palette": "Concrete Grey, Caution Yellow, Police Blue",
        "highlight_color": "Safety Orange",
        "layout_mode": "GRID"
    },
    "體育競技 (Victory Orange)": {
        "theme": "High-Energy Sports Broadcast, Dynamic Orange & Graphite",
        "ui": "Carbon fiber textures, Kinetic speed lines, Motion-blurred stadium spotlights",
        "header_style": "Italicized Impact Typography with Chrome finish",
        "palette": "Electric Orange, Graphite Grey, Stark White",
        "highlight_color": "Vivid Neon Yellow",
        "layout_mode": "GRID"
    },
    "全球財經 (Elite Obsidian)": {
        "theme": "High-end Financial Dashboard, Obsidian & Midnight Blue",
        "ui": "Anodized Aluminum frames, Holographic data streams, Ray-traced glass refractions",
        "header_style": "Metallic Platinum Gradient, Sharp slab-serif typography",
        "palette": "Deep Navy, Gold, Cyan Data Lines",
        "highlight_color": "Electric Cyan",
        "layout_mode": "GRID"
    },
    "突發重磅 (Breaking Alert)": {
        "theme": "Emergency Alert Aesthetic, High-Gloss Crimson & Pitch Black",
        "ui": "Radial Motion Blur, Glassy UI panels with Red internal glow Cinematic flare",
        "header_style": "Heavy Bold Sans-serif with White Stroke",
        "palette": "Signal Red, Stark White, Pure Black",
        "highlight_color": "Bright Vivid Yellow",
        "layout_mode": "GRID"
    },
    "選情政論 (Democracy Grey)": {
        "theme": "Political Election Studio, Slate Grey & Patriotic Blue/Red",
        "ui": "Matte Metallic surfaces, Subtle star patterns, Studio spotlighting",
        "header_style": "Classic Bold Sans-serif, High-contrast White",
        "palette": "Slate Grey, Navy Blue, Crimson",
        "highlight_color": "Vibrant Scarlet Red",
        "layout_mode": "GRID"
    },
    "科技政策 (Cyber Policy)": {
        "theme": "Digital Policy Hub, Steel Blue & Neon Cyan accents",
        "ui": "Poly-grid overlays, Ray-traced refraction, Semi-transparent frosted glass",
        "header_style": "Techno-Futuristic Sans-serif, Metallic Silver",
        "palette": "Steel Blue, Neon Cyan, Silver",
        "highlight_color": "Neon Lime Green",
        "layout_mode": "DYNAMIC"
    },
    "現代民俗 (Modern Festive)": {
        "theme": "Modern Folk, Rich Vermilion & Imperial Gold",
        "ui": "Lacquered Wood finish, Silk texture, Traditional cloud patterns",
        "header_style": "Calligraphic Bold with Gold Leaf outline",
        "palette": "Vermilion Red, Gold, Deep Charcoal",
        "highlight_color": "Imperial Gold",
        "layout_mode": "GRID"
    }
}

# ==========================================
# 2. 核心組裝邏輯 (鎖定 16:9 與物理貼合)
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, layout_mode, icon_style):
    style = STYLE_CONFIG[style_name]
    
    IRONCLAD_PROTOCOL = """
[CORE PROTOCOL: ABSOLUTE CANVAS & ASSET CONTROL]
1. MANDATORY DIMENSION: Fixed 1920x1080 (Strict 16:9 Landscape). 
   - FORBIDDEN: Any ratio change is a FAILURE. The frame is the "Physical Glass of a TV Screen".
2. PHYSICAL ASSET INTEGRATION (HARD-PASTING): 
   - UPLOADED FILES: Treat as "Immutable Physical Objects". 
   - NO RE-IMAGINING: Do NOT redraw, stylize, or morph the uploaded pixels.
   - ASSET SCALING: Scale to fit, but NEVER change the 1920x1080 canvas.
"""

    SYMBOL_PROTOCOL = f"""
[SYMBOL TRANSFORMATION MATRIX]
1. QUOTE RULE (" "): Text color to {style['highlight_color']}. REMOVE quotes from final render.
2. BRACKET RULE (【 】): Place text on a Deep Blue Color Block. REMOVE brackets from final render.
3. PARENTHESES RULE (( )): Keep text AND parentheses exactly (e.g., 125(公里)). NO color change.
"""

    TICKER_ZONE_GUARD = """
[PRECISION TICKER ZONE VOID]
- AREA: Bottom-Right ($X > 1332, Y > 990$, $588 x 90$ px).
- RULE: Strictly ZERO content. Background texture must flow seamlessly.
"""

    l_cmd = f"[LAYOUT: DYNAMIC FLOW] Use visual weighting." if "Dynamic" in layout_mode else "[LAYOUT: BALANCED GRID] Standard 50/50 split."
    i_cmd = "[ASSET: 3D VOLUMETRIC] Render with physical depth." if "3D" in icon_style else "[ASSET: 2D FLAT] Minimalist vector icons."

    final_prompt = f"""
[SYSTEM PROTOCOL: BROADCAST GRAPHIC V6.9]
{IRONCLAD_PROTOCOL}
{SYMBOL_PROTOCOL}
{TICKER_ZONE_GUARD}
{l_cmd}
{i_cmd}

[AESTHETIC & TEXTURE: {style_name}]
- THEME: {style['theme']} | UI: {style['ui']}
- HEADER: {style['header_style']} | PALETTE: {style['palette']}

[CONTENT]
- TITLE: {title}
- DATA_A: {left_in}
- DATA_B: {right_in}

[STRICT_GUARDRAILS]
- RENDER TRADITIONAL CHINESE ONLY.
- REMOVE labels like [日曆效果] or [圖]. Render visual assets ONLY.
- 16:9 Ratio and Asset Authenticity are the HIGHEST priorities.
"""
    return final_prompt

# ==========================================
# 3. Streamlit 介面
# ==========================================
st.set_page_config(page_title="Visual Director v6.9", layout="wide")
st.title("🎬 Visual Director v6.9 - 旗艦最終整合版")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📋 內容編輯區")
    title_in = st.text_input("新聞主標", placeholder='民生消費"漲價潮"觀測')
    left_in = st.text_area("區塊 A (主要內容)", height=150)
    right_in = st.text_area("區塊 B (補充說明)", height=150)
    
    st.divider()
    st.subheader("🛠️ 規格參數")
    s_style = st.selectbox("1. 選擇視覺風格", list(STYLE_CONFIG.keys()))
    
    c1, c2 = st.columns(2)
    with c1:
        s_layout = st.radio("2. 排版模式", ["固定網格 (Fixed Grid)", "動態流動 (Dynamic Flow)"], index=0)
    with c2:
        s_icon = st.radio("3. 物件質感", ["2D 簡約 (Flat)", "3D 立體 (Volumetric)"], index=1)

with col_out:
    st.subheader("🚀 生成之 AI 繪圖指令")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, s_layout, s_icon)
        st.success(f"已啟動：{s_style} 方案")
        
        # 顯示指令代碼
        st.code(final_cmd, language="markdown")
        
        # 製作人專屬檢查清單
        with st.expander("✅ 影像規格確認 (Checklist)", expanded=True):
            st.markdown(f"""
            - **畫布設定**：強制 1920x1080 (16:9)。
            - **高亮變色**："{title_in}" 將轉為 **{STYLE_CONFIG[s_style]['highlight_color']}** 並移除引號。
            - **資產保護**：物理硬貼合協定已生效，嚴禁 AI 重繪上傳圖檔。
            - **幾何避讓**：右下角 $588 \\times 90$ px 禁區已封印。
            """)
    else:
        st.info("請在左側輸入標題，系統將自動生成符合廣播級規格的繪圖指令。")