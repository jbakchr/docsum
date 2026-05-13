import requests

from .prompts import build_prompt
from .chunking import chunk_text

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"  # change if you want

def summarize(text: str):
    prompt = build_prompt(text)

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    data = response.json()

    return data["response"]


def summarize_long(text: str):
    chunks = chunk_text(text)

    summaries = []

    for chunk in chunks:
        summaries.append(summarize(chunk))

    combined = "\n\n".join(summaries)

    # Final "summary of summaries"
    return summarize(combined)