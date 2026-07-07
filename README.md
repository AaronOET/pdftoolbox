# PDFGEARS

A collection of Python tools for working with PDF files.

> Distributed on PyPI as **pdfgears**; the importable package is `pdfgears`.

## Installation

```bash
pip install pdfgears
```

## Features

- **rmbmk**: Remove PDF bookmarks (outline entries) whose title consists only of Arabic numerals (e.g. "1", "2.", "10"), while preserving the links/destinations of the remaining bookmarks.

## Usage

### Command-line

```bash
# List all available commands
pdfgears-info

# Remove numeric-only bookmarks, overwriting the input (keeps a .bak backup)
rmbmk -i input.pdf

# Remove numeric-only bookmarks, writing to a new file
rmbmk -i input.pdf -o output.pdf

# Process every PDF matched by the shell glob
rmbmk -i *.pdf
```

### Python API

```python
from pdfgears import rmbmk

# Remove numeric-only bookmarks from a PDF
rmbmk.remove_numeric_bookmarks("input.pdf", output_path="output.pdf")
```

## Notes

- `rmbmk` automatically creates a `.bak` backup of the original file whenever it overwrites it in place (i.e. when `-o/--output` is omitted).
- `-o/--output` can only be used with a single `-i` input file.
