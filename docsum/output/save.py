# docsum/output/save.py

from pathlib import Path

def save_text(output_path: Path, content: str) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path


def save_summary(input_path: Path, content: str) -> Path:
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / (input_path.stem + ".md")

    formatted = f"# {input_path.stem}\n\n{content}\n"
    output_file.write_text(formatted, encoding="utf-8")
    return output_file