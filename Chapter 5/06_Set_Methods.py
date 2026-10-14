# Set Methods

s = {1,2,3,4,32,54,5,"Komal"}

print(s, type(s))

# 1. s.add()

s = {1,2,3,4,32,54,5,"Komal"}

s.add(566)

print(s, type(s))

# 2.len(s)

# use repl


# 3. s.remove

s = {1,2,3,4,32,54,5,"Komal"}

s.remove(1)
print(s, type(s)) # remove 1

# 4.  s.pop(): Removes an arbitrary element from the set and return the element removed.

# 5. s.clear(): empties the set s.

# 6.  s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}.

# 7. s.intersection({8,11}): Return a set which contains only item in both sets {8}.

# 8. copy()

new_s = s.copy()

print(new_s)

# 9. difference()- Do sets mein jo elements first set mein hain lekin second mein nahi hain, woh return karta hai.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.difference(b)) # output {1,2}

# 10. discard() - Set se specified element remove karta hai.

numbers = {10, 20, 30}

numbers.discard(20) # output {10,30}

print(numbers)

# 11. issubset()

# Check karta hai ki ek set ke saare elements doosre set mein present hain ya nahi.

a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b)) # True

# 12. issuperset()

# Check karta hai ki ek set ke andar doosre set ke saare elements present hain ya nahi.

a = {1, 2, 3, 4}
b = {1, 2}

print(a.issuperset(b)) # True

# 13. pop()

# Set se random/arbitrary element remove karke return karta hai.

# 14. update()

# Set mein doosre iterable ke unique elements add karta hai.

a = {1, 2, 3}

a.update({3, 4, 5})

print(a) # output {1,2,3,4,5}

# ⭐ Operators bhi yaad rakho

# Set mein methods ke shortcuts bhi hote hain:

# A | B       # Union
# A & B       # Intersection
# A - B       # Difference
# A ^ B       # Symmetric Difference
# A <= B      # Subset
# A < B       # Proper subset
# A >= B      # Superset
# A > B       # Proper superset
# A.isdisjoint(B)