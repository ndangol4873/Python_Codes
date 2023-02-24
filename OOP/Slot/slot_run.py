from guest import User
from checkin import user_check_in, user_deposit
from pick_bet import  get_number_of_lines, get_bet

## PROGRAM RUN SCRIPT

print("----------Welcome to Slot Game------------------")
customer_option = int(input("Press any number to Continue "))
Name,Age,Gender,Balance = user_check_in(option=customer_option)


user_balance = user_deposit(Balance)
lines = get_number_of_lines()
while True:
    bet = get_bet()
    total_bet = bet * lines
    if total_bet > user_balance:
        print(f"You do not have enough balance to make this bet. Your Current Balance is :{user_balance} ")
    else:
        break
print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
