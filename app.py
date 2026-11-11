"""
Streamlit UI for the Acme Cloud RAG assistant.

Run with:
    streamlit run app.py
"""

import os

os.environ.setdefault("USE_TF", "0")

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from rag_core import SYSTEM_PROMPT, CHAT_MODEL, EMBEDDING_MODEL

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Acme Cloud Assistant", page_icon="☁️", layout="centered")

st.title("☁️ Acme Cloud Assistant")
st.caption(f"Model: `{CHAT_MODEL}` · Embeddings: `{EMBEDDING_MODEL}`")

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input(
        "Groq API Key",
        value=os.getenv("GROQ_API_KEY", ""),
        type="password",
        placeholder="gsk_...",
    )
    st.markdown("[Get a free Groq API key →](https://console.groq.com/keys)")
    st.markdown("---")
    st.subheader("System Prompt")
    st.code(SYSTEM_PROMPT, language=None)
    st.markdown("---")
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

# ── Check API key ────────────────────────────────────────────────────────────
if not api_key:
    st.info("👈 Enter your **Groq API Key** in the sidebar to get started.")
    st.stop()

# Set for the Groq SDK to pick up
os.environ["GROQ_API_KEY"] = api_key

# ── Build the RAG graph (cached per api_key) ─────────────────────────────────
@st.cache_resource(show_spinner="Loading model and documents…")
def get_app(_key: str):
    from rag_core import build_rag_graph
    return build_rag_graph()

rag_app = get_app(api_key)

# ── Chat history ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("📄 Sources"):
                for src in msg["sources"]:
                    st.markdown(f"- **{src}**")

# ── User input ───────────────────────────────────────────────────────────────
if question := st.chat_input("Ask a question about Acme Cloud…"):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            result = rag_app.invoke({"question": question})

        answer = result["answer"]
        sources = [d.metadata["title"] for d in result["context"]]

        st.markdown(answer)
        with st.expander("📄 Sources"):
            for src in sources:
                st.markdown(f"- **{src}**")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": sources}
    )
