## Parent class "User"
# Holds details about the Users

class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        

    def show_details(self):
        print (f"User Details\nName: {self.name}\nage: {self.age}\ngender: {self.gender} ")