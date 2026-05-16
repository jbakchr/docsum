# FEEDBACK.md

## Purpose

This document captures my thoughts, frustrations, and insights while developing and using the `docsum` project.

---

## ⚠️ Friction & Challenges

### 1. Manual Copy-Pasting is Slow

Currently, the workflow for summarizing an article is:

- Copy-paste a section under 3000 characters
- Run the CLI
- Repeat

For long articles (~27,000 characters), this results in ~9 repetitions.

#### 🧠 Insights

- This feels too slow and manual-heavy

#### 🔧 Ideas / Improvements

In some way code something that would take an entire article (one longer than 3000 characters) and some way help me "dissect" the article into smaller logical chunks with each chunk being less than 3000 characters in order to create good "sub"-summaries of an entire article

In a way this could just be some sort tool (incorporated in the "docsum" cli or not) that would take the entire text of the article and then provide me with details like the following which would make me know better how to create these chunks myself:

Let's assume this/such a tool could give me some overview like:

- Total text from H1: 30000 characters
- Total text within H2 sections of H1 section: 
  - 2 sections of 15000 characters each
- Total text within H3 sections with each H2 sections:
  - 8 sections of 1875 characters each

By knowing that each H3 section would be around 1875 each I would then know that each of these sections would be good for the current model summarize and that I would than have to create 16 separate sections of one entire article which would probably be good to both make separate summaries of and later ONE good final summary out these 16 smaller summaries.

---

### 2. Can Multiple Summaries Become One Good Summary?

A key question:

> Can multiple small summaries be combined into one useful final summary?

This is critical:

- If YES → the system becomes useful
- If NO → the workflow may not scale

#### 🧠 Insights

- Creating ONE good summary out of multiple summaries works surprisingly well!

---

### 3. Model Size & Quality

Concern:

- A small model (like llama3) might struggle with:
  - combining summaries
  - maintaining coherence

👉 A larger model might be needed for final summarization.

#### 🧠 Insights

- This how NOT been tested yet and for now using a smaller model still works good enough for making ONE summary out of multiple summaries.

---

## 🤔 Reflections on Learning Process

### 4. Should I Read Before Summarizing?

Important realization:

> If I don’t read the article myself first, how do I know the summaries are actually valuable?

This feels crucial.

---

### ✅ Revised Mental Model

A better process might be:

1. Read article
2. Decide: “Is this worth keeping?”
3. Then summarize (sections + final)

👉 This ensures quality in the knowledge base.

---

## ✅ What’s Working Well

### 5. Section-Based Summaries Work Surprisingly Well

Even without reading the full article:

- The 9 summaries are useful individually
- I can extract meaningful insights just from them

Examples:

- Take time to learn concepts
- Take notes
- Use visualization
- Ask “What / Why / How”

👉 This already provides value.

---

### 6. Combined Summary Feels Very Strong

The `combine` feature:

✅ Produces a clear, concise final summary  
✅ Captures the main idea well  
✅ Feels useful for learning and recall

👉 This is a big success.

---

## 🧠 Current Conclusion

- Section-based summaries ✅ useful
- Combined summary ✅ valuable
- Workflow ⚠️ still manual
- Reading-first approach ✅ likely important

👉 The project is already useful, but can be improved further.
