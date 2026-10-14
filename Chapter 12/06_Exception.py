
try:
    a = int(input("Hey,Enter a number"))
    print(a)             # agar user ne number enter kiya to ye chalega 

except Exception as e:
    print(e)             # agar user ne number ki jagah word ya aur kuch enter kiya to ye error nahi dikhayega uski 
                          # jagah invalid batayega

print("Thank You")       # invalid batane ke baad ye thank you ko bhi print krega



# pahle try execute krega aur agar try ka input sahi nahi h to except exception ko run krega

# We can also specify the exception to catch like below:


try:
    a = int(input("Hey,Enter a number"))
    print(a)             # agar user ne number enter kiya to ye chalega 

except ValueError as v:
    print("Heyyy")
    print(v)
except Exception as e:
    print(e)             # agar user ne number ki jagah word ya aur kuch enter kiya to ye error nahi dikhayega uski 
                          # jagah invalid batayega

print("Thank You") 