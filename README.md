# 🛡️ AI Safety & LLM Security

Hands-on tutorials exploring **LLM security risks** from the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/), built with **LangGraph** and powered by **Groq**.

We build a small RAG chatbot for a fictional company called **Acme Cloud**, then attack and defend it module by module.

---

## 📸 Demo

The Streamlit web app provides a simple chat interface to interact with the RAG assistant:

```
☁️ Acme Cloud Assistant
├── Chat with the assistant about Acme Cloud policies
├── View retrieved source documents for every answer
└── Enter your Groq API key in the sidebar to get started
```

---

## 🏗️ Architecture

```
User question ──► Retrieve (vector store) ──► Build prompt ──► LLM (Groq) ──► Answer
                                               • system prompt
                                               • retrieved passages
                                               • user message
```

| Component       | Technology                                              |
| --------------- | ------------------------------------------------------- |
| LLM             | `openai/gpt-oss-120b` via [Groq](https://groq.com/)    |
| Embeddings      | `all-MiniLM-L6-v2` (local, HuggingFace)                |
| Orchestration   | [LangGraph](https://langchain-ai.github.io/langgraph/) |
| Vector Store    | LangChain `InMemoryVectorStore`                         |
| Web UI          | [Streamlit](https://streamlit.io/)                      |

---

## 📁 Project Structure

```
Ai-Safety-And-LLM-Security/
├── app.py                    # Streamlit web app
├── rag_core.py               # RAG pipeline (graph + retriever + generator)
├── fake_docs.py              # Fake Acme Cloud knowledge base (public docs)
├── confidential_docs.py      # Sensitive docs for security modules
├── 01_basic_rag.ipynb        # Module 1: Build the baseline RAG app
├── 02_prompt_injection.ipynb # Module 2: Prompt injection attacks
├── example.env               # Template for environment variables
├── requirements.txt          # Python dependencies
├── LICENSE                   # GPL-3.0
└── .gitignore
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/Ai-Safety-And-LLM-Security.git
cd Ai-Safety-And-LLM-Security
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Copy the example env file and add your [Groq API key](https://console.groq.com/keys) (free):

```bash
cp example.env .env
```

Edit `.env`:

```env
GROQ_API_KEY=gsk_your_key_here
```

> **Tip:** You can also enter the key directly in the Streamlit sidebar — no `.env` file needed.

### 4. Run the web app

```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

### 5. Run the notebooks

```bash
jupyter notebook
```

| Notebook                     | Topic                          |
| ---------------------------- | ------------------------------ |
| `01_basic_rag.ipynb`         | Build the baseline RAG app     |
| `02_prompt_injection.ipynb`  | LLM01 — Prompt injection attacks |

---

## ⚙️ Configuration

All settings are optional overrides in `.env`:

| Variable          | Default                 | Description                        |
| ----------------- | ----------------------- | ---------------------------------- |
| `GROQ_API_KEY`    | *(required)*            | Your Groq API key                  |
| `GROQ_MODEL`      | `openai/gpt-oss-120b`  | Chat model served by Groq          |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2`     | HuggingFace embedding model (local)|

---

## 🔒 Security Modules

Each module targets a specific OWASP LLM risk using the same baseline app:

| Module | OWASP Risk | What happens |
| ------ | ---------- | ------------ |
| **01** | — | Build the RAG app (baseline) |
| **02** | LLM01 Prompt Injection | Direct & indirect injection attacks |
| *03+*  | *Coming soon* | Guardrails, data poisoning, sensitive info disclosure, etc. |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-module`)
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the [GPL-3.0 License](LICENSE).
