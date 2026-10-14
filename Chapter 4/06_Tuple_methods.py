# 1. Count

a = (1,234,90,"Komal", False, True)

no = a.count(90)

print(no)

# 2 index

a = (1,234,90,"Komal", False, True)

a.index(1)

print(a)

# 3. list in tuple

a = (1,234,90,"Komal", False, True, [23,44.5, "Abhishek"])

print(a)

# 4. convert tuple into list

numbers = (10, 20, 30)

numbers_list = list(numbers)

numbers_list.append(40)

print(numbers_list)

# 5.Tuple with if

numbers = (10, 20, 30)

if 20 in numbers:
    print("20 is present")

# 6. Sum()    

numbers = (10, 20, 30)

print(sum(numbers))

# 7. Max() And Min()

numbers = (10, 50, 20, 40)

print(max(numbers))
print(min(numbers))

# 8. len() Function

numbers = (10, 20, 30, 40)

print(len(numbers)) # tuple me kitne function hain

# 9. in Operator

numbers = (10, 20, 30)

print(20 in numbers) # True

# 10. not in Operator

numbers = (10, 20, 30)

print(50 not in numbers) # true

# 11. Tuple repetition

numbers = (10, 20)

print(numbers * 3) # (10,20,10,20,10,20)

# 12. TUple COncatination

a = (10, 20)
b = (30, 40)

c = a + b

print(c)

# 13. Tuple Packing

student = "Abhi", 23, "Pune"

print(student)

# 14. Tuple Unpacking

student = ("Abhi", 23, "Pune")

name, age, city = student

print(name)
print(age)
print(city)

# 15. Tuple Slicing

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])

