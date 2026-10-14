class Employee:
    language = "Python"  # This is a class attribute
    salary = 1500000


Komal = Employee()
print(Komal.salary, Komal.language)

abhishek = Employee()
print(abhishek.language, abhishek.salary)

# isme ham name bhi print kr sakte hain

Komal = Employee()
Komal.name = "Komal"    # This is an instance attribute
print(Komal.name, Komal.salary, Komal.language)

abhishek = Employee()
abhishek.name = "Abhishek"
print(abhishek.name, abhishek.language, abhishek.salary)

# Her name is instance attribute and salary and language
#  are class attributes as they directly belong to the class