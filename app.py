import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# 1. 旗艦風格庫 (10 大全規格美學：還原所有細節描述)
# ==========================================
STYLE_CONFIG = {
    "民生消費 (Fluid Analytics)": {"theme": "Consumer TRENDS, Fluid", "ui": "Organic shapes, Frosted glass", "palette": "Beige, Blue, Red", "highlight": "Vibrant Sunburst Orange"},
    "社會案件 (Justice Alert)": {"theme": "Crime Scene Noir", "ui": "CCTV grain, Map data overlays, Forensic textures, Caution tape", "palette": "Concrete Grey, Caution Yellow, Police Blue", "highlight": "Safety Orange"},
    "體育競技 (Victory Orange)": {"theme": "High-Energy Sports Broadcast", "ui": "Carbon fiber, Kinetic lines, Stadium spotlights", "palette": "Electric Orange, Graphite Grey, Stark White", "highlight": "Vivid Neon Yellow"},
    "全球財經 (Elite Obsidian)": {"theme": "High-end Financial Dashboard", "ui": "Anodized Aluminum, Holographic streams, Glass refractions, Grid", "palette": "Deep Navy, Gold, Cyan Data Lines", "highlight": "Electric Cyan"},
    "突發重磅 (Breaking Alert)": {"theme": "Emergency Alert, High-Gloss Crimson", "ui": "Radial Motion Blur, Red glow, Danger pulse", "palette": "Signal Red, White, Black", "highlight": "Bright Vivid Yellow"},
    "選情政論 (Democracy Grey)": {"theme": "Political Election Studio", "ui": "Matte Metallic, Star patterns, Studio spotlighting, Marble", "palette": "Slate Grey, Navy Blue, Crimson", "highlight": "Vibrant Scarlet Red"},
    "科技政策 (Cyber Policy)": {"theme": "Digital Policy Hub", "ui": "Poly-grid, Ray-traced refraction, Semi-transparent glass, Nodes", "palette": "Steel Blue, Neon Cyan, Silver", "highlight": "Neon Lime Green"},
    "綠能永續 (Eco-Future)": {"theme": "Sustainability & ESG", "ui": "Natural leaf textures, Soft outdoor bokeh, Organic glass", "palette": "Emerald Green, Leaf Green, Soft White", "highlight": "Sunlight Gold"},
    "現代民俗 (Modern Festive)": {"theme": "Modern Folk, Rich Vermilion", "ui": "Lacquered Wood, Silk texture, Cloud patterns, Gold leaf", "palette": "Vermilion Red, Gold, Deep Charcoal", "highlight": "Imperial Gold"},
    "生醫科技 (Clinical White)": {"theme": "Medical & Bio-Tech", "ui": "Sanitized surfaces, DNA helix motifs, Hexagonal grid", "palette": "Pristine White, Sky Blue, Navy", "highlight": "Bright Sky Blue"}
}

