# Parent Class : User
#   Hold the details of the User
class User():
    def __init__(self,name,age,gender,country):
        self.name = name
        self.age = age
        self.gender = gender
        self.country = country

    def show_details(self):
        print(f"Personal_details\nName :{self.name}\nage :{self.age}\nGender : {self.gender}\nCountry : {self.country}")


Naresh =  User('Naresh',35,'male','Nepal')
Naresh.show_details()
