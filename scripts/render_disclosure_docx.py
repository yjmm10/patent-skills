#!/usr/bin/env python3
"""将交底书 Markdown 渲染为 A4 Word 文档（封装 tools/md_to_docx.py）。"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Render patent disclosure Markdown to A4 DOCX")
    parser.add_argument("--input", "-i", required=True, help="Input Markdown path")
    parser.add_argument("--output", "-o", required=True, help="Output DOCX path")
    parser.add_argument(
        "--base-dir",
        default=".",
        help="Base directory for resolving relative image paths",
    )
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parent.parent
    md_to_docx = skill_dir / "tools" / "md_to_docx.py"
    if not md_to_docx.is_file():
        print(f"error: md_to_docx.py not found at {md_to_docx}", file=sys.stderr)
        return 1

    cmd = [
        sys.executable,
        str(md_to_docx),
        "--input",
        args.input,
        "--output",
        args.output,
        "--base-dir",
        args.base_dir,
    ]
    return subprocess.call(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
