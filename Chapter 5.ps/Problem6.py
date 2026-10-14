# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

d = {}

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)

#  If the names of 2 friends are same; what will happen to the program in problem 
# The values entered later will be updated
# jo last me hoga wo output aayega bcz wo update hota jayega


# If languages of two friends are same; what will happen to the program in problem
# Nothing will happen. The values can be same
# to jaisa diya hain waisa same output milega sirf key change ho to hi last ka output milega
# value same ho sakti hain
