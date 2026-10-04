# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2026-10-04

### Changed

- `rmbmk` now takes input files as positional arguments (`rmbmk input.pdf`); the `-i`/`--input` flag has been removed.

## [0.1.1] - 2026-08-05

### Added

- Recursive-glob example in `rmbmk --help`.

## [0.1.0] - 2026-07-07

### Added

- Initial `pdfgears` package.
- `rmbmk` CLI to remove numeric-only PDF bookmarks (outline entries) while preserving the rest of the outline.
- `pdfgears-info` / `describe` CLI to inspect PDF files.
- `pdfgears` umbrella CLI entry point.

[Unreleased]: https://github.com/AaronOET/pdftoolbox/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/AaronOET/pdftoolbox/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/AaronOET/pdftoolbox/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/AaronOET/pdftoolbox/releases/tag/v0.1.0
