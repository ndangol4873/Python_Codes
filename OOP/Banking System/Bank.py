import Users_Details

## Child Class
# Inherited al the properties from ParentClass

class Banks(Users_Details.User ):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0


    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f'Account Balance has been updated : {self.balance}')

    def withdraw(self,amount):
        self.amount = amount

        if self.amount > self.balance:
            print(f"Insufficient Balance | Available Balance: {self.balance}\n"
                  f"Request Amount {self.amount}")
        else:
            self.balance = self.balance - self.amount
            print(f"Request Amount:{self.amount}\nBalance :{self.balance}")



