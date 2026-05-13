import sys
from pathlib import Path

from .summarizer import summarize

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

if __name__ == "__main__":
    main()