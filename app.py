import streamlit as st
from PIL import Image
from streamlit_cropper import st_cropper
import io

# ==========================================
# 1. 視覺風格庫 (旗艦 10 大風格，全量鎖定)
# ==========================================
STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {"theme": "Consumer TRENDS, Fluid", "ui": "Organic shapes, Frosted glass", "palette": "Beige, Blue, Red", "highlight": "Vibrant Sunburst Orange"},
    "社會案件 (Justice Alert)": {"theme": "Crime Scene Noir", "ui": "CCTV grain, Map overlays", "palette": "Grey, Yellow, Police Blue", "highlight": "Safety Orange"},
    "體育競技 (Victory Orange)": {"theme": "Sports High-Energy", "ui": "Carbon fiber, Speed lines", "palette": "Orange, Graphite", "highlight": "Vivid Neon Yellow"},
    "全球財經 (Elite Obsidian)": {"theme": "Financial Dashboard", "ui": "Aluminum, Data streams", "palette": "Navy, Gold, Cyan", "highlight": "Electric Cyan"},
    "突發重磅 (Breaking Alert)": {"theme": "Emergency Crimson", "ui": "Radial Blur, Red glow", "palette": "Signal Red, White, Black", "highlight": "Bright Vivid Yellow"},
    "選情政論 (Democracy Grey)": {"theme": "Political Studio", "ui": "Matte Metallic, Star patterns", "palette": "Slate Grey, Navy, Crimson", "highlight": "Vibrant Scarlet Red"},
    "科技政策 (Cyber Policy)": {"theme": "Digital Hub", "ui": "Poly-grid, Frosted glass", "palette": "Steel Blue, Neon Cyan, Silver", "highlight": "Neon Lime Green"},
    "綠能永續 (Eco-Future)": {"theme": "Sustainability & ESG", "ui": "Natural textures, Bokeh", "palette": "Emerald Green, Leaf Green, White", "highlight": "Sunlight Gold"},
    "現代民俗 (Modern Festive)": {"theme": "Modern Folk, Rich Vermilion", "ui": "Lacquered Wood finish, Silk texture", "palette": "Vermilion Red, Gold, Charcoal", "highlight": "Imperial Gold"},
    "生醫科技 (Clinical White)": {"theme": "Bio-Tech", "ui": "Clinical surfaces, DNA helix", "palette": "Pristine White, Sky Blue, Navy", "highlight": "Bright Sky Blue"}
}

# 物理框架位置 (針對 1, 2, 3 張照片的吸附座標)
LAYOUT_PRESETS = {
    1: [{"label": "中央大框架", "pos": (451, 142), "size": (1018, 708)}],
    2: [{"label": "左對抗位", "pos": (120, 200), "size": (800, 550)}, {"label": "右對抗位", "pos": (1000, 200), "size": (800, 550)}],
    3: [{"label": "三方左", "pos": (50, 250), "size": (580, 450)}, {"label": "三方中", "pos": (670, 250), "size": (580, 450)}, {"label": "三方右", "pos": (1290, 250), "size": (580, 450)}]
}

# ==========================================
# 2. 核心組裝引擎
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, layout, icon_style, ai_autonomy=True, has_image=False):
    style = STYLE_CONFIG[style_name]
    TICKER_ZONE = "[ABSOLUTE VOID] Bottom-Right ($1332 < X < 1920$, $990 < Y < 1080$) for Ticker."
    
    if ai_autonomy:
        color_logic = f"AI AUTONOMY: Select striking palette & highlight based on '{title}' sentiment."
    else:
        color_logic = f"FIXED: Palette {style['palette']}, Highlight {style['highlight']}"

    SYMBOL_MATRIX = f"""
[SYMBOL MATRIX]
1. Quotes (" "): Color per Highlight, REMOVE symbols.
2. Brackets (【 】): Deep Blue Block, REMOVE symbols.
3. Parentheses (( )): KEEP as is.
"""
    return f"""
[SYSTEM V9.4] CANVAS: 1920x1080. {TICKER_ZONE}
{SYMBOL_MATRIX}
[PIXEL LOCK] UPLOADED PHOTOS ARE RAW MATTER. NO REDRAWING.
STYLE: {style_name} | {color_logic}
LAYOUT: {layout} | ICON: {icon_style}
[CONTENT] TITLE: {title} | DATA_A: {left_in} | DATA_B: {right_in}
[STRICT] Traditional Chinese ONLY. No poses alteration.
"""

