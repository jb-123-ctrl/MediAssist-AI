import streamlit as st

from llm.gemini import get_ai_response
from memory.memory import (
    add_message,
    get_chat_history,
    initialize_memory,
)
from safety.emergency import EMERGENCY_MESSAGE, is_emergency


st.set_page_config(
    page_title="MediAssist AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize_memory(st.session_state)

if "emergency_count" not in st.session_state:
    st.session_state["emergency_count"] = 0


CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #f4f7fb;
    --surface: rgba(255, 255, 255, 0.82);
    --surface-strong: #ffffff;
    --ink: #122033;
    --muted: #64748b;
    --line: rgba(15, 23, 42, 0.10);
    --brand: #0f766e;
    --brand-2: #2563eb;
    --danger: #dc2626;
    --shadow: 0 24px 70px rgba(15, 23, 42, 0.10);
}

html, body, [class*="css"] {
    font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(14, 165, 233, 0.18), transparent 34rem),
        radial-gradient(circle at top right, rgba(20, 184, 166, 0.16), transparent 30rem),
        linear-gradient(135deg, #eef7fb 0%, #f8fafc 46%, #f2f7f4 100%);
}

.block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 5.5rem;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(15, 118, 110, 0.94), rgba(15, 23, 42, 0.96));
    border-right: 1px solid rgba(255, 255, 255, 0.20);
    box-shadow: 18px 0 50px rgba(15, 23, 42, 0.16);
}

section[data-testid="stSidebar"] * {
    color: #f8fafc !important;
}

section[data-testid="stSidebar"] [data-testid="stMetric"] {
    background: rgba(255, 255, 255, 0.10);
    border: 1px solid rgba(255, 255, 255, 0.16);
    border-radius: 16px;
    padding: 0.8rem 0.9rem;
    backdrop-filter: blur(18px);
}

section[data-testid="stSidebar"] .stButton button,
section[data-testid="stSidebar"] .stDownloadButton button {
    border-radius: 999px;
    border: 1px solid rgba(255, 255, 255, 0.22);
    background: rgba(255, 255, 255, 0.12);
    color: #ffffff;
    font-weight: 700;
    transition: all 180ms ease;
}

section[data-testid="stSidebar"] .stButton button:hover,
section[data-testid="stSidebar"] .stDownloadButton button:hover {
    transform: translateY(-1px);
    border-color: rgba(255, 255, 255, 0.44);
    background: rgba(255, 255, 255, 0.18);
}

.hero {
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(15, 23, 42, 0.08);
    border-radius: 28px;
    padding: 2.2rem;
    background:
        linear-gradient(135deg, rgba(255, 255, 255, 0.90), rgba(255, 255, 255, 0.62)),
        linear-gradient(120deg, rgba(37, 99, 235, 0.14), rgba(20, 184, 166, 0.18));
    box-shadow: var(--shadow);
    animation: riseIn 520ms ease both;
}

.hero h1 {
    margin: 0;
    color: var(--ink);
    font-size: 2.6rem;
    line-height: 1.04;
    letter-spacing: 0;
}

.hero p {
    max-width: 760px;
    margin: 0.85rem 0 1.2rem;
    color: var(--muted);
    font-size: 1.02rem;
    line-height: 1.7;
}

.hero-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 0.65rem;
}

.badge {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    border: 1px solid rgba(15, 23, 42, 0.09);
    border-radius: 999px;
    padding: 0.48rem 0.75rem;
    background: rgba(255, 255, 255, 0.72);
    color: #164e63;
    font-size: 0.86rem;
    font-weight: 700;
}

.stat-card,
.suggestion-card,
.emergency-card,
.footer-card {
    border: 1px solid var(--line);
    border-radius: 22px;
    background: var(--surface);
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
    backdrop-filter: blur(18px);
}

.stat-card {
    min-height: 126px;
    padding: 1.15rem;
    animation: riseIn 560ms ease both;
}

.stat-label {
    color: var(--muted);
    font-size: 0.82rem;
    font-weight: 800;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.stat-value {
    margin-top: 0.35rem;
    color: var(--ink);
    font-size: 2rem;
    font-weight: 800;
}

.stat-note {
    margin-top: 0.3rem;
    color: #0f766e;
    font-size: 0.88rem;
    font-weight: 700;
}

.section-title {
    margin: 1.8rem 0 0.7rem;
    color: var(--ink);
    font-size: 1.3rem;
    font-weight: 800;
}

.suggestion-card {
    min-height: 130px;
    padding: 1rem;
    margin-bottom: 0.65rem;
    transition: transform 180ms ease, box-shadow 180ms ease;
}

.suggestion-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 22px 60px rgba(15, 23, 42, 0.12);
}

