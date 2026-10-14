# When a program gets bigger in size and its complexity grows, it gets difficult for a
# program to keep track on which piece of code is doing what!
# A function can be reused by the programmer in a given program any number of


a = 12
b = 32
c = 11

average = ( a + b + c)/3
print(average)

a = int(input("Enter your number"))
b = int(input("Enter your number"))
c = int(input("Enter your number"))

average = ( a + b + c)/3
print(average)

# agar aise hame kafi alag alag numbers ki average krni hain to iske liye time lagega
# aisa bar bar krne ke liye ham function use krte hain

# Functiion Definition
def avg():
    a = int(input("Enter your number"))
    b = int(input("Enter your number"))
    c = int(input("Enter your number"))

    average = ( a + b + c)/3
    print(average)

avg() # Functioin Call
avg()
avg()
avg()
avg()    # iska matlab muze 5 bar avg krni hain 


# This function can be called any number of times, anywhere in the program