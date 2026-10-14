# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]


l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    print(name.startswith("S"))
    print(f"Hello {name}")


# f = string ke andar variable ki value directly insert karna.
# agar f nahi lagaya to = Python {name} ko variable nahi samjhega.
# aur Hello {name} aisa print hota
# "Is string ke andar {} me jo variable/expression hai, uski actual value insert karo."

name = "Rahul"
age = 25

print(f"My name is {name} and my age is {age}")

# isme f ki vajah se name variable ki value aur age variable ki value add krega
