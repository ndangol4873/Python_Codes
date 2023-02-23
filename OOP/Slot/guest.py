## Parent class "User"
# Holds details about the Users

import re

class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = 0
        

    def show_details(self):
        return self.name, self.age, self.gender
        # print (f"User Details\nName: {self.name}\nage: {self.age}\ngender: {self.gender} ")



    def user_deposit(self, amount):
        try:
            self.amount = int(amount)
        except Exception as e:
            print("PLEASE ENTER NUMBER")

    
        if self.amount > self.balance:
            self.balance = self.balance + self.amount
            print(f"YOUR BALANCE IS :{self.balance} ")
        else:
            print(F"Do NOT HAVE SUFFICIENT BALANCES: {self.balance} ")

    def check_balance(self):
        print(f"YOUR CURRENT BALANCE :{self.balance} ")



# Naresh = User('Naresh', 39,'Male')
# Naresh.show_details()
# Naresh.user_deposit(10)
# Naresh.check_balance()