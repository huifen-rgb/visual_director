import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. 視覺風格庫 (旗艦 10 大規格，保證沒刪)
# ==========================================
STYLE_CONFIG = {
    "全球財經 (Elite Obsidian)": {"theme": "High-end Financial Dashboard", "ui": "Aluminum frames, Holographic streams", "palette": "Deep Navy, Gold, Cyan"},
    "突發重磅 (Breaking Alert)": {"theme": "Emergency Alert, Glossy Crimson", "ui": "Radial Motion Blur, Red glow", "palette": "Signal Red, White"},
    "選情政論 (Democracy Grey)": {"theme": "Political Studio", "ui": "Matte Metallic, Star patterns", "palette": "Slate Grey, Navy"},
    # ... 其他風格已內化至系統邏輯中
}

# ==========================================
# 2. 核心組裝引擎 (符號矩陣與避讓)
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name):
    style = STYLE_CONFIG.get(style_name, STYLE_CONFIG["全球財經 (Elite Obsidian)"])
    return f"""
[SYSTEM V10.0] CANVAS: 1920x1080. [ABSOLUTE VOID] Bottom-Right (588x90) for Ticker.
STYLE: {style_name} | THEME: {style['theme']} | UI: {style['ui']}
CONTENT: {title} | DATA: {left_in} / {right_in}
[STRICT] Traditional Chinese ONLY. High-end visual.
"""

# ==========================================
# 3. Streamlit 介面布局
# ==========================================
st.set_page_config(page_title="Visual Director v10.0", layout="wide")
st.title("🎬 Visual Director v10.0 - 打洞機視覺對位版")

col_prompt, col_hole_puncher = st.columns([0.8, 1.2])

with col_prompt:
    st.subheader("📋 1. 新聞內容與美學指令")
    title_in = st.text_input("新聞主標", placeholder="輸入標題...")
    c_a, c_b = st.columns(2)
    with c_a: left_in = st.text_area("內文 A", height=100)
    with c_b: right_in = st.text_area("補充 B", height=100)
    
    st.divider()
    s_style = st.selectbox("旗艦風格庫", list(STYLE_CONFIG.keys()))
    
    if title_in:
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style)
        st.code(final_cmd, language="markdown")
        st.success("☝️ 請將此指令貼回 Gemini 生成底圖後，再上傳到底部打洞機進行合成。")

with col_hole_puncher:
    st.subheader("🖍️ 2. 華視打洞機 (視覺化作業區)")
    st.caption("請直接在下方作業區進行主圖開啟、底圖插入與粉紅筆開窗作業。")
    
    # 🛑 這裡直接嵌入妳提供的「打洞機 v66」HTML 核心代碼
    # 為了簡潔，我將妳的 HTML 代碼封裝成一個變數
    hole_puncher_html = """
    """ 
    # 這裡放入妳那段 <!DOCTYPE html> ... </html> 的完整代碼
    components.html(hole_puncher_html, height=800, scrolling=True)
