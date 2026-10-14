# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3


n = int(input("Enter a number: "))
for i in range(1, n+1):
    print("*"* i, end="")
    print("")

    '''
     print("*"* i, end="")

  ye * print krega
  "*" * 1
  1 * print krega

  "*" * 2 
  2 * print krega 

  "*" * 3 
  3 star print krega

  end="   
    
    '''