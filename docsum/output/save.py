from pathlib import Path

def save_summary(input_path: Path, content: str):
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / (input_path.stem + ".md")

    formatted = f"""# {input_path.stem}

{content}
"""

    output_file.write_text(formatted)

    return output_file