.suggestion-card h3 {
    margin: 0 0 0.45rem;
    color: var(--ink);
    font-size: 1rem;
}

.suggestion-card p {
    margin: 0;
    color: var(--muted);
    font-size: 0.9rem;
    line-height: 1.55;
}

.stButton button {
    border-radius: 14px;
    border: 1px solid rgba(15, 118, 110, 0.18);
    background: #ffffff;
    color: #0f172a;
    font-weight: 700;
    min-height: 2.75rem;
    transition: all 180ms ease;
}

.stButton button:hover {
    border-color: rgba(15, 118, 110, 0.48);
    box-shadow: 0 12px 30px rgba(15, 118, 110, 0.12);
    transform: translateY(-1px);
}

div[data-testid="stChatMessage"] {
    border-radius: 22px;
    border: 1px solid rgba(15, 23, 42, 0.08);
    box-shadow: 0 14px 36px rgba(15, 23, 42, 0.08);
    animation: riseIn 360ms ease both;
}

div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(135deg, #eaf5ff, #ffffff);
}

div[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(135deg, #ffffff, #effdf8);
}

.chat-name {
    margin-bottom: 0.35rem;
    color: var(--ink);
    font-weight: 800;
}

.emergency-card {
    padding: 1rem 1.1rem;
    margin: 0.8rem 0 1rem;
    border-color: rgba(220, 38, 38, 0.28);
    background: linear-gradient(135deg, rgba(254, 242, 242, 0.96), rgba(255, 255, 255, 0.88));
}

.emergency-card h3 {
    margin: 0 0 0.4rem;
    color: #991b1b;
    font-size: 1rem;
}

.emergency-card p {
    margin: 0;
    color: #7f1d1d;
    line-height: 1.55;
}

.footer-card {
    margin-top: 2rem;
    padding: 1.2rem;
    text-align: center;
    color: var(--muted);
}

.footer-card strong {
    color: var(--ink);
}

@keyframes riseIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (max-width: 760px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .hero {
        padding: 1.35rem;
        border-radius: 20px;
    }

    .hero h1 {
        font-size: 2rem;
    }

    .stat-card,
    .suggestion-card {
        border-radius: 18px;
    }
}
</style>
"""


def render_stat_card(label, value, note):
    st.markdown(
        f"""
        <div class="stat-card">
            <div class="stat-label">{label}</div>
            <div class="stat-value">{value}</div>
            <div class="stat-note">{note}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_suggestion_card(title, description, key, prompt):
    st.markdown(
        f"""
        <div class="suggestion-card">
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("Ask this", key=key, width="stretch"):
        st.session_state["suggested_prompt"] = prompt
        st.rerun()


def render_chat_message(message):
    if message["role"] == "user":
        with st.chat_message("user", avatar="🙂"):
            st.markdown('<div class="chat-name">You</div>', unsafe_allow_html=True)
            st.write(message["content"])
    else:
        with st.chat_message("assistant", avatar="🏥"):
            st.markdown(
                '<div class="chat-name">MediAssist AI</div>',
                unsafe_allow_html=True,
            )
            st.markdown(message["content"])


def render_emergency_card():
    st.markdown(
        f"""
        <div class="emergency-card">
            <h3>🚨 Emergency alert</h3>
            <p>{EMERGENCY_MESSAGE}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if st.session_state.get("suggested_prompt"):
    prompt = st.session_state.pop("suggested_prompt")
else:
    prompt = None

history = get_chat_history(st.session_state)
question_count = sum(1 for msg in history if msg["role"] == "user")
assistant_count = sum(1 for msg in history if msg["role"] == "assistant")
emergency_count = st.session_state.get("emergency_count", 0)

with st.sidebar:
    st.markdown("## 🏥 MediAssist AI")
    st.caption("Clinical education assistant")

    st.markdown("### System")
    st.badge("LLM online", icon=":material/check_circle:", color="green")
    st.badge("Memory active", icon=":material/forum:", color="blue")
    st.badge("RAG loaded", icon=":material/database:", color="green")
    st.badge("Emergency scan on", icon=":material/emergency:", color="red")

    st.markdown("### Session")
    st.metric("Questions asked", question_count)
    st.metric("Emergency alerts", emergency_count)

    if st.button("🧹 Clear chat", width="stretch"):
        st.session_state.messages = []
        st.session_state["emergency_count"] = 0

        if "suggested_prompt" in st.session_state:
            del st.session_state["suggested_prompt"]

        st.toast("Chat history cleared successfully.")
        st.rerun()

    chat_text = ""
    for msg in history:
        chat_text += f"{msg['role'].capitalize()}:\n{msg['content']}\n\n"

    st.download_button(
        "📄 Download chat",
        data=chat_text,
        file_name="chat_history.txt",
        mime="text/plain",
        width="stretch",
    )

    with st.expander("About MediAssist AI", icon=":material/info:"):
        st.write(
            """
            MediAssist AI explains health topics using Groq Llama 3.3,
            conversation memory, FAISS retrieval, references, and emergency
            symptom detection.
            """
        )

    st.markdown("### 👩‍💻 Developer")
    st.write("**Jayabharathi S**")
    st.caption("Version 1.0")

st.markdown(
    """
    <section class="hero">
        <h1>MediAssist AI</h1>
        <p>
            A modern healthcare assistant for clear medical education,
            source-aware answers, and immediate emergency guidance.
        </p>
        <div class="hero-badges">
            <span class="badge">🏥 Healthcare focused</span>
            <span class="badge">📚 Knowledge base grounded</span>
            <span class="badge">🚨 Emergency aware</span>
            <span class="badge">🤖 Llama 3.3 powered</span>
        </div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.space("small")

stat_cols = st.columns(4)
with stat_cols[0]:
    render_stat_card("Questions", question_count, "Asked in this session")
with stat_cols[1]:
    render_stat_card("Responses", assistant_count, "Generated by MediAssist")
with stat_cols[2]:
    render_stat_card("Alerts", emergency_count, "Emergency checks triggered")
with stat_cols[3]:
    render_stat_card("Knowledge", "Loaded", "FAISS healthcare base")

chat_prompt = st.chat_input(
    "Ask a healthcare question...",
    key="chat_input",
    submit_mode="disable",
)

if chat_prompt:
    prompt = chat_prompt

if len(history) == 0 and prompt is None:
    st.markdown('<div class="section-title">Suggested questions</div>', unsafe_allow_html=True)

    q_cols = st.columns(4)
    with q_cols[0]:
        render_suggestion_card(
            "🌡️ Fever basics",
            "Understand common causes, warning signs, and when to seek care.",
            "suggest_fever",
            "What causes fever?",
        )
    with q_cols[1]:
        render_suggestion_card(
            "🥗 Healthy foods",
            "Get practical nutrition ideas for balanced everyday eating.",
            "suggest_foods",
            "What foods are healthy?",
        )
    with q_cols[2]:
        render_suggestion_card(
            "🩺 Diabetes symptoms",
            "Learn common symptoms and when professional evaluation matters.",
            "suggest_diabetes",
            "What are the symptoms of diabetes?",
        )
    with q_cols[3]:
        render_suggestion_card(
            "🔥 Burns first aid",
            "Review safe first-aid steps and urgent red flags.",
            "suggest_burns",
            "What is first aid for burns?",
        )

st.markdown('<div class="section-title">Conversation</div>', unsafe_allow_html=True)

for message in history:
    render_chat_message(message)

if prompt:
    add_message(st.session_state, "user", prompt)

    with st.chat_message("user", avatar="🙂"):
        st.markdown('<div class="chat-name">You</div>', unsafe_allow_html=True)
        st.write(prompt)

    if is_emergency(prompt):
        st.session_state["emergency_count"] = (
            st.session_state.get("emergency_count", 0) + 1
        )
        render_emergency_card()

    chat_history = get_chat_history(st.session_state)

    with st.chat_message("assistant", avatar="🏥"):
        st.markdown('<div class="chat-name">MediAssist AI</div>', unsafe_allow_html=True)
        with st.spinner("Thinking through the safest answer..."):
            response = get_ai_response(prompt, chat_history)
        st.markdown(response)

    add_message(st.session_state, "assistant", response)

st.markdown(
    """
    <footer class="footer-card">
        <strong>Powered by</strong><br>
        Groq · Llama 3.3 · LangChain · FAISS · Streamlit<br><br>
        Version 1.0<br>
        © 2026 Jayabharathi S
    </footer>
    """,
    unsafe_allow_html=True,
)
