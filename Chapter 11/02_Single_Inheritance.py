# SINGLE INHERITANCE

# Single inheritance occurs when child class inherits only a single parent class.


# Base to Derived class


class Employee:                                # Base class
    company = 'ITC'
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")    

# so instead of doing this you can do this (down)

class Programmer(Employee):                   # Derived or Child class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

# isase employee me kuch bhi change kiya to automaticlay isme bhi change ho jayega


a = Employee()
b = Programmer()

print(a.company, b.company)


    