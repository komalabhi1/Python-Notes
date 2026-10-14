# CHAPTER 9 – FILE I/O

'''
a = "a very long string with emails"

emails = []
3 second 

program chala, emails generate huye, program exit hua, finish
ek bar program exit hone ke baad wo emails aapko nahi dikhenge

iske liye wo jo data aapne generate kiya use agar aap store karna chahte ho to aapko 
file ka use krna padega
'''

# Read File

f = open("file.txt", "r")
data = f.read()
print(data)
f.close

# ye hame file.txt dikhayega
# open = python builtin function hain jo files ko read krne me help krta hain