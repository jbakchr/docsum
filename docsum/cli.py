# docsum/cli.py

import sys
from pathlib import Path
import argparse

from .summarization.summarizer import summarize
from .combine.combiner import combine_summaries
from .output.save import save_summary, save_text
from .commands.batch import summarize_batch

DEFAULT_LIMIT = 3000


def cmd_summarize(args):
    file_path = Path(args.file)

    if not file_path.exists():
        print("File not found")
        return 2

    text = file_path.read_text(encoding="utf-8", errors="ignore")
    print(f"Text length: {len(text)}")

    sys.exit(1)

    if args.limit is not None:
        text = text[:args.limit]

    result = summarize(text)

    print("\n" + "=" * 40)
    print(result)
    print("=" * 40 + "\n")

    out_path = save_summary(file_path, result)
    print(f"Saved summary to: {out_path}")
    return 0


def cmd_combine(args):
    final_summary, paths = combine_summaries(args.glob)

    header = f"# Combined summary\n\n"
    header += f"Sources ({len(paths)} files):\n"
    for p in paths:
        header += f"- {p.as_posix()}\n"
    header += "\n---\n\n"

    output_content = header + final_summary + "\n"

    out_path = Path(args.out)
    save_text(out_path, output_content)

    print("\n" + "=" * 40)
    print(final_summary)
    print("=" * 40 + "\n")
    print(f"Saved combined summary to: {out_path}")
    return 0


def cmd_summarize_batch(args):
    summarize_batch(args.path)
    return 0


def build_parser():
    parser = argparse.ArgumentParser(prog="docsum")
    sub = parser.add_subparsers(dest="command")

    # ✅ Summarize single file
    p_sum = sub.add_parser("summarize", help="Summarize a single file")
    p_sum.add_argument("file")
    p_sum.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    p_sum.set_defaults(func=cmd_summarize)

    # ✅ Combine summaries
    p_combine = sub.add_parser(
        "combine", help="Combine multiple saved summaries into one final summary"
    )
    p_combine.add_argument(
        "glob", help='Glob pattern, e.g. "data/processed/*.md"'
    )
    p_combine.add_argument(
        "--out", default="data/processed/_combined_summary.md"
    )
    p_combine.set_defaults(func=cmd_combine)

    # ✅ NEW: Batch summarization
    p_batch = sub.add_parser(
        "summarize-batch", help="Summarize all .txt files in a folder"
    )
    p_batch.add_argument(
        "path", help="Path to folder or file (e.g. data/raw/)"
    )
    p_batch.set_defaults(func=cmd_summarize_batch)

    return parser


def main():
    parser = build_parser()

    # Backwards compatibility:
    # If user runs: python -m docsum.cli somefile.txt
    if len(sys.argv) >= 2 and sys.argv[1] not in (
        "summarize",
        "combine",
        "summarize-batch",
        "-h",
        "--help",
    ):
        args = parser.parse_args(
            ["summarize", sys.argv[1], "--limit", str(DEFAULT_LIMIT)]
        )
        return args.func(args)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())