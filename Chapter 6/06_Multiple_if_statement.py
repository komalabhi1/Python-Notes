
a = int(input("Enter your age: "))

# If statement no: 1
if(a%2==0):
    print("a is even") # apna ek independent if satement hain
# End of if statement no: 1

# If statement no: 2   
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age age")

elif(a==0):
    print("You are entering 0 which is not valid")   

else:
    print("You are below the age of consent")
# End of if statement no: 2

print("End of program") 

#  Last else is executed only if all the conditions inside elifs fail.