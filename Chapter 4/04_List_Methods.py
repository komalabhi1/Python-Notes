# 3. Lists Methods

# 1. Append

friends = ["Apple", "Komal", 5, 35.67, "Abhishek", False, True]

print(friends)

friends.append("Rohan") # adds "Rohan" at the end of the list 

print(friends)

# 2. Sort

numbers = [1,9,8,35,7,2,21,15]

numbers.sort() # update the list acending or decending

print(numbers)

# 3. Reverse

numbers = [1,9,8,35,7,2,21,15]
 
numbers.reverse() # update the list reverse

print(numbers)

# 4. insert

numbers = [1,9,8,35,7,2,21,15]

numbers.insert(3, 4444) # this will add 444 at index 3

print(numbers) 

# 5. pop
#  Element ko remove karta hai aur removed element ko return bhi karta hai.
numbers = [1,9,8,35,7,2,21,15]

numbers.pop(3)

print(numbers)

# 6. remove

numbers = [1,9,8,35,7,2,21,15]

numbers.remove(1) # removed 1

print(numbers)

# 7. Clear
# lists ke sare elements remove kr deta hain

numbers = [1,9,8,35,7,2,21,15]

numbers.clear()

print(numbers)

# 8. copy
# excisting list ki copy banata hain

numbers = [1,9,8,35,7,2,21,15]

numbers.copy()

print(numbers)

# 9. Count
# Koi value list me kitni bar hain ye count krta hain

numbers = [1,9,8,35,7,2,21,15]

print(numbers.count(2))

# 10. index
# given value ka first index banata hain

numbers = [1,9,8,35,7,2,21,15]

print(numbers.index(35))

