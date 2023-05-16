import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows , cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
        print()
        

def get_user_input_for_deposit():
    while True:
        amount = input("How much would you like to depposit?  $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a number greater than 0")
        else:
            print("Please enter a valid number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("how many lines would you want to bet on(1-" +str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a number within than 0 - 3")
        else:
            print("please enter a valid number")
    return lines

def amount_to_bet_on_each_line():
    while True:
        amount = input("what would you like to bet?  $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Please enter a bet between ${MIN_BET}-${MAX_BET}.")
        else:
            print("please enter a valid number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = amount_to_bet_on_each_line()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(f"Insufficient balance! please re-enter your bet.....")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet
    
def main():
    balance = get_user_input_for_deposit()
    while True:
        spins = input("Press enter to play (q to quit).")
        if spins == "q":
            break
        balance += spin(balance)
        print(f"Current balance is ${balance}")
    print(f"You have ${balance} left")

    
main()