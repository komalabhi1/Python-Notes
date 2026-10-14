

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass               # parent me implementation nahi hain


class Dog(Animal):

    def sound(self):
        print("Dog says Bark")


class Cat(Animal):

    def sound(self):
        print("Cat says Meow")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# Abstraction = User ko "WHAT" dikhana, "HOW" hide karna.

# Humne Animal ko ek rule/blueprint bana diya.

# Hum keh rahe hain:

# Jo bhi Animal ka child hoga, uske paas sound() method hona hi chahiye.

# Parent ne WHAT define kiya.

# Child ne HOW define kiya.

# Abstraction = Complexity hide karta hai.

# ABC → abstract class बनाने में मदद करता है
# @abstractmethod → child को method implement करना compulsory करता है
# pass → parent में implementation नहीं है

from abc import ABC, abstractmethod

class Animal(ABC):         # yaha animal ek abstract class hain

    @abstractmethod          # ye ek abstract method hain
    def sound(self):
        pass

    # Har Animal ka sound() method hona chahiye, lekin Animal class ye decide nahi karegi ki sound kya hoga.