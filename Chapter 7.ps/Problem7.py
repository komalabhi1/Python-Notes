# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3

'''
for n = 3
  *
 ***
*****

for n = 5
    *
   ***
  *****
 ********
**********

'''

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")


    '''
    for no 3 
        print(" "* (n-i), end="")

    ye space print krta hain
    n - i       here # i = 1
    3 - 1    
    2 means ye 2 space print krega
    
    fir 3 se pahle 2 aata hain to 
    2 - 1
    1 means 1 space print krega

    fir 2 se pahle 1 aata hain
    1 - 1
    0 means ye 0 space print krega
    
    yaha pe ye end ho jayega
    

    now,
        print("*"* (2*i-1), end="")
        
    ye * print krega
    2*i-1
    2*1-1
    2-1
    1 means ye 1 * print karega

    2*2-1
    4-1
    3 means ye 3 * print krega

    2*3-1
    6-1
    5 means ye 5 * print krega

    uske baad ye end krna hoga kyuni hamara n = 3 hain    

    now,
    print("") ye next line me lekar jata hain 
    
    '''