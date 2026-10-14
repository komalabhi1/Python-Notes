# Dictionary Methods

# 1. a.items(): Returns a list of (key,value)tuples.

marks = {
    "Harry" : 100,
    "Abhishek" : 56,
    "Komal" : 23,
    0 : "Harry"
}

print(marks.items())

# 2.  a.keys(): Returns a list containing dictionary's keys.

marks = {
    "Harry" : 100,
    "Abhishek" : 56,
    "Komal" : 23,
    0 : "Harry"
}

print(marks.keys())

# 3. a.values

marks = {
    "Harry" : 100,
    "Abhishek" : 56,
    "Komal" : 23,
    0 : "Harry"
}

print(marks.values())

# 4. • a.update({"friends":}): Updates the dictionary with supplied key-value pairs.

marks = {
    "Harry" : 100,
    "Abhishek" : 56,
    "Komal" : 23,
    0 : "Harry"
}

marks.update({"Harry": 99})
print(marks)

marks.update({"Harry": 99, "Renuka": 100}) # "harry" update hoga aur "Renuka" add ho jayegi

# 5. a.get("name"): Returns the value of the specified keys (and value is returned
# eg."harry" is returned here).

marks = {
    "Harry" : 100,
    "Abhishek" : 56,
    "Komal" : 23,
    0 : "Harry"
}

print(marks.get("Harry")) # 100 
print(marks["Harry"]) # 100
# but

print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Prints Error

# This is difference between this two

# 6. len() function

d = {0:1, 1:"Komal"}

# 7. Clear() - Dictionary ke saare items remove karta hai.

marks = {
    "Harry" : 100,
    "Abhishek" : 56,
    "Komal" : 23,
    0 : "Harry"
}

marks.clear()
print(marks)

# 8. copy() - Dictionary ki copy banata hain

marks = {
    "Harry" : 100,
    "Abhishek" : 56,
    "Komal" : 23,
    0 : "Harry"
}
new_marks = marks.copy()
print(new_marks)

# 9. fromkeys()

keys = ["name", "age", "city"]

student = dict.fromkeys(keys)

print(student)

# 10. pop() - specific key ko remove krta hai aur usko return krta hain

student = {
    "name": "Abhishek",
    "age": 24,
    "city": "Pune"
}

result = student.pop("age")

print(result)
print(student)

# 11. popiteam()-Dictionary ka last inserted key-value pair remove karta hai.

student = {
    "name": "Abhishek",
    "age": 24,
    "city": "Pune"
}

result = student.popitem()
print(result)
print(student)

# 12. setdefault() - Key exist karti hai to existing value return karta hai.
                    #  keys absent ho to add krti hain
                    
# Notes                    

# clear     → sab hatao
# copy      → copy banao
# fromkeys  → keys se dictionary banao
# get       → value lo
# items     → key + value
# keys      → keys lo
# pop       → particular item hatao
# popitem   → last item hatao
# setdefault→ nahi hai to add karo
# update    → add/update karo
# values    → values lo

# OPERATORS IN DICTIONARY

# 1. [] — Access Operator - Key ke through value access karne ke liye.

student = {
    "name": "Abhishek",
    "age": 24,
    "city": "Pune"
}

print(student["name"]) # Abhishek

# 2. in — Membership Operator - Check karta hai ki key dictionary mein present hai ya nahi.

print("name" in student) # True
print("salary" in student) # False

# 3. not in — Membership Operator-Check karta hai ki key dictionary mein present nahi hai.

print("salary" not in student) # True
print("age" not in student) # False

# 4. == — Equal Operator - Dono dictionaries ka key-value data same hai ya nahi check karta hai.

a = {"name": "Abhishek", "age": 24}
b = {"name": "Abhishek", "age": 24}

print(a == b) # True

# 5. != — Not Equal Operator - Check karta hai ki dictionaries same nahi hain.

a = {"name": "Abhishek"}
b = {"name": "Rahul"}

print(a != b) # True


# 6. | — Dictionary Merge Operator

a = {
    "name": "Abhishek"
}

b = {
    "age": 24
}

result = a | b

print(result)

# 7. |= — Update/Merge Assignment Operator - Existing dictionary mein doosri dictionary ko merge/update karta hai.

student = {
    "name": "Abhishek"
}

student |= {
    "age": 24
}

print(student)

# Notes

# | Operator | Kaam                    | Example          |
# | -------- | ----------------------- | ---------------- |
# | `[]`     | Value access            | `d["name"]`      |
# | `in`     | Key present?            | `"name" in d`    |
# | `not in` | Key absent?             | `"age" not in d` |
# | `==`     | Dictionaries equal?     | `a == b`         |
# | `!=`     | Dictionaries different? | `a != b`         |
# | `\|`     | Dictionaries merge      | `a \| b`         |
# | `\|=`    | Merge + update          | `a \|= b`        |