# ==========================================
# 2. 核心指令引擎 (鏡面符號矩陣 - 後台邏輯鎖定區)
# ==========================================
def build_final_prompt(title, left_in, right_in, style_name, header_mode, icon_style, ai_autonomy, ticker_lock):
    style = STYLE_CONFIG[style_name]
    
    # 🛑 禁區鎖定 (588x90)
    TICKER_ZONE = "[ABSOLUTE PHYSICAL VOID] Bottom-Right ($1332 < X < 1920$, $990 < Y < 1080$). NO content." if ticker_lock else "[FULL CANVAS ACCESS]"

    # 🛑 標題霸權 (300% MEGA SIZE)
    HEADER_W = "TITLE FONT SIZE: MEGA LARGE (300% of body text). ABSOLUTE VISUAL DOMINANCE."
    if "兩行" in header_mode: HEADER_W += " USE TWO-LINE STACKED LAYOUT."

    # 🛑 符號矩陣核心 (SYMBOL MATRIX PROTOCOL) - 成品絕對不留符號
    SYMBOL_PROTOCOL = f"""
[STRICT SYMBOL TRANSFORMATION]
1. "雙引號": Highlight text within using {style['highlight']}. REMOVE quotes from final image.
2. 【方頭括號】: Render text as Sub-headers on a color block. FONT SIZE: LARGE. REMOVE brackets.
3. (圓括號): KEEP both text and brackets as is. NO color change. (e.g. 125(公里))
4. [圖----slug圖]: ASSET PROTECTION ZONE. Leave area 100% BLANK for photo insertion. DELETE label.
5. [效果說明]: (e.g. [對話框], [圓餅圖], [日曆效果---(日期)], [筆刷效果], [蓋章效果], [icon]). 
   Render visual ONLY, COMPLETELY DELETE instruction text.
6. [換行]: Manual line break at this position. REMOVE label.
"""
    
    color_logic = f"AI_COLOR: Dynamic based on title sentiment." if ai_autonomy else f"FIXED: {style['palette']}"
    
    return f"""
[SYSTEM V11.7: PROTOCOL LOCKED] CANVAS: 1920x1080. {TICKER_ZONE}
{HEADER_W}
{SYMBOL_PROTOCOL}
[IMPORTANT] If "[圖----slug圖]" is present, leave area VOID. DO NOT overlap with any text.
STYLE: {style_name} | {color_logic} | ICON: {icon_style} | UI: {style['ui']}
CONTENT: TITLE={title} | DATA_A={left_in} | DATA_B={right_in}
[STRICT] Traditional Chinese ONLY. TITLES MUST BE MEGA LARGE (300% SIZE).
"""

