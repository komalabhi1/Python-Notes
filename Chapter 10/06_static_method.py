# STATIC METHOD
# Sometimes we need a function that does not use the self-parameter. We can define a
# static method like this:
# @staticmethod # decorator to mark greet as a static method
# def greet():
# print("Hello user")


class Employee:
    language = "Pyhton"
    salary = 150000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("Good Morning")   


komal = Employee()
# harry.language = "Javascript"  # this is an instance attribute
komal.greet()
komal.getInfo()
# Employe.getinfo(komal) # ye inko likhan eka second tarika hain

# @staticmethod  = means hamne function ko mark kr diya ki ye self nahi lega that means iske andar object ka kuch bhi nahi chahiye