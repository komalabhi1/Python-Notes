# CLASS METHOD
# A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.
# Syntax:
# @classmethod
# def(cls,p1,p2):


class Employee:
    a = 1 
    def show(self):
        print(f"The class attribute of a is {self.a}")

e = Employee()
e.a = 45  # instant attribute

e.show()  # Prints 45 not 1


# but if we want class attribute to print then do this:
class Employee:
    a = 1 
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45  # instant attribute

e.show()  # now it prints 1


#  self = means object pr method chal raha h
#  cls = means class par method chal raha hain