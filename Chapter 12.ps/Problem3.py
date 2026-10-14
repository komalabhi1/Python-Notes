# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.


n = int(input("Enter a number"))

# n = 5     # 5 ki table print ho jaygi

table = [ n*i for i in range (1,11)]

print(table)


# jo bhi number enter kroge uski table print ho jayegi