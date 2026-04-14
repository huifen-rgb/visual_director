import streamlit as st
from PIL import Image

# ==========================================
# 1. 視覺風格庫 (10 大旗艦風格，核心資產保留)
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
# 2. 核心組裝邏輯 (權重層級鎖定)
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, has_image=False):
    style = STYLE_CONFIG[style_name]
    
    # 權重 1: 避讓區絕對鎖定
    TICKER_ZONE = "[CRITICAL] Bottom-Right ($1332 < X < 1920$, $990 < Y < 1080$) MUST be void of user content."
    
    # 權重 2: 物理硬鎖定 (針對重繪事故)
    asset_protocol = ""
    if has_image:
        asset_protocol = "[ULTIMATE PIXEL LOCK] UPLOADED PHOTO IS IMMUTABLE. NO REDRAWING POSES OR FACES. HARD-COMPOSITE ONLY."

    # 權重 3: 符號轉換
    SYMBOL_PROTOCOL = f"Quotes to {style['highlight_color']} & REMOVE. 【Brackets】 to Blue Block & REMOVE. (Parentheses) KEEP."

    return f"""
[SYSTEM V8.2: MASTER BROADCAST]
CANVAS: 1920x1080. {TICKER_ZONE}
{asset_protocol}
{SYMBOL_PROTOCOL}
STYLE: {style_name} | UI: {style['ui']}
[CONTENT DATA]
TITLE: {title}
DATA_A: {left_in}
DATA_B: {right_in}
[STRICT] Traditional Chinese ONLY. Background must blend into ticker zone naturally.
"""

# ==========================================
# 3. Streamlit 介面 (疊加優化佈局)
# ==========================================
st.set_page_config(page_title="Visual Director v8.2", layout="wide")
st.title("🎬 Visual Director v8.2 - 疊加優化完全體")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    # --- 1. 原本的功能保留：文字內容區 ---
    st.subheader("📋 內容編輯區")
    title_in = st.text_input("新聞主標", placeholder="輸入標題...")
    left_in = st.text_area("區塊 A (內容)", height=100, placeholder="輸入主內文...")
    right_in = st.text_area("區塊 B (補充)", height=100, placeholder="輸入補充數據...")
    
    # --- 2. 局部更改：資產處理層 (疊加裁切預覽) ---
    st.divider()
    st.markdown("📸 **資產焦點處理**")
    uploaded_file = st.file_uploader("上傳欲硬貼合的照片", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        raw_img = Image.open(uploaded_file)
        w, h = raw_img.size
        
        # 局部優化：裁切預覽滑桿
        st.caption("調整裁切焦點，確保元首臉部不被 UI 框架遮擋")
        zoom = st.slider("1. 縮放 (Zoom)", 0.1, 1.0, 0.7)
        off_x = st.slider("2. 水平中心 (X Offset)", 0, w, w//2)
        off_y = st.slider("3. 垂直中心 (Y Offset)", 0, h, h//2)
        
        # 即時顯示預覽 (改回相容語法 use_column_width)
        st.image(raw_img, caption="資產已載入：將執行物理硬貼合", use_column_width=True)

    # --- 3. 原本的功能保留：風格與規格 ---
    st.divider()
    s_style = st.selectbox("視覺風格 (10 大旗艦庫)", list(STYLE_CONFIG.keys()))
    s_layout = st.radio("排版模式", ["固定網格", "動態流動"])

with col_out:
    st.subheader("🚀 生成之 AI 繪圖指令")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, has_image=(uploaded_file is not None))
        st.error("🚨 物理避讓與像素鎖定協定已啟動")
        st.code(final_cmd, language="markdown")
        
        # 檢查清單
        with st.expander("✅ 核心規格檢查 (v8.2)", expanded=True):
            st.markdown(f"""
            - **內文 A/B**：{'已填寫' if left_in else '空白'}
            - **避讓區**：$588 \\times 90$ px 鎖定
            - **像素鎖定**：{'硬合成模式' if uploaded_file else 'AI 生成模式'}
            - **畫布比例**：$1920 \\times 1080$
            """)
    else:
        st.info("請輸入標題開始組裝指令。")
