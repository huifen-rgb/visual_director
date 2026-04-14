import streamlit as st
from PIL import Image, ImageDraw
from streamlit_cropper import st_cropper
import io

# ==========================================
# 1. 視覺風格庫 (旗艦全規格回歸，絕不精簡)
# ==========================================
STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {"theme": "Consumer TRENDS", "ui": "Organic shapes", "palette": "Beige, Blue, Red", "highlight": "Vibrant Sunburst Orange"},
    "社會案件 (Justice Alert)": {"theme": "Crime Scene Noir", "ui": "CCTV grain", "palette": "Grey, Yellow, Police Blue", "highlight": "Safety Orange"},
    "體育競技 (Victory Orange)": {"theme": "Sports High-Energy", "ui": "Carbon fiber", "palette": "Orange, Graphite", "highlight": "Vivid Neon Yellow"},
    "全球財經 (Elite Obsidian)": {"theme": "Financial Dashboard", "ui": "Aluminum", "palette": "Navy, Gold, Cyan", "highlight": "Electric Cyan"},
    "突發重磅 (Breaking Alert)": {"theme": "Emergency Crimson", "ui": "Radial Blur", "palette": "Red, White, Black", "highlight": "Bright Vivid Yellow"},
    "選情政論 (Democracy Grey)": {"theme": "Political Studio", "ui": "Matte Metallic", "palette": "Slate Grey, Navy", "highlight": "Vibrant Scarlet Red"},
    "科技政策 (Cyber Policy)": {"theme": "Digital Hub", "ui": "Poly-grid", "palette": "Blue, Silver", "highlight": "Lime"},
    "綠能永續 (Eco-Future)": {"theme": "Sustainability & ESG", "ui": "Natural textures", "palette": "Emerald Green, White", "highlight": "Sunlight Gold"},
    "現代民俗 (Modern Festive)": {"theme": "Modern Folk", "ui": "Lacquered Wood", "palette": "Vermilion Red, Gold", "highlight": "Imperial Gold"},
    "生醫科技 (Clinical White)": {"theme": "Bio-Tech", "ui": "Clinical surfaces", "palette": "White, Sky Blue", "highlight": "Bright Sky Blue"}
}

# ==========================================
# 2. 核心指令引擎 (避讓、符號、AI 主權)
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, ai_autonomy):
    style = STYLE_CONFIG[style_name]
    ticker_void = "[ABSOLUTE VOID] Bottom-Right ($1332 < X < 1920$, $990 < Y < 1080$) for Ticker."
    return f"""
[SYSTEM V9.8: DYNAMIC LAYOUT] CANVAS: 1920x1080. {ticker_void}
[COMPOSITION] User has manually defined asset areas. 
STYLE: {style_name} | AI_AUTONOMY: {ai_autonomy}
CONTENT: {title} | DATA: {left_in} / {right_in}
[STRICT] Traditional Chinese ONLY. No redraw on assets.
"""

# ==========================================
# 3. Streamlit 介面 (全面轉向「自定義插入」)
# ==========================================
st.set_page_config(page_title="Visual Director v9.8", layout="wide")
st.title("🎬 Visual Director v9.8 - 自由排版與視覺插入版")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    # 第一步：底圖參考
    st.subheader("🖼️ 1. 底圖與文字資產")
    bg_ref_file = st.file_uploader("上傳 AI 背景底圖 (1920x1080)", type=["png", "jpg"])
    title_in = st.text_input("新聞主標")
    c_a, c_b = st.columns(2)
    with c_a: left_in = st.text_area("內文 A", height=80)
    with c_b: right_in = st.text_area("補充 B", height=80)

    # 第二步：自定義插入與拖曳模擬
    st.divider()
    st.subheader("📸 2. 自定義選區並插入圖片")
    uploaded_files = st.file_uploader("上傳欲插入的照片 (支援 1-4 張)", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    processed_assets = []
    if uploaded_files:
        for idx, file in enumerate(uploaded_files):
            with st.expander(f"📍 調整照片 {idx+1} 的大小與位置", expanded=(idx == 0)):
                # --- 核心優化：視覺化位置控制 ---
                st.write("設定在 1920x1080 畫布上的位置：")
                p1, p2, p3, p4 = st.columns(4)
                with p1: target_x = st.number_input(f"X (左距)", 0, 1920, 451, key=f"tx{idx}")
                with p2: target_y = st.number_input(f"Y (頂距)", 0, 1080, 250, key=f"ty{idx}")
                with p3: target_w = st.number_input(f"寬度", 100, 1920, 800, key=f"tw{idx}")
                with p4: target_h = st.number_input(f"高度", 100, 1080, 500, key=f"th{idx}")

                # --- 視覺化裁切 ---
                raw_img = Image.open(file).convert("RGB")
                st.write("裁切要保留的畫面焦點：")
                # 這裡的比例會自動跟隨上面妳設定的寬度高度！
                cropped = st_cropper(raw_img, aspect_ratio=(target_w, target_h), box_color='#FF0000', key=f"cr_{idx}")
                final_p = cropped.resize((target_w, target_h), Image.Resampling.LANCZOS)
                
                # --- 即時對位預覽 (Mockup) ---
                if bg_ref_file:
                    bg_ref = Image.open(bg_ref_file).convert("RGBA")
                    mockup = bg_ref.copy()
                    # 在預覽圖畫一個紅框表示插入位子
                    draw = ImageDraw.Draw(mockup)
                    draw.rectangle([target_x, target_y, target_x + target_w, target_y + target_h], outline="red", width=5)
                    mockup.paste(final_p.convert("RGBA"), (target_x, target_y), final_p.convert("RGBA"))
                    st.image(mockup, caption="在此位置插入預覽", use_column_width=True)
                
                processed_assets.append({'img': final_p, 'pos': (target_x, target_y)})

with col_out:
    # 規格與指令
    st.subheader("🛠️ 3. 視覺規格設定")
    s_style = st.selectbox("旗艦風格庫", list(STYLE_CONFIG.keys()))
    ai_sovereignty = st.toggle("✨ 啟動 AI 視覺主權", value=True)
    
    st.divider()
    st.subheader("🚀 第一產出：AI 繪圖指令")
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, ai_sovereignty)
        st.code(final_cmd, language="markdown")
    
    # 最終合成與下載
    st.divider()
    st.subheader("🔥 第二產出：物理硬合成成品")
    if bg_ref_file and processed_assets:
        if st.button("執行最終硬合成 (Apply Selection)"):
            final_canvas = Image.open(bg_ref_file).convert("RGBA")
            for asset in processed_assets:
                final_canvas.paste(asset['img'].convert("RGBA"), asset['pos'], asset['img'].convert("RGBA"))
            
            st.image(final_canvas, use_column_width=True)
            buf = io.BytesIO()
            final_canvas.save(buf, format="PNG")
            st.download_button("💾 下載最終 1920x1080 成品圖", data=buf.getvalue(), file_name="Final_CG.png")
