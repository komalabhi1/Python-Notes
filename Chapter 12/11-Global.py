a = 89

def fun():
    global a       # global keyword global variables ko change kr deta hain
    a = 3
    print(a)


fun()
print(a)