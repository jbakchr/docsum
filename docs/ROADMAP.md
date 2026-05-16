# ROADMAP.md

## 🎯 Purpose

This roadmap is derived from real usage and reflections in `FEEDBACK.md`.

It focuses on:

- Reducing friction
- Improving usefulness
- Gradually evolving `docsum` into a personal "second brain"

---

# ✅ Current State (Baseline)

## What works well

- Section-based summarization ✅
- Local LLM integration ✅
- Consistent output format ✅
- Combine feature ✅ (high value)

## Core workflow

```

Article → Sections → Summaries → Combined Summary

```

---

# ⚠️ Current Friction

## 1. Manual chunking is slow

- Copy-paste per section is repetitive
- ~9 runs per article feels heavy

👉 This is the **biggest friction point**

---

## 2. Workflow feels semi-manual

- No automation for ingesting articles
- No way to quickly process full documents

---

## 3. Trust / validation issue

- If I don’t read the article:
  - I don’t know if summaries are good
  - Risk of storing low-value knowledge

---

# 🧠 Key Insights (from FEEDBACK)

## Insight 1: Smaller inputs → better output

- Section-based summaries outperform full-article summaries
- This is a core design principle

---

## Insight 2: Combine step is valuable

- Final summary gives:
  - clarity
  - recall
  - structure

👉 Keep this as a core feature

---

## Insight 3: Reading matters

> Summarizing ≠ learning (by itself)

Better workflow:

```

Read → Evaluate → Summarize → Store

```

---

## Insight 4: Summaries are useful even without full reading

- Can extract useful learning patterns
- But depth is limited

👉 Use summaries as:

- reinforcement ✅
- not replacement ❌

---

# 🚀 Roadmap

---

## ✅ Phase 1 — Stabilization (NOW)

Focus: clean, reliable, usable

- [x] CLI summarization
- [x] Save summaries to disk
- [x] Combine summaries
- [x] Clean project structure
- [x] Improve README

---

## 🔧 Phase 2 — Reduce Friction (NEXT)

Focus: remove manual pain

### High priority

- [ ] Semi-automatic chunking
  - detect sections from text
  - or split by headers

- [ ] Batch summarization
  - run summarize on all files in folder
  - e.g.:
    ```
    docsum summarize-batch data/raw/
    ```

---

### Medium priority

- [ ] Improve CLI UX
  - cleaner commands
  - better output messages

---

## 🧠 Phase 3 — Knowledge System

Focus: make summaries usable long-term

### High priority

- [ ] List summaries

  ```
  docsum list
  ```

- [ ] Search summaries (basic)
  ```
  docsum search "variables"
  ```

---

### Medium priority

- [ ] Add metadata to summaries
  - title
  - source
  - tags

---

## 🔗 Phase 4 — Input Improvements

Focus: reduce manual ingestion

- [ ] Load from URL (basic scraping)
- [ ] Clean HTML → text
- [ ] Optional PDF support

---

## 🚀 Phase 5 — Second Brain Features

Focus: real value layer

- [ ] Cross-summary summarization
      → summarize multiple articles

- [ ] Topic-based grouping
- [ ] Lightweight "knowledge base"

---

# 🧪 Experiments (Optional)

These are ideas — not commitments

- [ ] Try larger models for combine step
- [ ] Compare prompt variations
- [ ] Try automatic vs manual chunking

---

# ✅ Guiding Principles

## 1. Usefulness > Perfection

If it’s useful now → keep it  
Don’t over-engineer

---

## 2. Small inputs win

Prefer:

- structured
- section-based
- iterative processing

---

## 3. Human in the loop

You decide:

- what to read
- what to keep

AI supports — not replaces

---

## 4. Build from real usage

Only add features when:

- you feel the pain
- or it blocks you

---

# ✅ Current Priority

👉 Reduce friction in summarization workflow

Specifically:

- automate chunking OR
- batch process files

---

# 🧠 Long-Term Vision

Turn this into:

> A personal system for turning reading into structured knowledge

---
