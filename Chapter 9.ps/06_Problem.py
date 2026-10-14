# 6. Write a program to mine a log file and find out whether it contains ‘python’.


with open("log.txt", "r") as f:
    content = f.read()

if("Python" in content):
    print("yes python in present")
else:
    print("No, Python is not present")