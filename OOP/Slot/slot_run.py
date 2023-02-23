from guest import User
from checkin import user_check_in

## PROGRAM RUN SCRIPT

print("Welcome to Slot Game")
customer_option = int(input("Press any number to Continue "))
Name,Age,Gender = user_check_in(option=customer_option)
print(Name)

