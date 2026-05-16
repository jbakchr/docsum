# docsum 🧠

A simple AI-powered CLI tool for summarizing documents and building a personal knowledge base.

---

## ✨ Motivation

Reading long technical articles takes time and effort.

This project explores how to:

- Summarize content quickly using local LLMs
- Extract useful insights from long-form text
- Build a personal “second brain” for learning

---

## 🚀 Current Features

- 📄 Summarize text files (section-by-section)
- 🤖 Generate structured summaries using a local LLM (Ollama)
- 💾 Automatically save summaries as Markdown
- 🔗 Combine multiple summaries into one final, concise summary

---

## 🧱 Current Workflow (Actual Architecture)

This reflects how the tool is _actually used today_:

```

Article
↓
Manual sectioning (copy/paste)
↓
docsum summarize (per section)
↓
Saved summaries (.md)
↓
docsum combine
↓
Final combined summary

```

👉 This approach avoids LLM limitations with long inputs and produces higher quality summaries.

---

## 🧠 How It's Used

Example workflow:

1. Copy an article into smaller sections
2. Save as:

   ```
   data/raw/article\_part1.txt
   data/raw/article\_part2.txt
   ```

3. Summarize each part:

   ```bash
   python -m docsum.cli summarize data/raw/article_part1.txt
   ```

4. Combine all summaries:
   ```bash
   python -m docsum.cli combine "data/processed/article_part*.md"
   ```

---

## 🧪 Example Output

Each summary follows a consistent structure:

    TL;DR:
    ...

    Key points:
    - ...

    Actionable insights:
    - ...

---

## 📚 Real Example Walkthrough

This example shows how `docsum` is used in practice to summarize a real Python article.

### 📰 Source Article

“How to Conceptualize Python Fundamentals for Greater Mastery”  
(from Real Python)

---

### Step 1 – Split the Article

The article is manually divided into smaller sections (to avoid LLM input limits):

```
data/raw/
    how_to_conceptualize_python_fundamentals_part1.txt
    how_to_conceptualize_python_fundamentals_part2.txt
    ...
    how_to_conceptualize_python_fundamentals_part9.txt
```

Each file contains a natural section of the article (intro, step 1, step 2, etc.).

---

### Step 2 – Summarize Each Section

Run:

```bash
python -m docsum.cli summarize data/raw/how_to_conceptualize_python_fundamentals_part1.txt
```

Repeat for all parts.

This produces:

```
data/processed/
  how_to_conceptualize_python_fundamentals_part1.md
  ...
  how_to_conceptualize_python_fundamentals_part9.md
```

---

### Step 3 – Combine Summaries

Run:

```bash
python -m docsum.cli combine "data/processed/how_to_*_part*.md"
```

This generates a final combined summary:

```
data/processed/
    how_to_conceptualize_python_fundamentals_summary.md
```

---

### ✅ Final Combined Summary (Example)

```
TL;DR:
Master Python fundamentals by defining concepts in your own words, connecting them to real-world patterns, and applying understanding through practice.

Key points:
- Define Python concepts using "What", "Why", and "How"
- Connect concepts to real-world and software analogies
- Apply understanding through practice, comparison, and teaching

Actionable insights:
- Start with one concept and apply the 3-step framework
- Write definitions and use diagrams
- Reinforce knowledge by teaching or coding examples
```

---

### 🧠 What This Demonstrates

- High-quality summaries come from small, focused inputs
- Combining summaries produces a clear overall understanding
- The workflow scales to long articles without complexity

---

### 💡 Takeaway

Instead of trying to summarize long documents in one step:

👉 Break → Summarize → Combine

This produces better results and builds a reusable knowledge base.

---

## 🧠 Design Philosophy

This project intentionally:

- ✅ avoids large inputs (LLM limitation)
- ✅ favors small, high-quality summaries
- ✅ builds knowledge incrementally
- ✅ focuses on real usefulness over complexity

---

## 🗺️ Roadmap

### ✅ Done

- CLI summarizer
- Section-based workflow
- Save summaries to disk
- Combine summaries into final output

### ⏳ Next

- Better CLI UX (list, search)
- PDF / web content ingestion
- Automatic chunking (optional)
- Lightweight search over summaries
- Personal "second brain" features

---

## 🛠️ Tech Stack

- Python
- Local LLM via Ollama
- Requests (HTTP)
- Markdown for storage

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

### Summarize one file

```bash
python -m docsum.cli summarize data/raw/example.txt
```

### Combine summaries

```bash
python -m docsum.cli combine "data/processed/*.md"
```

---

## 🧠 Inspiration

This project explores how AI can:

- Reduce friction when learning
- Help retain knowledge
- Turn reading into structured insight

---

## 📄 License

MIT
