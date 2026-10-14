# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = "Hey abhishek, how are you you are my love you are very handsome"

if("abhishek" in post):
    print("This post is talking about abhishek")

# 2nd example: 

post = input("Enter your post")

if("abhishek" in post):
    print("This post is talking about abhishek")

else: 
    print("This post is not talking about abhishek")

# 3rd example:

post = input("Enter your post")

if("abhishek".upper() in post.upper()):
    print("This post is talking about abhishek")

else: 
    print("This post is not talking about abhishek")