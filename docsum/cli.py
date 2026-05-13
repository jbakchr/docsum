import sys
from pathlib import Path

from .summarizer import summarize
from .output.save import save_summary

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m docsum.cli <file>")
        return

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print("File not found")
        return

    text = file_path.read_text()

    print(f"Text length: {len(text)}")

    result = summarize(text[:3000])

    print("\n" + "="*40)
    print(result)
    print("="*40 + "\n")

    # ✅ Save summary
    output_path = save_summary(file_path, result)

    print(f"Saved summary to: {output_path}")

if __name__ == "__main__":
    main()