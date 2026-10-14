# 2. Write a python program using function to convert Celsius to Fahrenheit.



# formula of celsius to fahrenheit : c/5 = (f-32)/9

f = int(input("Enter temperature in F"))
c = 5*(f-32)/9

print(c)

# same ise hi function me krenge

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)

print(f"{round(c,2)}  degree celcious")

# round = decimal ke liye use hota hain
# here round(c, 2) means number ke baad 2 decimal point hi dikhenge
# for ex : 33.44