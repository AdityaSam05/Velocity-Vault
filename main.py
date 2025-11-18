
import random


class SlotMachine:
    def get_number_of_lines(self):
        """
        Asks the player how many lines they want to bet on.
        Keeps asking until a valid number or 'q' to quit is entered.
        """
        while True:
            lines = input(f"Enter number of lines to bet on (1-{self.MAX_LINES}) (or 'q' to quit): ")
            if lines.lower() == 'q':
                print("Goodbye!")
                exit()
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= self.MAX_LINES:
                    return lines
            print(f"Invalid input. Please enter a number between 1 and {self.MAX_LINES}.")

    def get_bet(self):
        """
        Asks the player how much they want to bet on each line.
        Keeps asking until a valid amount or 'q' to quit is entered.
        """
        while True:
            amount = input(f"Enter bet amount on each line: {self.CURRENCY} (or 'q' to quit): ")
            if amount.lower() == 'q':
                print("Goodbye!")
                exit()
            if amount.isdigit():
                amount = int(amount)
                if self.MIN_BET <= amount <= self.MAX_BET:
                    return amount
            print(f"Invalid bet amount. Please enter a number between {self.CURRENCY}{self.MIN_BET} - {self.CURRENCY}{self.MAX_BET}.")

    def print_slot_machine(self, columns):
        """
        Nicely prints the slot machine's current state in rows and columns.
        """
        print("\n--- SLOT MACHINE ---")
        for row in range(len(columns[0])):
            print(" | ".join(str(column[row]) for column in columns))
        print("--------------------\n")

    def check_wins(self, columns, lines, bet):
        """
        Checks if any of the lines the player bet on are winners.
        Returns the total winnings and which lines won.
        """
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += self.symbol_values[symbol] * bet
                winning_lines.append(line + 1)
        return winnings, winning_lines

    def spin(self, balance):
        """
        Handles a single round: gets bets, spins the machine, shows results, and returns the net win/loss.
        """
        lines = self.get_number_of_lines()
        while True:
            bet = self.get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"Insufficient balance. Your current balance is {self.CURRENCY}{balance}.")
            else:
                break
        print(f"Bet amount: {self.CURRENCY}{bet} on lines: {lines}. Total bet is {self.CURRENCY}{total_bet}")
        slots = self.get_spin()
        self.print_slot_machine(slots)
        winnings, winning_lines = self.check_wins(slots, lines, bet)
        print(f"You won {self.CURRENCY}{winnings}.")
        if winning_lines:
            print(f"You won on lines: ", *winning_lines)
        else:
            print("No winning lines this round.")
        return winnings - total_bet, winnings, winning_lines
    def deposit(self):
        """
        Asks the player how much money they want to deposit to start playing.
        Keeps asking until a valid amount or 'q' to quit is entered.
        """
        while True:
            amount = input(f"Enter amount to deposit: {self.CURRENCY} (or 'q' to quit): ")
            if amount.lower() == 'q':
                print("Goodbye!")
                exit()
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    return amount
            print("Invalid amount. Please enter a positive number.")
    MAX_LINES = 3
    MAX_BET = 100
    MIN_BET = 1
    ROWS = 3
    COLS = 3
    CURRENCY = "₹"
    DEFAULT_SYMBOL_COUNTS = {
        "A": 2,
        "B": 3,
        "C": 4,
        "D": 5
    }
    DEFAULT_SYMBOL_VALUES = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
    }

    def __init__(self, symbol_counts=None, symbol_values=None):
        self.symbol_counts = symbol_counts if symbol_counts else self.DEFAULT_SYMBOL_COUNTS.copy()
        self.symbol_values = symbol_values if symbol_values else self.DEFAULT_SYMBOL_VALUES.copy()

    def get_spin(self):
        """
        Randomly generates the slot machine's columns for a spin.
        """
        all_symbols = []
        for symbol, count in self.symbol_counts.items():
            all_symbols.extend([symbol] * count)
        columns = []
        for _ in range(self.COLS):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(self.ROWS):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            columns.append(column)
        return columns

def main():
    slot_machine = SlotMachine()
    balance = slot_machine.deposit()
    print(f"Deposited amount: {slot_machine.CURRENCY}{balance}")
    last_winnings = None
    while True:
        print(f"Current balance is {slot_machine.CURRENCY}{balance}")
        if last_winnings is not None:
            print(f"Previous round winnings: {slot_machine.CURRENCY}{last_winnings}")
        answer = input("Press enter to play (q to quit). ")
        if answer.lower() == "q":
            break
        try:
            net, last_winnings, _ = slot_machine.spin(balance)
            balance += net
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    print(f"You left with {slot_machine.CURRENCY}{balance}")

if __name__ == "__main__":
    main()
    main()
