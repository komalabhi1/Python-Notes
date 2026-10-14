# 9. Write a program to print the following star pattern.
# * * *
# *   *    for n = 3
# * * * 


n = int(input("Enter a number"))
for i in range(1, n+1):
    if(i==1 or i==n):               
        print("*"* n, end="")

else:
    print("*", end="")
    print(" "* (n-2), end="")
    print("*", end="")   
print("")


'''
if(i==1 or i==n)
        print("*"* n, end="")
means starting ki line aur end ki line ko 3 star print kro 
yaha hamara n 3 hain 

now,
else:
    print("*", end="")
ye pahle * print krega

    print(" "* (n-2), end="")
ye space ke liye hain 
* ke baad ek spae hain so n-2 means 1 so 1 space print hogi

    print("*", end="") 
ye end me * print krega    


'''