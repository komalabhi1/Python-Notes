# 6. Write a program to calculate the factorial of a given number using for loop


# factorial
# 5! = 1 * 2 * 3 *4 * 5

n = int(input('Enter a number'))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")


# Yaha n + 1 isliye liya hai kyunki Python ka range() last number ko include nahi karta.

# Tumhare code me:

# for i in range(1, n + 1):

# Agar user n = 5 deta hai, to:

# range(1, 5 + 1)

# yaani:

# range(1, 6)

# Python isme values dega:

# 1, 2, 3, 4, 5
# Agar n hi likhte:
# range(1, n)

# To:

# range(1, 5)

# values milengi:

# 1, 2, 3, 4

# 5 include nahi hoga ❌

# Lekin factorial ke liye hume chahiye:

# 5! = 1 × 2 × 3 × 4 × 5

# Isliye:

# range(1, n + 1)
# Simple rule 🧠

# Python range(start, stop) me:

# start included hota hai, stop excluded hota hai.