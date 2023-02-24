from guest import User
import re

def user_check_in(option):
    # if option > 0:
    name = input("Please enter your Full Name : ")
    if re.match("^[a-zA-Z]+(?:\s[a-zA-Z]+)?$", name):
        age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            gender = input("Enter your gender: ")
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



def user_deposit(balance):
    try:
        amount = input("Add Balance to Your Account ")
        amount = int(amount)
    except Exception as e:
        print("PLEASE ENTER NUMBER")
    if amount > balance:
        balance = balance + amount
        print(f"YOUR BALANCE IS :{balance} ")

