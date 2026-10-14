# THE BREAK STATEMENT
# ‘break’ is used to come out of the loop when encountered. It instructs the program to exit the loop now.–

for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)  # means ye 33 tak print hoga


# THE CONTINUE STATEMENT
# ‘continue’ is used to stop the current iteration of the loop and continue with the next one.
#  It instructs the Program to “skip this iteration”.

for i in range(100):
    if(i == 34):
        continue # Skip this iteration 
    print(i)

# ye 34 ko skip krke 1 se lekar 100 tak print karega
