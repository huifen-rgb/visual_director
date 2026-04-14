import streamlit as st

# ==========================================
# 🛑【Visual Director 系統檢討報告 - 事故編號 20260414】
# ==========================================
# 檢討對象：AI 生成邏輯模組
# 事故描述：
#   1. 嚴重篡改照片真實性：將賴副總統合照由「端坐」改為「祝酒」，擅自刪除現場人員並修改國父遺像。
#   2. 避讓區執行不力：無視右下角 588x90 px 的避讓指令，導致星星裝飾遮擋跑馬燈。
# 根因分析：
#   AI 盲目追求視覺平衡與「美化」，導致創意權限蓋過了「新聞真實性」與「播報硬體限制」。
# 修正對策：
#   1. 升級 [ULTIMATE PIXEL LOCK] 指令：禁止 AI 對上傳資產進行任何語義理解，改為物理貼合。
#   2. 鎖定 [TICKER ZONE CONTENT VOID]：將右下角定義為內容禁區，僅允許背景擴散，嚴禁任何資產進入。
# ==========================================

STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {"theme": "Consumer TRENDS", "ui": "Organic shapes, Frosted glass", "palette": "Beige, Blue, Red", "highlight_color": "Vibrant Sunburst Orange", "layout_mode": "DYNAMIC"},
    "社會案件 (Justice Alert)": {"theme": "Crime Scene Noir", "ui": "CCTV grain, Map overlays", "palette": "Grey, Yellow, Police Blue", "highlight_color": "Safety Orange", "layout_mode": "GRID"},
    "體育競技 (Victory Orange)": {"theme": "Sports High-Energy", "ui": "Carbon fiber, Speed lines", "palette": "Orange, Graphite, White", "highlight_color": "Vivid Neon Yellow", "layout_mode": "GRID"},
    "全球財經 (Elite Obsidian)": {"theme": "Financial Dashboard", "ui": "Aluminum, Data streams", "palette": "Navy, Gold, Cyan", "highlight_color": "Electric Cyan", "layout_mode": "GRID"},
    "突發重磅 (Breaking Alert)": {"theme": "Emergency Crimson", "ui": "Radial Motion Blur, Red glow", "palette": "Signal Red, White, Black", "highlight_color": "Bright Vivid Yellow", "layout_mode": "GRID"},
    "選情政論 (Democracy Grey)": {"theme": "Political Studio", "ui": "Matte Metallic, Star patterns", "palette": "Slate Grey, Navy, Crimson", "highlight_color": "Vibrant Scarlet Red", "layout_mode": "GRID"},
    "科技政策 (Cyber Policy)": {"theme": "Digital Hub", "ui": "Poly-grid, Frosted glass", "palette": "Steel Blue, Cyan, Silver", "highlight_color": "Neon Lime Green", "layout_mode": "DYNAMIC"},
    "綠能永續 (Eco-Future)": {"theme": "Sustainability", "ui": "Natural textures, Bokeh", "palette": "Emerald Green, Leaf Green, White", "highlight_color": "Sunlight Gold", "layout_mode": "GRID"},
    "現代民俗 (Modern Festive)": {"theme": "Modern Folk", "ui": "Lacquered Wood, Silk textures", "palette": "Vermilion Red, Gold, Charcoal", "highlight_color": "Imperial Gold", "layout_mode": "GRID"},
    "生醫科技 (Clinical White)": {"theme": "Bio-Tech", "ui": "Clinical surfaces, DNA helix", "palette": "Pristine White, Sky Blue, Navy", "highlight_color": "Bright Sky Blue", "layout_mode": "DYNAMIC"}
}

def build_final_prompt(title, left_in, right_in, style_name, layout_mode, icon_style):
    style = STYLE_CONFIG[style_name]
    
    # --- 暴力級避讓：區分背景與內容 ---
    TICKER_ZONE_MANDATE = """
[ABSOLUTE CONTENT EXCLUSION: TICKER ZONE]
- VOID AREA: Bottom-Right ($1332 < X < 1920$, $990 < Y < 1080$).
- CONTENT LOCK: No text (TITLE, DATA_A, DATA_B) or Uploaded Asset can touch this zone.
- VISUAL FLOW: Background texture must naturally bleed into this zone, but foreground objects are STRICKLY FORBIDDEN.
"""

    # --- 像素級鎖死：針對賴副總統照片重繪事故的對策 ---
    PIXEL_LOCK_PROTOCOL = """
[ULTIMATE PIXEL LOCK: NEWS INTEGRITY]
- UPLOADED FILE: Treat as IMMUTABLE RAW DATA.
- NO HALLUCINATION: Do NOT redraw faces, poses, or objects. Do NOT use it as a reference.
- HARD-COMPOSITE: Take the EXACT original pixels and place them into the frame. 
- PROHIBITED: If the AI changes the people's poses (e.g., from sitting to toasting), it is a CATASTROPHIC FAILURE.
"""

    SYMBOL_PROTOCOL = f"""
[SYMBOL TRANSFORMATION MATRIX]
1. Quotes (" "): Color to {style['highlight_color']}. REMOVE quotes.
2. Brackets (【 】): Deep Blue Block. REMOVE brackets.
3. Parentheses (( )): KEEP exactly as is.
"""

    final_prompt = f"""
[SYSTEM V7.8: MASTER BROADCAST CONTROL]
CANVAS: Fixed 1920x1080 (16:9).
{TICKER_ZONE_MANDATE}
{PIXEL_LOCK_PROTOCOL}
{SYMBOL_PROTOCOL}

[AESTHETIC: {style_name}]
- THEME: {style['theme']} | UI: {style['ui']} | PALETTE: {style['palette']}

[DATA CONTENT]
- TITLE: {title}
- DATA_A: {left_in}
- DATA_B: {right_in}

[STRICT_GUARDRAILS]
- Traditional Chinese ONLY.
- REMOVE labels like [圖].
- NO ALTERATION to original photograph pixels.
- Bottom-right content void is non-negotiable.
"""
    return final_prompt

# --- Streamlit 介面 ---
st.set_page_config(page_title="Visual Director v7.8", layout="wide")
st.title("🎬 Visual Director v7.8 - 像素級檢討修正版")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📋 內容編輯區")
    title_in = st.text_input("新聞主標", placeholder='輸入標題...')
    left_in = st.text_area("區塊 A", height=150)
    right_in = st.text_area("區塊 B", height=150)
    
    st.divider()
    s_style = st.selectbox("視覺風格", list(STYLE_CONFIG.keys()))
    s_layout = st.radio("排版模式", ["固定網格 (Fixed Grid)", "動態流動 (Dynamic Flow)"])
    s_icon = st.radio("物件質感", ["2D 簡約 (Flat)", "3D 立體 (Volumetric)"])

with col_out:
    st.subheader("🚀 生成之 AI 繪圖指令")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, s_layout, s_icon)
        st.error("檢討報告已載入並鎖定指令邏輯")
        st.code(final_cmd, language="markdown")
    else:
        st.info("輸入標題以啟動。")
