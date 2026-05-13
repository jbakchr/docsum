def build_prompt(text: str) -> str:
    return f"""
Summarize this technical article.

IMPORTANT:
- Identify any frameworks, steps, or structured approaches
- If the article contains a step-by-step method, list ALL steps clearly
- Focus on the overall structure, not just the first section

Return:

TL;DR:
(2-3 sentences, include the main framework if present)

Key points:
- core ideas
- include ALL major steps or sections

Actionable insights:
- practical actions based on the article

TEXT:
{text}
"""