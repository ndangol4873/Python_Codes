## Function For user input.

def deposit():
    while True:
        amount = input("Deposit Amount?") # user input
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Number must be greater than 0")
        else:
            print("Please Enter Number")
    return amount


deposit()