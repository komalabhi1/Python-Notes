# 7. Write a python function to remove a given word from a list ad strip it at the same time.

# for remove only
# def remove(l, word):
#     for item in l:
#         l.remove(word)
#         return l

# l = [ "Harry", "Rohan", "Komal", "Abhishek"]

# print(remove(l, "Harry"))

# for remove and ad strip

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
            return n

l = ["harry", "Komal", "Shital", "Abhishek"]

print(rem(l, "l"))