# Changelog

All notable changes to this project are documented in this file. This project follows a simple, human-readable changelog format.

## [Unreleased]

### 2025-11-19
- Docs: Rewrote and cleaned `README.md` (removed duplicates and stray formatting). Added Quick Start, Requirements, Project Structure, and Contribution notes.
- Repo hygiene: Added and normalized `.gitignore` for Python/Windows/IDEs.
- Code: Removed duplicated `main()` function in `main.py` to leave a single, clear entry point.
- Tests: Added `tests/test_slot_machine.py` with deterministic unit tests for `SlotMachine.check_wins` and `get_spin`.
- Dev: Added `requirements.txt` (pytest)

## [2025-11-18]
- Initial project files (basic slot machine implementation) — original code and README.

---

Notes:
- Use the `Unreleased` section for ongoing changes. When releasing a new version, move the relevant entries into a dated section (e.g., `## [2025-11-19]`) and add a release header.
