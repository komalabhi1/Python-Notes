# 5. TYPE() FUNCTION AND TYPECASTING


a = 31 
t = type(a) # class <int>

print(t)

a = 31.2
t = type(a) # class <float>

print(t)

a = "Komal"
t = type(a) # class <string>

print(t)

a = "31.2"
t = type(a) # class <string> , Bcz 31.2 is in the double inverted comma

print(t)

# Change Type()

a = "31.2"
b = float(a) # a but the type should be float
t = type(b)

print(t)

a = "32"
b = int(a)
t = type(b)

print(t)