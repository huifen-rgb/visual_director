import streamlit as st
from PIL import Image
import io

# ==========================================
# 1. 物理框架規格 (不准動，這是副控室底線)
# ==========================================
FRAME_SPEC = {
    "width": 1018,
    "height": 708,
    "pos": (451, 142)  # 針對 Elite Obsidian 版面的中心框位
}

# ==========================================
# 2. 物理合成引擎 (硬貼合，不重繪)
# ==========================================
def hard_composite(bg_image, photo_image, crop_box):
    # 這裡 crop_box 是使用者在預覽區選定的區域 (left, top, right, bottom)
    bg = bg_image.convert("RGBA")
    
    # 執行手動裁切：確保最重要的臉部被保留
    cropped_photo = photo_image.crop(crop_box)
    
    # 縮放到框架尺寸 (使用最高清晰度 LANCZOS)
    final_photo = cropped_photo.resize((FRAME_SPEC["width"], FRAME_SPEC["height"]), Image.Resampling.LANCZOS)
    
    # 暴力硬貼
    bg.paste(final_photo, FRAME_SPEC["pos"], final_photo)
    return bg

# ==========================================
# 3. Streamlit 介面 (加入預覽功能)
# ==========================================
st.set_page_config(page_title="Visual Director v8.0", layout="wide")
st.title("🎬 Visual Director v8.0 - 焦點裁切預覽版")

col_in, col_out = st.columns([1, 1.2])

with col_in:
    st.subheader("📸 資產處理區")
    uploaded_file = st.file_uploader("上傳原始新聞照片", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        raw_img = Image.open(uploaded_file)
        
        # 建立裁切預覽邏輯
        st.info("💡 請在下方拖動滑桿，調整照片在 1018x708 框架中的顯示中心")
        
        # 這裡我們用 Slider 來實作一個簡易但穩定的裁切預覽
        w, h = raw_img.size
        # 這裡計算一個 1018:708 的比例區塊
        zoom = st.slider("1. 縮放比例 (Zoom)", 0.1, 1.0, 0.8)
        
        # 計算裁切框的大小
        crop_w = int(w * zoom)
        crop_h = int(crop_w * (FRAME_SPEC["height"] / FRAME_SPEC["width"]))
        
        # 確保裁切框不超過原圖
        if crop_h > h:
            crop_h = h
            crop_w = int(crop_h * (FRAME_SPEC["width"] / FRAME_SPEC["height"]))

        # 選擇中心點
        offset_x = st.slider("2. 水平位置 (X Offset)", 0, w - crop_w, (w - crop_w)//2)
        offset_y = st.slider("3. 垂直位置 (Y Offset)", 0, h - crop_h, (h - crop_h)//2)
        
        crop_box = (offset_x, offset_y, offset_x + crop_w, offset_y + crop_h)
        
        # 即時呈現裁切預覽
        preview_img = raw_img.crop(crop_box)
        st.image(preview_img, caption="裁切預覽：這將是硬貼到框架中的內容", use_column_width=True)
        
        if st.button("🚀 確認裁切並鎖定資產"):
            st.session_state['locked_crop'] = crop_box
            st.success("像素焦點已鎖定！")

with col_out:
    st.subheader("🎬 CG 生產指令與規格")
    title_in = st.text_input("新聞主標")
    
    if title_in and uploaded_file:
        # 這裡生成給 AI 的指令，同時標註「已經過人工裁切處理」
        st.error("🚨 警告：已啟動像素級合成，AI 嚴禁對照片進行任何重繪。")
        
        # 這裡輸出妳在 v7.9 的暴力指令
        # ... (省略部分 STYLE 選擇邏輯)
        
        st.markdown(f"""
        ### 製作人最終指令：
        1. **物理規格**：1920x1080 (16:9)。
        2. **硬合成要求**：請將照片硬貼至座標 {FRAME_SPEC['pos']}。
        3. **絕對禁止**：禁止重構人物臉部、禁止修改祝酒動作。
        4. **右下角避讓**：588x90 px 嚴格保留給 Ticker。
        """)
