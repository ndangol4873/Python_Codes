from guest import User
import re

def user_check_in(option):
    if option > 0:
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
            else:
                print("ERROR Input must be Number")
        else:
            print("ERROR Input must be Text")
    else:
        print('Thank you')

    return Name, Age, Gender


