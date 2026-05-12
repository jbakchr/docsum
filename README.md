# docsum 🧠

A simple AI-powered tool for summarizing documents and building a personal knowledge base.

## ✨ Motivation

Reading long documents (articles, tutorials, PDFs) takes time and effort.

This project explores how to:

- Automatically summarize documents using LLMs
- Extract useful insights from text
- (Eventually) build a personal "second brain"

---

## 🚀 Features (initial)

- 📄 Load text files or PDFs
- ✂️ Split content into chunks
- 🤖 Generate summaries using an LLM
- 📋 Output structured summaries

---

## 🧱 Architecture

```

Input → Parsing → Chunking → LLM → Summary

```

Planned extensions:

- Storage of summaries
- Search and retrieval
- Multi-document summarization
- Knowledge base ("second brain")

---

## 🛠️ Tech stack

- Python
- FastAPI (future)
- Local LLM (Ollama) or API (OpenAI)
- LangChain / custom pipeline

---

## 📦 Setup

```bash
git clone https://github.com/<your-username>/docsum.git
cd docsum

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## ⚙️ Usage

```bash
python -m docsum.cli summarize data/raw/example.txt
```

---

## 🧪 Example output

    TL;DR:
    This article explains how FastAPI handles async requests.

    Key points:
    - FastAPI uses async/await
    - Built on Starlette
    - Very fast performance

    Actionable insights:
    - Use async for I/O-bound tasks
    - Prefer FastAPI for APIs

---

## 🗺️ Roadmap

- [ ] CLI summarizer (MVP)
- [ ] PDF support
- [ ] Better prompts / output structure
- [ ] Save summaries to disk
- [ ] Search summaries
- [ ] Build "second brain"

---

## 🧠 Inspiration

This project explores how AI can:

- Reduce friction when learning
- Help retain knowledge
- Turn reading into structured insight

---

## 📄 License

MIT
