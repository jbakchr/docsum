from pathlib import Path
from docsum.summarization.summarizer import summarize
from docsum.output.save import save_summary


def summarize_batch(input_path: str):
    path = Path(input_path)

    if not path.exists():
        print(f"Path not found: {path}")
        return

    # Collect all .txt files
    if path.is_file():
        files = [path]
    else:
        files = sorted(path.glob("*.txt"))

    if not files:
        print("No .txt files found")
        return

    print(f"\nFound {len(files)} files\n")

    for i, file in enumerate(files, 1):
        print(f"[{i}/{len(files)}] Processing: {file.name}")

        text = file.read_text(encoding="utf-8", errors="ignore")

        # Keep your safe limit
        text = text[:3000]

        result = summarize(text)

        save_path = save_summary(file, result)

        print(f"Saved → {save_path}\n")

    print("✅ Batch summarization completed\n")