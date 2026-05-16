# docsum/summarizer.py

import requests
from .prompts import build_prompt, build_combine_prompt

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"  # change if needed, e.g. "llama3:8b" or "mistral"

def _ollama_generate(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            # These options keep outputs bounded and help avoid "takes forever"
            "options": {
                "temperature": 0.2,
                "num_predict": 450,   # cap output tokens-ish
            }
        },
        timeout=600,  # hard stop (seconds) so it can't hang forever
    )
    response.raise_for_status()
    return response.json()["response"]


def summarize(text: str) -> str:
    prompt = build_prompt(text)
    return _ollama_generate(prompt)


def summarize_combined(section_summaries_md: str) -> str:
    prompt = build_combine_prompt(section_summaries_md)
    return _ollama_generate(prompt)