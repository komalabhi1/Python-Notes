# 7. Write a program to find out the line number where python is present from ques 6.

line = 1
with open("log.txt", "r") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("Python" in line):
        print("yes python in present. Line no: (lineno)")
        break
    lineno += 1     
         
else:
    print("No, Python is not present")
   