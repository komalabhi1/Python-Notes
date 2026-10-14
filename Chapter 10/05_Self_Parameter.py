# SELF PARAMETER
# self refers to the instance of the class. It is automatically passed with a function call
# from an object.

class Employee:
    language = "Pyhton"
    salary = 150000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning")   


komal = Employee()
# harry.language = "Javascript"  # this is an instance attribute
komal.greet()
komal.getInfo()
# Employe.getinfo(komal) # ye inko likhan eka second tarika hain

# self sirf ek name hain aap koi bhi le sakte hain