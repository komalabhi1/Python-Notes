# MULTIPLE INHERITANCE

# Multiple Inheritance occurs when the child class inherits from more than one parent classes.


class Employee:                                # Base class / Parent class
    company = 'ITC'
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:                                   # Base class / Parent class
    language = "Python"                       
    def printLanguage(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee, Coder):                   # Derived or Child class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()