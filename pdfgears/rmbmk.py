#!/usr/bin/env python3
"""
rmbmk - Remove numeric-only PDF bookmarks (outline entries)
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

NUMERIC_ONLY_RE = re.compile(r"^\d+[.。]?$")


def is_numeric_only(title: str) -> bool:
    """Return True if `title` is only digits, with an optional trailing '.'/'。'."""
    return bool(NUMERIC_ONLY_RE.match(title.strip()))


def remove_numeric_bookmarks(input_path, output_path=None):
    """
    Remove numeric-only bookmarks from a PDF, preserving the rest of the outline.

    Args:
        input_path: Path to the input PDF.
        output_path: Path to write the result to (defaults to overwriting
            `input_path`, keeping a `.bak` backup of the original).

    Returns:
        The Path the result was written to.
    """
    input_path = Path(input_path)
    output_path = Path(output_path) if output_path else input_path

    reader = PdfReader(str(input_path))
    writer = PdfWriter()
    writer.append(reader, import_outline=False)

    def clone_outline(items, parent=None):
        # A list immediately following an item in pypdf's outline tree holds
        # that item's children, so track the most recently created node to
        # use as the parent for such a list. If the item was skipped
        # (numeric-only), its children are promoted to `parent` instead.
        last_node = parent
        for item in items:
            if isinstance(item, list):
                clone_outline(item, last_node)
                continue
            if is_numeric_only(item.title):
                last_node = parent
                continue
            # Use `reader` (not `writer`) to resolve the page index: item.page
            # is a page object from the original reader, and since append()
            # clones every page in order, that same index is valid in writer.pages.
            page_number = reader.get_page_number(item.page.get_object())
            last_node = writer.add_outline_item(title=item.title, page_number=page_number, parent=parent)

    clone_outline(reader.outline)

    if output_path == input_path:
        backup_path = input_path.with_suffix(input_path.suffix + ".bak")
        shutil.copy2(input_path, backup_path)
        print(f"  Backup saved to {backup_path}")

    with open(output_path, "wb") as f:
        writer.write(f)

    print(f"  Wrote {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        prog="rmbmk",
        description=(
            "Remove PDF bookmarks (outline entries) whose title consists only "
            'of Arabic numerals (e.g. "1", "2.", "10"), while preserving the '
            "links/destinations of the remaining bookmarks."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  rmbmk input.pdf                    # Overwrite input.pdf, keep a .bak backup
  rmbmk input.pdf -o output.pdf      # Write result to output.pdf
  rmbmk *.pdf                        # Process every PDF matched by the shell glob
  rmbmk **/*.pdf                     # Recurse into subdirectories (enable globstar first, e.g. `shopt -s globstar` in bash)
        """,
    )
    parser.add_argument(
        "input",
        nargs="+",
        metavar="FILE",
        type=Path,
        help="One or more input PDF files (shell globs like *.pdf are expanded by the shell)",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        metavar="FILE",
        help="Output PDF path (only valid with a single input file; defaults to overwriting the input)",
    )
    args = parser.parse_args()

    if args.output and len(args.input) > 1:
        print("Error: -o/--output can only be used with a single input file.", file=sys.stderr)
        sys.exit(2)

    exit_code = 0
    for input_path in args.input:
        if not input_path.is_file():
            print(f"Error: File not found: {input_path}", file=sys.stderr)
            exit_code = 1
            continue

        print(f"Processing: {input_path}")
        try:
            remove_numeric_bookmarks(input_path, args.output)
        except Exception as e:
            print(f"  Error: {e}", file=sys.stderr)
            exit_code = 1

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
