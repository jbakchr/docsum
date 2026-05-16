# docsum/prompts.py

def build_prompt(text: str) -> str:
    # v1 prompt (your best so far)
    return f"""
Summarize the following text.

Provide output in this format:

TL;DR:
...

Key points:
- ...
- ...

Actionable insights:
- ...

TEXT:
{text}
"""


def build_combine_prompt(section_summaries_md: str) -> str:
    # v1-style, but explicitly for "summaries of sections"
    return f"""
You are given multiple section summaries of one longer article.
Create ONE consolidated summary that:
- removes duplicates
- preserves the overall 3-step structure if present
- stays concise

Provide output in this format:

TL;DR:
...

Key points:
- ...
- ...

Actionable insights:
- ...

SECTION SUMMARIES:
{section_summaries_md}
"""