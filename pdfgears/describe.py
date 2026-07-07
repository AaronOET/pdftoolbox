#!/usr/bin/env python
"""
Command-line utility to display descriptions of pdfgears functionality.
"""

import argparse
from textwrap import dedent

TOOL_DESCRIPTIONS = {
    'rmbmk': """
        Remove PDF bookmarks (outline entries) whose title consists only of
        Arabic numerals (e.g. "1", "2.", "10").

        This tool reads one or more PDF files and rewrites their bookmark
        outline, dropping numeric-only entries while preserving the
        links/destinations of the remaining bookmarks. Children of a removed
        bookmark are promoted up a level. If -o/--output is omitted, the
        input file is overwritten and a .bak backup is kept.

        Examples:
            rmbmk -i input.pdf                 # Overwrite input.pdf, keep a .bak backup
            rmbmk -i input.pdf -o output.pdf   # Write result to output.pdf
            rmbmk -i *.pdf                      # Process every PDF matched by the shell glob
    """,
}


def main():
    parser = argparse.ArgumentParser(
        prog='pdfgears-info',
        description='Display descriptions of pdfgears commands',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        'tool',
        nargs='?',
        choices=list(TOOL_DESCRIPTIONS.keys()),
        help='Tool name to describe (omit to list all tools)',
    )
    args = parser.parse_args()

    if args.tool:
        print(f"\n--- {args.tool} ---")
        print(dedent(TOOL_DESCRIPTIONS[args.tool]))
    else:
        print("\nPDFGEARS — PDF utility commands\n")
        for tool, desc in TOOL_DESCRIPTIONS.items():
            first_line = dedent(desc).strip().splitlines()[0]
            print(f"  {tool:<14} {first_line}")
        print("\nRun 'pdfgears-info <tool>' for details on a specific command.")


if __name__ == "__main__":
    main()
