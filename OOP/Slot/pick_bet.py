import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3


def get_number_of_lines():
    while True:
       lines = input("Enter number of lines to bet on (1-" +str(MAX_LINES) + ")? ")
       if lines.isdigit():
           lines = int(lines)
           if 1 <= lines <= MAX_LINES:
               break
           else:
               print("Enter valid number of lines ")
       else:
           print("Please enter number")
    return  lines


#             print("Please enter a number ")


def get_bet():
    while True:
       amount = input("What would you like to bet on each line? ")
       if amount.isdigit():
           amount = int(amount)
           if MIN_BET <= amount <= MAX_BET:
               break
           else:
               print(f"Amount must be between  $ { MAX_BET} -$  {MAX_BET}. ")
       else:
           print("Please enter number")
    return  amount