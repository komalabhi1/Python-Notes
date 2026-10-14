
class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"   

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45

e.name = "Komal Dhandar"
print(e.fname, e.lname)

e.show()

# Getter = data read karna

# Setter = data update/change karna

# example 2:

class Mobile:

    def __init__(self, volume):
        self.__volume = volume

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, value):

        if 0 <= value <= 100:
            self.__volume = value
        else:
            print("Volume must be between 0 and 100")


mobile = Mobile(50)

print(mobile.volume)

mobile.volume = 80

print(mobile.volume)

mobile.volume = 150