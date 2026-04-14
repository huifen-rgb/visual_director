import streamlit as st
from PIL import Image

# ==========================================
# 1. 視覺風格庫 (10 大旗艦風格完全體)
# ==========================================
STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {"theme": "Consumer TRENDS", "ui": "Organic shapes, Frosted glass", "palette": "Beige, Blue, Red", "highlight_color": "Vibrant Sunburst Orange", "layout_mode": "DYNAMIC"},
    "社會案件 (Justice Alert)": {"theme": "Crime Scene Noir", "ui": "CCTV grain, Map overlays", "palette": "Grey, Yellow, Police Blue", "highlight_color": "Safety Orange", "layout_mode": "GRID"},
    "體育競技 (Victory Orange)": {"theme": "Sports High-Energy", "ui": "Carbon fiber, Speed lines", "palette": "Orange, Graphite", "highlight_color": "Vivid Neon Yellow", "layout_mode": "GRID"},
    "全球財經 (Elite Obsidian)": {"theme": "Financial Dashboard", "ui": "Aluminum, Data streams", "palette": "Navy, Gold, Cyan", "highlight_color": "Electric Cyan", "layout_mode": "GRID"},
    "突發重磅 (Breaking Alert)": {"theme": "Emergency Crimson", "ui": "Radial Motion Blur, Red glow", "palette": "Signal Red, White, Black", "highlight_color": "Bright Vivid Yellow", "layout_mode": "GRID"},
    "選情政論 (Democracy Grey)": {"theme": "Political Studio", "ui": "Matte Metallic, Star patterns", "palette": "Slate Grey, Navy, Crimson", "highlight_color": "Vibrant Scarlet Red", "layout_mode": "GRID"},
    "科技政策 (Cyber Policy)": {"theme": "Digital Hub", "ui": "Poly-grid, Frosted glass", "palette": "Steel Blue, Cyan, Silver", "highlight_color": "Neon Lime Green", "layout_mode": "DYNAMIC"},
    "綠能永續 (Eco-Future)": {"theme": "Sustainability", "ui": "Natural textures, Bokeh", "palette": "Emerald Green, Leaf Green, White", "highlight_color": "Sunlight Gold", "layout_mode": "GRID"},
    "現代民俗 (Modern Festive)": {"theme": "Modern Folk, Rich Vermilion", "ui": "Lacquered Wood, Silk textures", "palette": "Vermilion Red, Gold, Charcoal", "highlight_color": "Imperial Gold", "layout_mode": "GRID"},
    "生醫科技 (Clinical White)": {"theme": "Bio-Tech", "ui": "Clinical surfaces, DNA helix", "palette": "Pristine White, Sky Blue, Navy", "highlight_color": "Bright Sky Blue", "layout_mode": "DYNAMIC"}
}

# ==========================================
# 2. 核心組裝邏輯
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, layout_mode, icon_style, has_image=False):
    style = STYLE_CONFIG[style_name]
    
    TICKER_ZONE_MANDATE = """
[ABSOLUTE CONTENT EXCLUSION: TICKER ZONE]
- AREA: Bottom-Right ($1332 < X < 1920$, $990 < Y < 1080$).
- CONTENT LOCK: No text or primary image pixels allowed here. Background textures ONLY.
"""

    asset_instruction = ""
    if has_image:
        asset_instruction = """
[ULTIMATE PIXEL LOCK: IMMUTABLE ASSET]
- UPLOADED FILE DETECTED: This is RAW PHYSICAL MATTER.
- NO HALLUCINATION: Do NOT redraw faces, Do NOT change the people's poses.
- HARD-COMPOSITE: Take the EXACT pixels of the uploaded photo and paste them into the layout.
- VERIFICATION: If the AI-generated person looks different from the uploaded photo, it is a FAILED render.
"""

    SYMBOL_PROTOCOL = f"""
[SYMBOL TRANSFORMATION MATRIX]
1. Quotes (" "): Color to {style['highlight_color']}. REMOVE quotes.
2. Brackets (【 】): Deep Blue Color Block. REMOVE brackets.
3. Parentheses (( )): KEEP exactly as is.
"""

    final_prompt = f"""
[SYSTEM V7.9: MASTER BROADCAST CONTROL]
CANVAS: Fixed 1920x1080 (16:9).
{TICKER_ZONE_MANDATE}
{asset_instruction}
{SYMBOL_PROTOCOL}

[STYLE: {style_name}]
- THEME: {style['theme']} | UI: {style['ui']} | PALETTE: {style['palette']}

[CONTENT]
- TITLE: {title}
- DATA_A: {left_in}
- DATA_B: {right_in}

[STRICT_GUARDRAILS]
- Traditional Chinese ONLY.
- REMOVE labels like [日曆效果].
- DO NOT re-imagine original photograph pixels.
- Background must flow naturally into the ticker zone.
"""
    return final_prompt

# ==========================================
# 3. Streamlit 介面
# ==========================================
st.set_page_config(page_title="Visual Director v7.9", layout="wide")
st.title("🎬 Visual Director v7.9 - 資產硬鎖定強化版")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📋 內容與資產上傳")
    title_in = st.text_input("新聞主標", placeholder='輸入標題...')
    left_in = st.text_area("區塊 A (主要內容)", height=100)
    right_in = st.text_area("區塊 B (補充說明)", height=100)
    
    st.divider()
    st.markdown("📸 **資產對應區 (新聞照片上傳)**")
    uploaded_file = st.file_uploader("上傳欲硬貼合的照片 (JPG/PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="已偵測到上傳資產：系統將啟動像素鎖定協定", use_container_width=True)
    
    st.divider()
    s_style = st.selectbox("1. 選擇視覺風格", list(STYLE_CONFIG.keys()))
    s_layout = st.radio("2. 排版模式", ["固定網格 (Fixed Grid)", "動態流動 (Dynamic Flow)"])
    s_icon = st.radio("3. 物件質感", ["2D 簡約 (Flat)", "3D 立體 (Volumetric)"])

with col_out:
    st.subheader("🚀 生成之 AI 繪圖指令")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, s_layout, s_icon, has_image=(uploaded_file is not None))
        
        if uploaded_file:
            st.error("🚨 警告：偵測到上傳資產，已強制掛載『像素鎖定協定』。")
        else:
            st.warning("💡 提示：目前未上傳照片，AI 將根據主題自定義視覺物件。")
            
        st.code(final_cmd, language="markdown")
        
        with st.expander("✅ 核心規格檢查表", expanded=True):
            st.markdown(f"""
            - **避讓區**：右下角 $588 \\times 90$ px 淨空 (允許背景融合)。
            - **像素鎖定**：{'已啟動 (禁止重繪照片)' if uploaded_file else '未啟動 (使用 AI 預設物件)'}。
            - **高亮色**：使用 **{STYLE_CONFIG[s_style]['highlight_color']}**。
            - **畫布比例**：鎖定 1920x1080。
            """)
    else:
        st.info("請輸入標題開始。")
