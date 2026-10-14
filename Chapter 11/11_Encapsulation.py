
# Data ko protect/control karta hai.

# Encapsulation = Data ko class ke andar rakhna + us data ko 
# direct access/change karne se control karna.

'''
🎓 Real-life Student Example

Maan lo ek student ka marks hai:

Student
   |
   └── Marks = 80

Agar marks ko koi bhi directly change kar sake:

Marks = -500
Marks = 1000
Marks = 99999

to problem hai.

Isliye hum marks ko protect karenge.

Student ke marks change karne ke liye ek proper method hoga:

set_marks()

Aur marks dekhne ke liye:

get_marks()

'''

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    # Set marks with validation
    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully")
        else:
            print("Invalid marks! Marks must be between 0 and 100.")

    # Get marks
    def get_marks(self):
        return self.__marks


# Create object
student = Student("Abhishek", 80)

# Access marks using method
print("Student Name:", student.name)
print("Marks:", student.get_marks())

# Update marks
student.set_marks(90)

print("Updated Marks:", student.get_marks())

# Try invalid marks
student.set_marks(150)