# ==========================================
# 3. 華視打洞機 v66 完全歸位鑲嵌版 (Undo & 縮放全修復)
# ==========================================
HOLE_PUNCHER_V66 = """
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>華視打洞機 v66</title>
    <script src="https://cdn.jsdelivr.net/npm/@mediapipe/selfie_segmentation/selfie_segmentation.js"></script>
    <style>
        :root { --pink: #ff00ff; --panel: #1a1a1a; --blue: #2979ff; --green: #00c853; --cyan: #00e5ff; --yellow: #ffeb3b; --orange: #ff9800; }
        body { font-family: 'Segoe UI', sans-serif; background: #0a0a0a; color: #fff; margin: 0; padding: 10px; height: 100vh; display: flex; flex-direction: column; overflow: hidden; }
        .toolbar { background: var(--panel); padding: 10px 20px; border-radius: 12px; display: flex; align-items: center; gap: 10px; margin-bottom: 10px; border: 1px solid #333; flex-shrink: 0; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
        .group { display: flex; align-items: center; gap: 8px; border-right: 1px solid #444; padding-right: 12px; }
        .main-layout { display: flex; gap: 10px; flex: 1; min-height: 0; }
        .view-panel { flex: 1; display: flex; flex-direction: column; position: relative; border-radius: 12px; background: #000; border: 1px solid #222; overflow: hidden; }
        .label { position: absolute; top: 12px; left: 12px; background: rgba(0,0,0,0.8); padding: 4px 10px; border-radius: 4px; font-size: 10px; font-weight: bold; z-index: 1000; color: #aaa; pointer-events: none; }
        .canvas-wrapper { position: relative; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        canvas { max-width: 100%; max-height: 100%; cursor: crosshair; }
        button { padding: 8px 12px; cursor: pointer; background: #2a2a2a; color: #ccc; border: 1px solid #444; border-radius: 6px; font-size: 11px; font-weight: 600; transition: 0.2s; }
        button.active { background: var(--pink) !important; color: #fff; }
        .download-btn { background: #fff; color: #000; font-weight: bold; margin-left: auto; }
    </style>
</head>
<body>
    <div id="loading-overlay" style="position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); display:none; flex-direction:column; align-items:center; justify-content:center; z-index:2000;">🤖 打洞機調整中...</div>
    <div class="toolbar">
        <div class="group"><button onclick="document.getElementById('upload').click()" style="color: var(--yellow);">📁 開啟主圖</button><label style="font-size:10px; color:#888;"><input type="checkbox" id="autoLayoutCheck"> 自動留邊</label><input type="file" id="upload" accept="image/*" style="display:none"></div>
        <div class="group"><button onclick="document.getElementById('bgInput').click()">🖼️ 插入底圖</button><input type="file" id="bgInput" accept="image/*" style="display:none" multiple><button onclick="document.getElementById('fgInput').click()" style="color: var(--cyan);">➕ 插入前景</button><input type="file" id="fgInput" accept="image/*" style="display:none" multiple><button onclick="deleteSelectedItem()" style="color: var(--orange);">🗑️ 刪除選中</button></div>
        <div class="group"><button id="aiProtectBtn" style="background:var(--blue); color:#fff; border:none;">🔒 AI 鎖定</button><button class="mode-btn" data-mode="brush">粉紅筆 (B)</button><button class="mode-btn" data-mode="rect">矩形 (R)</button><button class="mode-btn" data-mode="eraser">橡皮擦 (E)</button></div>
        <div class="group"><label>筆刷</label><input type="range" id="brushSize" min="1" max="250" value="50"><label>羽化</label><input type="range" id="featherSize" min="0" max="100" value="8"></div>
        <button id="commitBtn" style="background:#444">✅ 定案</button><button onclick="undo()">↶ Undo</button><button id="downloadBtn" class="download-btn">導出 PNG</button>
    </div>
    <div class="main-layout">
        <div class="view-panel"><div class="label">WORKSPACE (作業區)</div><div class="canvas-wrapper"><canvas id="workCanvas"></canvas></div></div>
        <div class="view-panel"><div class="label">PREVIEW (成品區)</div><div class="canvas-wrapper"><canvas id="previewCanvas"></canvas></div></div>
    </div>
    <script>
        let img = new Image(), bgImages = [], fgImages = [], activeItem = { type: null, index: -1 }; 
        let isDrawing = false, isMovingItem = false, isResizingItem = false, isMovingShape = false;
        let currentMode = 'brush', mouseX = 0, mouseY = 0, startX, startY, lastMoveX, lastMoveY, activeShape = null, history = [];
        let layout = { outW: 1920, outH: 1080, padding: 180, drawW: 0, drawH: 0, drawX: 0, drawY: 0 };
        const HANDLE_SIZE = 24;
        const workCanvas = document.getElementById('workCanvas'), previewCanvas = document.getElementById('previewCanvas');
        const wCtx = workCanvas.getContext('2d'), pCtx = previewCanvas.getContext('2d');
        const cache = { manual: document.createElement('canvas'), ai: document.createElement('canvas'), mask: document.createElement('canvas'), mb: document.createElement('canvas'), pink: document.createElement('canvas') };
        const mCtx = cache.manual.getContext('2d'), aiCtx = cache.ai.getContext('2d'), tCtx = cache.mask.getContext('2d'), mbCtx = cache.mb.getContext('2d'), pkCtx = cache.pink.getContext('2d');
        const selfieSegmentation = new SelfieSegmentation({ locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/selfie_segmentation/${file}` });
        selfieSegmentation.setOptions({ modelSelection: 1 });
        selfieSegmentation.onResults(res => {
            document.getElementById('loading-overlay').style.display = 'none';
            aiCtx.clearRect(0, 0, 1920, 1080); aiCtx.save(); aiCtx.filter = 'blur(2.5px)'; aiCtx.drawImage(res.segmentationMask, layout.drawX, layout.drawY, layout.drawW, layout.drawH); aiCtx.restore();
            const data = aiCtx.getImageData(0,0,1920,1080);
            for(let i=0; i<data.data.length; i+=4) { let a = data.data[i]; if(a < 128) a = (Math.pow(a/128, 1.8) * 128); else a = 255 - (Math.pow((255-a)/127, 1.8) * 127); data.data[i] = data.data[i+1] = data.data[i+2] = 255; data.data[i+3] = a; }
            aiCtx.putImageData(data, 0, 0); render();
        });
        function render() {
            if(!img.src) return; const W = 1920, H = 1080;
            [wCtx, pCtx, tCtx, mbCtx, pkCtx].forEach(ctx => { ctx.globalCompositeOperation = 'source-over'; ctx.imageSmoothingEnabled = true; ctx.clearRect(0, 0, W, H); });
            const feather = document.getElementById('featherSize').value;
            if(feather > 0) tCtx.filter = `blur(${feather}px)`; tCtx.drawImage(cache.manual, 0, 0);
            let s = isDrawing && (currentMode==='rect'||currentMode==='circle') ? { type: currentMode, x: startX, y: startY, w: mouseX-startX, h: mouseY-startY } : activeShape;
            if (s) { tCtx.fillStyle = 'white'; if (s.type === 'rect') tCtx.fillRect(s.x, s.y, s.w, s.h); else { tCtx.beginPath(); tCtx.ellipse(s.x+s.w/2, s.y+s.h/2, Math.abs(s.w/2), Math.abs(s.h/2), 0, 0, Math.PI*2); tCtx.fill(); } }
            tCtx.filter = 'none'; tCtx.globalCompositeOperation = 'destination-out'; tCtx.drawImage(cache.ai, 0, 0); tCtx.globalCompositeOperation = 'source-over';
            const drawStack = (targetCtx) => {
                targetCtx.save();
                if(document.getElementById('autoLayoutCheck').checked) { targetCtx.filter = 'blur(40px) brightness(0.6)'; targetCtx.drawImage(img, -50, -50, W + 100, H + 100); targetCtx.filter = 'none'; }
                bgImages.forEach(bg => targetCtx.drawImage(bg.img, bg.x, bg.y, bg.w, bg.h));
                mbCtx.clearRect(0, 0, W, H); mbCtx.globalCompositeOperation = 'source-over'; mbCtx.drawImage(img, layout.drawX, layout.drawY, layout.drawW, layout.drawH);
                mbCtx.globalCompositeOperation = 'destination-out'; mbCtx.drawImage(cache.mask, 0, 0); targetCtx.drawImage(cache.mb, 0, 0);
                fgImages.forEach(fg => targetCtx.drawImage(fg.img, fg.x, fg.y, fg.w, fg.h)); targetCtx.restore();
            };
            drawStack(pCtx); drawStack(wCtx);
            pkCtx.drawImage(cache.mask, 0, 0); pkCtx.globalCompositeOperation = 'source-in'; pkCtx.fillStyle = '#ff00ff'; pkCtx.fillRect(0,0,W,H);
            wCtx.save(); wCtx.globalAlpha = 0.4; wCtx.drawImage(cache.pink, 0, 0); wCtx.restore(); drawUI(s);
        }
        function drawUI(s) {
            wCtx.save();
            let sel = activeItem.type === 'bg' ? bgImages[activeItem.index] : (activeItem.type === 'fg' ? fgImages[activeItem.index] : null);
            if(sel && !isDrawing) {
                wCtx.setLineDash([5, 5]); wCtx.strokeStyle = activeItem.type === 'bg' ? '#ffeb3b' : '#00e5ff'; wCtx.lineWidth = 2; wCtx.strokeRect(sel.x, sel.y, sel.w, sel.h);
                const hX = sel.x + sel.w, hY = sel.y + sel.h; wCtx.beginPath(); wCtx.arc(hX, hY, HANDLE_SIZE/2, 0, Math.PI*2); wCtx.fillStyle = wCtx.strokeStyle; wCtx.fill(); wCtx.strokeStyle = "#fff"; wCtx.lineWidth = 3; wCtx.stroke();
            }
            if (s) { wCtx.setLineDash([8, 4]); wCtx.strokeStyle = '#FF0'; if (s.type === 'rect') wCtx.strokeRect(s.x, s.y, s.w, s.h); else { wCtx.beginPath(); wCtx.ellipse(s.x+s.w/2, s.y+s.h/2, Math.abs(s.w/2), Math.abs(s.h/2), 0, 0, Math.PI*2); wCtx.stroke(); } }
            wCtx.restore();
        }
        function deleteSelectedItem() { if (activeItem.type === 'bg') bgImages.splice(activeItem.index, 1); else if (activeItem.type === 'fg') fgImages.splice(activeItem.index, 1); activeItem = { type: null, index: -1 }; render(); }
        const getPos = e => { const r = workCanvas.getBoundingClientRect(); return { x: (e.clientX-r.left)*(1920/r.width), y: (e.clientY-r.top)*(1080/r.height) }; };
        function isInRect(p, r) { const xM=Math.min(r.x,r.x+r.w), xX=Math.max(r.x,r.x+r.w), yM=Math.min(r.y,r.y+r.h), yX=Math.max(r.y,r.y+r.h); return p.x>=xM && p.x<=xX && p.y>=yM && p.y<=yX; }
        function isOverHandle(p, sel) { if(!sel) return false; return Math.sqrt(Math.pow(p.x-(sel.x+sel.w), 2)+Math.pow(p.y-(sel.y+sel.h), 2)) < HANDLE_SIZE; }
        
        // 🛑 Undo & 下筆邏輯校正
        workCanvas.onmousedown = e => {
            if(!img.src) return; const p = getPos(e); saveHistory();
            let sel = activeItem.type === 'bg' ? bgImages[activeItem.index] : (activeItem.type === 'fg' ? fgImages[activeItem.index] : null);
            if(isOverHandle(p, sel)) { isResizingItem = true; return; }
            for (let i = fgImages.length-1; i >= 0; i--) { if (isInRect(p, fgImages[i])) { activeItem = { type: 'fg', index: i }; isMovingItem = true; lastMoveX = p.x; lastMoveY = p.y; render(); return; } }
            for (let i = bgImages.length-1; i >= 0; i--) { if (isInRect(p, bgImages[i])) { activeItem = { type: 'bg', index: i }; isMovingItem = true; lastMoveX = p.x; lastMoveY = p.y; render(); return; } }
            activeItem = { type: null, index: -1 }; isDrawing = true; startX = p.x; startY = p.y;
            if(currentMode==='brush'||currentMode==='eraser'){ mCtx.beginPath(); mCtx.moveTo(p.x, p.y); mCtx.lineWidth = document.getElementById('brushSize').value; mCtx.lineCap = 'round'; mCtx.globalCompositeOperation = currentMode==='eraser' ? 'destination-out' : 'source-over'; mCtx.strokeStyle = 'white'; mCtx.lineTo(p.x, p.y); mCtx.stroke(); }
            render();
        };
        workCanvas.onmousemove = e => {
            const p = getPos(e); mouseX = p.x; mouseY = p.y; let sel = activeItem.type === 'bg' ? bgImages[activeItem.index] : (activeItem.type === 'fg' ? fgImages[activeItem.index] : null);
            if (isOverHandle(p, sel)) workCanvas.style.cursor = 'nwse-resize';
            else if (isResizingItem && sel) { sel.w = Math.max(50, p.x - sel.x); sel.h = sel.w / sel.aspectRatio; }
            else if (isMovingItem && sel) { sel.x += (p.x - lastMoveX); sel.y += (p.y - lastMoveY); lastMoveX = p.x; lastMoveY = p.y; }
            else if (isDrawing && (currentMode==='brush'||currentMode==='eraser')) { mCtx.lineTo(p.x, p.y); mCtx.stroke(); }
            render();
        };
        window.onmouseup = () => { if (isDrawing && (currentMode==='rect'||currentMode==='circle')) { activeShape = { type: currentMode, x: startX, y: startY, w: mouseX-startX, h: mouseY-startY }; } isDrawing = isMovingItem = isResizingItem = false; render(); };
        function saveHistory() { history.push({ manual: mCtx.getImageData(0,0,1920,1080), ai: aiCtx.getImageData(0,0,1920,1080) }); if(history.length > 30) history.shift(); }
        function undo() { if(history.length > 0) { let h = history.pop(); mCtx.putImageData(h.manual, 0, 0); aiCtx.putImageData(h.ai, 0, 0); render(); } }
        document.getElementById('upload').onchange = e => { const f = e.target.files[0]; if(f){ const r = new FileReader(); r.onload = ev => { img.onload = () => { [workCanvas, previewCanvas, cache.manual, cache.ai, cache.mask, cache.mb, cache.pink].forEach(c => { c.width = 1920; c.height = 1080; }); const ratio = Math.min(1920 / img.width, 1080 / img.height); layout.drawW = img.width * ratio; layout.drawH = img.height * ratio; layout.drawX = (1920 - layout.drawW) / 2; layout.drawY = (1080 - layout.drawH) / 2; render(); }; img.src = ev.target.result; }; r.readAsDataURL(f); } };
        document.getElementById('bgInput').onchange = e => { Array.from(e.target.files).forEach(f => { const r = new FileReader(); r.onload = ev => { const n = new Image(); n.onload = () => { bgImages.push({ img: n, x: 0, y: 0, w: 1920, h: 1080, aspectRatio: n.width/n.height }); render(); }; n.src = ev.target.result; }; r.readAsDataURL(f); }); };
        document.getElementById('fgInput').onchange = e => { Array.from(e.target.files).forEach(f => { const r = new FileReader(); r.onload = ev => { const n = new Image(); n.onload = () => { fgImages.push({ img: n, x: 500, y: 300, w: 400, h: 400/(n.width/n.height), aspectRatio: n.width/n.height }); activeItem = { type: 'fg', index: fgImages.length - 1 }; render(); }; n.src = ev.target.result; }; r.readAsDataURL(f); }); };
        document.getElementById('aiProtectBtn').onclick = async () => { if(!img.src) return; document.getElementById('loading-overlay').style.display='flex'; await selfieSegmentation.send({image: img}); };
        document.querySelectorAll('.mode-btn').forEach(b => { b.onclick = () => { document.querySelectorAll('.mode-btn').forEach(x => x.classList.remove('active')); b.classList.add('active'); currentMode = b.dataset.mode; render(); }; });
        document.getElementById('commitBtn').onclick = () => { if(activeShape) { mCtx.fillStyle='white'; if(activeShape.type==='rect') mCtx.fillRect(activeShape.x, activeShape.y, activeShape.w, activeShape.h); else { mCtx.beginPath(); mCtx.ellipse(activeShape.x+activeShape.w/2, activeShape.y+activeShape.h/2, Math.abs(activeShape.w/2), Math.abs(activeShape.h/2), 0, 0, Math.PI*2); mCtx.fill(); } activeShape=null; render(); } };
        document.getElementById('downloadBtn').onclick = () => { const a = document.createElement('a'); a.download = 'Final_CG.png'; a.href = previewCanvas.toDataURL('image/png'); a.click(); };
        window.onkeydown = e => { if(e.key.toLowerCase()==='z'&&e.ctrlKey) undo(); };
    </script>
</body>
</html>
"""

