# f.readlines function

f = open("file.txt")

lines = f.readlines()

print(lines, type(lines))

f.close()

# ye list me file.txt ki sab lines print krega

# seperately bhi line print kr sakte hain

# line1 = f.readline()
# print(line1, type(line1))
# line2 = f.readline()
# print(line2, type(line2))
# line3 = f.readline()
# print(line3, type(line3))

# f.close()

# readline using while loop
line = f.readline()
while(line != ""):
    print(line)

f.close()
