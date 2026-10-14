# 4. STRING FUNCTIONS

# 1. len () function

name = "komal"

print(len(name)) # length is 5

# 2. String.endswith("mal")

name = "komal"

print(name.endswith("mal")) # True
print(name.endswith("mala")) # false bcz "Komal" ends with mal not mala
print(name.startswith("kom")) # True

# 3. Capatilize String

name = "komal"

print(name.capitalize()) # ye "komal" ko capatilize krega

# 4. string.count("c") 

name = "Komal"

count = name.count("m") # 1

print(count)

# 5.  string.find(word)

name = "Komal"

index = name.index("o")

print(index)

# 6. string.replace (old word, new word ) 

name = "komal"

replaced_name = name.replace("k" , "t") # tomal

print(replaced_name)

# 7. Upper

name = "hello"

name = name.upper() # HELLO

print(name)

# 8. Lower

name = "HELLO"

name = name.lower()

print(name)

# 9. split() - String ko list mein todna

name = "a,b,c"

name = name.split()

print(name)

# 10. Join

words = ["Hello", "Python", "World"]

result = " ".join(words)

print(result)
