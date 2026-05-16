# docsum/combiner.py

from pathlib import Path
import glob

from ..summarization.summarizer import summarize_combined

def combine_summaries(glob_pattern: str) -> tuple[str, list[Path]]:
    paths = [Path(p) for p in glob.glob(glob_pattern)]
    paths = sorted(paths, key=lambda p: p.name)

    if not paths:
        raise FileNotFoundError(f"No files matched pattern: {glob_pattern}")

    combined = []
    for p in paths:
        combined.append(f"\n\n---\n\n# Source: {p.name}\n\n")
        combined.append(p.read_text(encoding="utf-8", errors="ignore"))

    combined_text = "".join(combined)

    # Safety cap: summaries are usually small, but keep it bounded anyway
    combined_text = combined_text[:20000]

    final_summary = summarize_combined(combined_text)
    return final_summary, paths