# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Komal", 120000, 333444)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Abhishek", 150000, 123456)
print(r.name, r.salary, r.pin, r.company)