def build_prompt(text: str) -> str:
    return f"""
Summarize the following technical text clearly and concisely.

Provide output in this format:

TL;DR:
(2-3 sentences)

Key points:
- ...
- ...

Actionable insights:
- ...

TEXT:
{text}
"""