from guest import User
import re
import random


## Guest Check in function
def user_check_in(option):
    name = input("Please enter your Full Name : ")
    name = name.title()
    if re.match("^[a-zA-Z]+(?:\s[a-zA-Z]+)?$", name):
        age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            gender = input("Enter your gender: ")
            gender = gender.title()
            if re.match("^[A-Za-z]+$", gender):
                user_input = User(name, age, gender)
                Name,Age,Gender = user_input.show_details()
                print(f"Client Registration Details : \n{Name}\n{Age}\n{Gender}")
                user_balance = user_input.check_balance()
        else:
            print("ERROR Input must be Number")
    else:
        print("ERROR Input must be Text")

    return Name, Age, Gender,user_balance


## Guest Deposit Function
def user_deposit(balance):
    try:
        amount = input("Add Balance to Your Account ")
        amount = int(amount)
    except Exception as e:
        print("PLEASE ENTER NUMBER")
    if amount > balance:
        balance = balance + amount
        print(f"YOUR BALANCE IS : $ {balance} ")
        return balance



# MAX_LINES = 3
# def get_number_of_lines():
#     while True:
#        lines = input("Enter number of lines to bet on (1-" +str(MAX_LINES) + ")? ")
#        if lines.isdigit():
#            lines = int(lines)
#            if 1 <= lines <= MAX_LINES:
#                break
#            else:
#                print("Enter valid number of lines ")
#        else:
#            print("Please enter number")
#     return  lines
#
#
# #             print("Please enter a number ")
# MAX_BET = 100
# MIN_BET = 1
#
# def get_bet():
#     while True:
#        amount = input("What would you like to bet on each line? ")
#        if amount.isdigit():
#            amount = int(amount)
#            if MIN_BET <= amount <= MAX_BET:
#                break
#            else:
#                print(f"Amount must be between  $ { MAX_BET} -$  {MAX_BET}. ")
#        else:
#            print("Please enter number")
#     return  amount