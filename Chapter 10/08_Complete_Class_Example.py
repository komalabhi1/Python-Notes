class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def study(self):
        print(self.name, "is studying")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Abhishek", 24, "MCA")

student1.display()
student1.study()

# Multiple object : 

class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def study(self):
        print(self.name, "is studying")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student1 = Student("Abhishek", 24, "MCA")
student2 = Student("Komal", 24, "BSC")
student3 = Student("Pooja", 20, "BE")

student1.display()
student1.study()
student2.display()
student2.study()
student3.display()
student3.study()