# ==========================================
# 4. Streamlit 介面 (完全規格整合)
# ==========================================
st.set_page_config(page_title="Visual Director v11.7", layout="wide")
st.title("🎬 Visual Director v11.7 - 鏡面霸權整合版")
st.caption("Producer Huifen Edition | 符號協定 100% 鎖死、打洞機全修復")

tab1, tab2 = st.tabs(["🚀 第一步：產出鏡面指令", "🖍️ 第二步：華視打洞機作業區"])

with tab1:
    # --- 視覺轉換矩陣說明 (確保一行都沒少) ---
    with st.expander("❓ 如何寫出專業鏡面？ (符號矩陣與轉換原則說明)", expanded=True):
        st.markdown("### 🔠 鏡面符號矩陣 (Symbol Matrix Protocol)")
        st.table([
            {"語法": '"文字"', "視覺動作": "文字套用高亮變色 (Highlight)", "成品處理": "❌ 移除雙引號"},
            {"語法": "【方頭括號】", "視覺動作": "文字轉化為色塊小標、字體加大", "成品處理": "❌ 移除方頭括號"},
            {"語法": "(圓括號)", "視覺動作": "文字不變色、保持輔助資訊感", "成品處理": "✅ 保留圓括號 (如：125(公里))"},
            {"語法": "[圖----slug圖]", "視覺動作": "🛡️ 劃定素材留白特區，嚴禁文字效果壓過", "成品處理": "❌ 移除說明文字"},
            {"語法": "[效果說明]", "視覺動作": "轉化為專業視覺圖示或 UI 物件", "成品處理": "❌ 移除說明文字"},
            {"語法": "[換行]", "視覺動作": "標題強制執行斷行指令", "成品處理": "❌ 移除標籤"}
        ])
        st.info("💡 效果說明範例：[對話框][圓餅圖][日曆效果---(日期)][筆刷效果][蓋章效果][icon]")

    st.divider()
    col_l, col_r = st.columns([1.2, 0.8])
    with col_l:
        st.subheader("📋 鏡面內容編輯 (萬華喪屍專案)")
        h_mode = st.radio("標題張力：", ["兩行大標題 (MEGA SIZE)", "單行大標題 (專業感)"], horizontal=True)
        title_in = st.text_area("鏡面主標題 (AI 將字 300% 大大大)", value='"芬太尼喪屍"入侵萬華?[換行]\n"對折人"驚悚影像曝光', height=100)
        c1, c2 = st.columns(2)
        with c1: left_in = st.text_area("區塊 A 內文", value='[threads icon] \n[網友icon] 網友:[對話框] \n我以為我在舊金山\n[圖----網友圖佔版面1/2]\n北市萬華1男子\n遭疑吸"芬太尼"', height=220)
        with c2: right_in = st.text_area("區塊 B 內文", value='【"芬太尼"小檔案】\n●第二級毒品\n●人造鴉片類藥物\n  約嗎啡50-100倍\n●美加地區濫用\n  造成死亡案例\n\n刑事局:\n112年起僅台南查獲1件\n觀看影像確有吸毒樣子', height=220)
    
    with col_r:
        st.subheader("🛠️ 視覺與空間規格")
        ticker_lock = st.toggle("🔒 鎖定右下角 588x90 跑馬燈禁區", value=True)
        s_style = st.selectbox("旗艦風格庫 (10 大全規格)", list(STYLE_CONFIG.keys()), index=3) # 預設全球財經
        ai_sovereignty = st.toggle("✨ 啟動 AI 視覺主權 (自主配色)", value=True)
        r1, r2 = st.columns(2)
        with r1: s_layout = st.radio("排版模式", ["GRID", "DYNAMIC"], horizontal=True)
        with r2: s_icon = st.radio("物件質感", ["Flat", "Volumetric"], index=1, horizontal=True)
        st.info(f"🎨 高亮色：{STYLE_CONFIG[s_style]['highlight']}")

    if title_in:
        st.divider()
        st.subheader("🔥 最終生成：Gemini 繪圖指令")
        # 參數對位完全修正：8 個參數
        final_cmd = build_final_prompt(title_in, left_in, right_in, s_style, h_mode, s_icon, ai_sovereignty, ticker_lock)
        st.code(final_cmd, language="markdown")

with tab2:
    st.subheader("🛠️ 華視打洞機 v66 (最終修復整合版)")
    st.caption("開啟 AI 背景圖 $\rightarrow$ 插入底圖(縮放OK) $\rightarrow$ 插入前景 $\rightarrow$ 粉紅筆開窗(Undo OK) $\rightarrow$ 導出 PNG")
    # 鑲嵌最完整 v66 HTML，高度 950
    components.html(HOLE_PUNCHER_V66, height=950, scrolling=True)
