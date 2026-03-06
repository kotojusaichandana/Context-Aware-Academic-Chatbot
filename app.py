import streamlit as st
import chatbot_engine
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Context-Aware Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## ⚙️ Controls")
    dark_mode = st.toggle("🌙 Dark Mode", value=False)
    accent = st.color_picker("🎨 Accent Color", "#6366f1")
    st.markdown("---")
    st.markdown("### 🧠 Chat Memory")
    st.info("This chatbot remembers\nconversation context.")

# ---------------- CSS ----------------
bg_dark = "linear-gradient(-45deg, #020617, #0f172a, #020617, #000)"
bg_light = "linear-gradient(-45deg, #fdfbfb, #e0f2fe, #ede9fe, #fdfbfb)"

st.markdown(f"""
<style>
body {{
    background: {'{}'.format(bg_dark if dark_mode else bg_light)};
    background-size: 400% 400%;
    animation: gradientBG 14s ease infinite;
}}

@keyframes gradientBG {{
    0% {{ background-position: 0% 50%; }}
    50% {{ background-position: 100% 50%; }}
    100% {{ background-position: 0% 50%; }}
}}

.main {{
    background: rgba(255,255,255,{'0.08' if dark_mode else '0.6'});
    backdrop-filter: blur(20px);
    padding: 2rem;
    border-radius: 26px;
}}

.title {{
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    background: linear-gradient(90deg, {accent}, #22d3ee);
    -webkit-background-clip: text;
    color: transparent;
}}

.subtitle {{
    text-align: center;
    margin-bottom: 2rem;
    color: {'#9ca3af' if dark_mode else '#555'};
}}

.chat {{
    max-height: 420px;
    overflow-y: auto;
    padding-right: 6px;
}}

.user {{
    background: linear-gradient(135deg, {accent}, #22d3ee);
    color: white;
    padding: 14px 18px;
    border-radius: 22px 22px 6px 22px;
    margin: 12px 0;
    max-width: 80%;
    margin-left: auto;
}}

.bot {{
    background: rgba(30,41,59,{'0.85' if dark_mode else '0.95'});
    color: {'#e5e7eb' if dark_mode else '#333'};
    padding: 14px 18px;
    border-radius: 22px 22px 22px 6px;
    margin: 12px 0;
    max-width: 80%;
}}

.time {{
    font-size: 10px;
    opacity: 0.6;
    margin-top: 6px;
}}

.typing {{
    font-style: italic;
    opacity: 0.7;
}}

.footer {{
    text-align: center;
    margin-top: 2rem;
    font-size: 13px;
    color: {'#9ca3af' if dark_mode else '#666'};
}}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='title'>🤖 Context-Aware Academic Chatbot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Aesthetic • Intelligent • Context Driven</div>", unsafe_allow_html=True)

# ---------------- INIT ----------------
if "bot" not in st.session_state:
    st.session_state.bot = chatbot_engine.Chatbot()

if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------------- CLEAR ----------------
if st.button("🧹 Clear Chat"):
    st.session_state.chat = []

# ---------------- CHAT WINDOW ----------------
st.markdown("<div class='chat'>", unsafe_allow_html=True)

for who, msg, t in st.session_state.chat:
    if who == "You":
        st.markdown(f"<div class='user'>🧑 {msg}<div class='time'>{t}</div></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>🤖 {msg}<div class='time'>{t}</div></div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- INPUT BAR ----------------
user_input = st.text_input(
    "Message",
    placeholder="Type your question here…",
    label_visibility="collapsed"
)

# ---------------- SEND ----------------
if st.button("Send 🚀") and user_input.strip():
    time_now = datetime.now().strftime("%H:%M")

    st.session_state.chat.append(("You", user_input, time_now))

    with st.spinner("🤖 Typing..."):
        intent = st.session_state.bot.process_input(user_input)
        reply = st.session_state.bot.get_response(intent)

    st.session_state.chat.append(("Bot", reply, time_now))

    st.rerun()

# ---------------- FOOTER ----------------
st.markdown(
    "<div class='footer'>✨ Built with Python & Streamlit • Developed by Kotoju SaiChandana</div>",
    unsafe_allow_html=True
)
