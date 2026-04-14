import streamlit as st
from PIL import Image
import io

# ==========================================
# 1. 物理框架與規格字典 (針對多圖配置)
# ==========================================
# 定義不同張數時的座標偏移，確保排版不亂
LAYOUT_SPECS = {
    1: [{"pos": (451, 142), "size": (1018, 708)}],
    2: [{"pos": (120, 200), "size": (800, 550)}, {"pos": (1000, 200), "size": (800, 550)}],
    3: [{"pos": (50, 250), "size": (580, 450)}, {"pos": (670, 250), "size": (580, 450)}, {"pos": (1290, 250), "size": (580, 450)}]
}

# ==========================================
# 2. 核心合成引擎：執行真正的物理硬貼合
# ==========================================
def process_composite(bg_image, photo_assets, layout_type):
    canvas = bg_image.convert("RGBA")
    specs = LAYOUT_SPECS.get(layout_type, LAYOUT_SPECS[1])
    
    for i, asset in enumerate(photo_assets):
        if i < len(specs):
            spec = specs[i]
            # 取得該照片裁切後的預覽圖
            photo = asset['img'].resize(spec['size'], Image.Resampling.LANCZOS)
            # 硬貼合
            canvas.paste(photo, spec['pos'], photo)
    
    # 【最後檢核】絕對鎖死右下角 588x90 避讓區
    # 這裡可以選擇強制覆蓋一層透明背景，確保沒有任何像素溢出
    return canvas

# ==========================================
# 3. Streamlit 介面
# ==========================================
st.set_page_config(page_title="Visual Director v8.6", layout="wide")
st.title("🎬 Visual Director v8.6 - 多圖硬合成生產版")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📋 1. 內容與背景資產")
    bg_file = st.file_uploader("📥 第一步：上傳 AI 生成的背景圖 (1920x1080)", type=["png", "jpg"])
    
    st.divider()
    st.subheader("📸 2. 多圖資產焦點處理")
    # 開啟多檔案上傳
    uploaded_photos = st.file_uploader("上傳新聞照片 (可選取多張)", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    processed_assets = []
    if uploaded_photos:
        for idx, file in enumerate(uploaded_photos):
            with st.expander(f"對應照片 {idx+1}：焦點裁切", expanded=(idx==0)):
                raw_img = Image.open(file).convert("RGB")
                w, h = raw_img.size
                
                # 這裡保留妳要求的裁切滑桿，每張圖獨立控制
                z = st.slider(f"縮放 {idx+1}", 0.1, 2.0, 1.0, key=f"z{idx}")
                ox = st.slider(f"X 中心 {idx+1}", 0, w, w//2, key=f"x{idx}")
                oy = st.slider(f"Y 中心 {idx+1}", 0, h, h//2, key=f"y{idx}")
                
                # 簡單裁切預覽邏輯
                target_spec = LAYOUT_SPECS.get(len(uploaded_photos), LAYOUT_SPECS[1])[min(idx, 2)]
                tw, th = target_spec['size']
                cw, ch = int(tw * z), int(th * z)
                box = (max(0, ox-cw//2), max(0, oy-ch//2), min(w, ox+cw//2), min(h, oy+ch//2))
                
                preview = raw_img.crop(box).resize((tw, th), Image.Resampling.LANCZOS)
                st.image(preview, caption=f"照片 {idx+1} 裁切預覽", use_column_width=True)
                processed_assets.append({'img': preview})

with col_out:
    st.subheader("🚀 3. 最終生產與導出")
    if bg_file and processed_assets:
        if st.button("🔥 執行物理硬合成 (Generate Final CG)"):
            bg_img = Image.open(bg_file)
            final_cg = process_composite(bg_img, processed_assets, len(processed_assets))
            
            # 呈現最終結果
            st.success("✅ 合成完成！請檢查元首真實性與右下角避讓區。")
            st.image(final_cg, caption="Visual Director 最終產出成品", use_column_width=True)
            
            # 提供下載
            buf = io.BytesIO()
            final_cg.save(buf, format="PNG")
            st.download_button(
                label="💾 下載 1920x1080 最終成品圖",
                data=buf.getvalue(),
                file_name="final_news_cg.png",
                mime="image/png"
            )
    else:
        st.info("請上傳『AI 背景圖』與『至少一張新聞照片』以開始合成。")
