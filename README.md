# Velocity-Vault

Velocity-Vault is a compact, terminal-based slot machine game written in Python. It lets players deposit a balance, place bets across multiple lines, and spin a 3x3 slot machine with configurable symbols and payouts. The project is intentionally small and easy to extend for learning or hobby purposes.

## Features
- Terminal/console game (no GUI required)
- Customizable symbol counts and payout values
- Input validation and friendly prompts
- Simple, readable code aimed at easy modification

## Requirements
- Python 3.7+

## Quick start
1. Clone the repository or download the files.
2. (Optional) Create and activate a virtual environment (PowerShell on Windows):

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Run the game:

   python main.py

4. Follow on-screen prompts to deposit money, choose lines to bet on, place bets, and spin.

Notes:
- The default currency symbol is set to `₹` in `main.py`. Change `CURRENCY` in the `SlotMachine` class if you'd like a different symbol.

## Project structure
- `main.py` — primary game code and entrypoint
- `LICENSE` — MIT license
- `README.md` — this file

## Configuration & extension ideas
- Adjust `DEFAULT_SYMBOL_COUNTS` and `DEFAULT_SYMBOL_VALUES` in `SlotMachine` to change game balance and odds.
- Add persistent save/load of player balance to implement long-term play.
- Add logging and per-round statistics for analysis or a simple leaderboard.

## Contributing
Small, focused contributions are welcome. A few guidelines:
- Open an issue first if you plan a non-trivial change.
- Keep changes small and add a short description in pull requests.
- Add tests or a quick manual test note for behavior changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
If you have questions or suggestions, open an issue in the repository.
