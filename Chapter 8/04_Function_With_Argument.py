# A function can accept some value it can work with. We can put these values in the parentheses.
# A function can also return value as shown below:

# ex 1
def GoodDay(name):
    print("Good Day, " + name)

GoodDay("Komal")


#  ex 2
def GoodDay(name, ending):
    print("Good Day, " + name)
    print(ending)

GoodDay("Komal", "Thank you")
GoodDay("Abhishek", "Thank You")
GoodDay("Divya", "Thanks")

# ex 3 (return value)
def GoodDay(name, ending):
    print("Good Day, " + name)
    print(ending)
    return "Done"

a = GoodDay("Komal", "Thank you")
print(a)