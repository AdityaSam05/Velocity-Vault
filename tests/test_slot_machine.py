import types

from main import SlotMachine


def test_check_wins_single_line_win():
    # Construct columns where first row across all columns is 'A' => win on line 1
    columns = [
        ["A", "B", "C"],
        ["A", "D", "C"],
        ["A", "B", "D"],
    ]
    slot = SlotMachine()
    winnings, winning_lines = slot.check_wins(columns, lines=1, bet=10)
    # Symbol 'A' default value is 5, bet 10 => winnings 50
    assert winnings == slot.symbol_values["A"] * 10
    assert winning_lines == [1]


def test_check_wins_multiple_lines():
    # Lines 1 and 3 win
    columns = [
        ["D", "X", "C"],
        ["D", "Y", "C"],
        ["D", "Z", "C"],
    ]
    slot = SlotMachine()
    winnings, winning_lines = slot.check_wins(columns, lines=3, bet=2)
    # Only symbol 'D' matches on line 1 and 'C' matches on line 3
    expected = slot.symbol_values["D"] * 2 + slot.symbol_values["C"] * 2
    assert winnings == expected
    assert winning_lines == [1, 3]


def test_get_spin_shape_and_symbols():
    slot = SlotMachine()
    cols = slot.get_spin()
    # Should be a list with COLS columns and each column should have ROWS entries
    assert isinstance(cols, list)
    assert len(cols) == slot.COLS
    for col in cols:
        assert len(col) == slot.ROWS
        for sym in col:
            assert sym in slot.symbol_counts
