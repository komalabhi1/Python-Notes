# ENUMERATE FUNCTION IN PYTHON

# The ‘enumerate’ function adds counter to an iterable and returns it

l = [3, 66, 98, 456]

index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1

# This can be simplified using enumerate functiion
# isi kam ko aap enumerate function se aur aasani se kr sakte ho

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")
