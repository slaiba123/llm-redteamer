import streamlit as st

def inject_styles():
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'IBM Plex Sans', sans-serif; }

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp { background-color: #0a0a0a; color: #e8e8e8; }

[data-testid="stSidebar"] {
    background-color: #0f0f0f;
    border-right: 1px solid #1e1e1e;
}
[data-testid="stSidebar"] * { color: #e8e8e8 !important; }

.sidebar-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #555 !important;
    margin-bottom: 6px;
    margin-top: 20px;
    display: block;
}

.sidebar-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #ff3333 !important;
    margin-bottom: 20px;
}

.topbar {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 0 0 32px 0;
    border-bottom: 1px solid #1a1a1a;
    margin-bottom: 36px;
}
.topbar-badge {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    background: #ff3333;
    color: #fff;
    padding: 4px 10px;
    border-radius: 2px;
}
.topbar-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 22px;
    font-weight: 600;
    color: #f0f0f0;
    letter-spacing: -0.02em;
}
.topbar-sub {
    font-size: 13px;
    color: #444;
    margin-left: auto;
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: 0.03em;
}

.pipeline {
    display: flex;
    gap: 0;
    margin: 0 0 40px 0;
    border: 1px solid #1e1e1e;
    border-radius: 4px;
    overflow: hidden;
}
.pipeline-step {
    flex: 1;
    padding: 18px 20px;
    border-right: 1px solid #1e1e1e;
    background: #0f0f0f;
}
.pipeline-step:last-child { border-right: none; }
.pipeline-step-num {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #ff3333;
    font-weight: 600;
    letter-spacing: 0.1em;
    margin-bottom: 6px;
}
.pipeline-step-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 13px;
    font-weight: 600;
    color: #e8e8e8;
    margin-bottom: 4px;
}
.pipeline-step-desc {
    font-size: 12px;
    color: #555;
    line-height: 1.5;
}

.metric-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 32px;
}
.metric-card {
    background: #0f0f0f;
    border: 1px solid #1e1e1e;
    border-radius: 4px;
    padding: 20px 24px;
}
.metric-card-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #555;
    margin-bottom: 8px;
}
.metric-card-value {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 28px;
    font-weight: 600;
    color: #f0f0f0;
    line-height: 1;
}
.metric-card-value.red { color: #ff3333; }
.metric-card-value.green { color: #33cc66; }
.metric-card-value.yellow { color: #ffaa33; }

.section-header {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #555;
    margin: 32px 0 16px 0;
    padding-bottom: 10px;
    border-bottom: 1px solid #1a1a1a;
}

.status-bar {
    display: flex;
    gap: 0;
    border: 1px solid #1e1e1e;
    border-radius: 4px;
    overflow: hidden;
    margin-bottom: 32px;
}
.status-item {
    flex: 1;
    padding: 14px 18px;
    border-right: 1px solid #1e1e1e;
    background: #0f0f0f;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    color: #555;
    display: flex;
    align-items: center;
    gap: 8px;
}
.status-item:last-child { border-right: none; }
.status-item.active { color: #e8e8e8; background: #141414; }
.status-item.done { color: #33cc66; }
.status-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #333;
    flex-shrink: 0;
}
.status-dot.active { background: #ffaa33; animation: pulse 1s infinite; }
.status-dot.done { background: #33cc66; }
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.3; }
}

.stSelectbox > div > div {
    background-color: #0f0f0f !important;
    border: 1px solid #222 !important;
    color: #e8e8e8 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 13px !important;
    border-radius: 3px !important;
}
.stTextArea textarea {
    background-color: #0f0f0f !important;
    border: 1px solid #222 !important;
    color: #e8e8e8 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    border-radius: 3px !important;
}
.stTextInput input {
    background-color: #0f0f0f !important;
    border: 1px solid #222 !important;
    color: #e8e8e8 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    border-radius: 3px !important;
}
.stButton > button {
    background-color: #ff3333 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 3px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    padding: 12px 24px !important;
    width: 100% !important;
    transition: background 0.15s !important;
}
.stButton > button:hover { background-color: #cc0000 !important; }
.stDownloadButton > button {
    background-color: transparent !important;
    color: #e8e8e8 !important;
    border: 1px solid #333 !important;
    border-radius: 3px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 11px !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
}
</style>
""", unsafe_allow_html=True)