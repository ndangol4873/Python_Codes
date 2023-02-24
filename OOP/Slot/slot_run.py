from guest import User
from checkin import user_check_in, user_deposit, get_number_of_lines, get_bet

## PROGRAM RUN SCRIPT

print("----------Welcome to Slot Game------------------")
customer_option = int(input("Press any number to Continue "))
Name,Age,Gender,Balance = user_check_in(option=customer_option)


user_balance = user_deposit(Balance)
lines = get_number_of_lines()
bet = get_bet()
