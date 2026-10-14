
class Employee:
    language = "Pyhton"
    salary = 150000

    def __init___(self):   # dunder method, which is a automatically called
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("Good Morning") 


komal = Employee()
komal.name = "Komal"
print(komal.name, komal.salary)

Rohan = Employee()