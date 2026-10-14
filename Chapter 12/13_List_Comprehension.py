# List Comprehension is an elegant way to create lists based on existing lists.


myList = [1, 2, 3, 4, 5]

squaredList = []
for item in myList:
    squaredList.append(item*item)   


print(squaredList)


# this can be more simple using comprehension

myList = [1, 2, 3, 4, 5]

squaredList = [i*i for i in myList]

print(squaredList)