# ==========================================
# 3. Streamlit 介面
# ==========================================
st.set_page_config(page_title="Visual Director v9.4", layout="wide")
st.title("🎬 Visual Director v9.4 - 比例對位修正版")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📋 1. 新聞文字資產")
    title_in = st.text_input("新聞主標", placeholder="輸入標題...")
    c_a, c_b = st.columns(2)
    with c_a: left_in = st.text_area("區塊 A 內文", height=100)
    with c_b: right_in = st.text_area("區塊 B 補充", height=100)
    
    st.divider()
    st.subheader("📸 2. 照片視覺處理 (支援多圖拖曳)")
    uploaded_files = st.file_uploader("上傳照片 (支援多選)", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    processed_assets = []
    if uploaded_files:
        photo_count = len(uploaded_files)
        specs = LAYOUT_PRESETS.get(photo_count, LAYOUT_PRESETS[1])
        
        for idx, file in enumerate(uploaded_files):
            if idx < len(specs):
                with st.expander(f"視覺裁切：{specs[idx]['label']}", expanded=(idx==0)):
                    raw_img = Image.open(file).convert("RGB")
                    
                    # 🛑 核心修正處：直接把 size (寬, 高) 傳進去，不要做除法
                    aspect_tuple = specs[idx]['size'] 
                    
                    cropped_img = st_cropper(
                        raw_img, 
                        aspect_ratio=aspect_tuple, # 傳入 (1018, 708)
                        box_color='#FF0000', 
                        key=f"crop_{idx}"
                    )
                    
                    final_p = cropped_img.resize(specs[idx]['size'], Image.Resampling.LANCZOS)
                    st.image(final_p, caption=f"照片 {idx+1} 預覽", use_column_width=True)
                    processed_assets.append({'img': final_p, 'pos': specs[idx]['pos']})

    st.divider()
    st.subheader("🛠️ 3. 視覺規格設定")
    s_style = st.selectbox("視覺風格庫", list(STYLE_CONFIG.keys()))
    ai_sovereignty = st.toggle("✨ 啟動 AI 視覺主權", value=True)
    r1, r2 = st.columns(2)
    with r1: s_layout = st.radio("排版模式", ["GRID", "DYNAMIC"])
    with r2: s_icon = st.radio("物件質感", ["Flat", "Volumetric"])

with col_out:
    st.subheader("🚀 第一產出：AI 繪圖指令")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, s_layout, s_icon, ai_autonomy=ai_sovereignty, has_image=(len(uploaded_files)>0))
        st.code(final_cmd, language="markdown")
    
    st.divider()
    st.subheader("🔥 第二產出：物理硬合成成品")
    bg_file = st.file_uploader("📥 上傳 AI 生成的背景圖", type=["png", "jpg"])
    
    if bg_file and processed_assets:
        if st.button("執行硬合成預覽"):
            bg_img = Image.open(bg_file).convert("RGBA")
            for asset in processed_assets:
                bg_img.paste(asset['img'].convert("RGBA"), asset['pos'], asset['img'].convert("RGBA"))
            st.image(bg_img, use_column_width=True)
            
            buf = io.BytesIO()
            bg_img.save(buf, format="PNG")
            st.download_button("💾 下載最終成品圖", data=buf.getvalue(), file_name="CTS_Final_CG.png", mime="image/png")
