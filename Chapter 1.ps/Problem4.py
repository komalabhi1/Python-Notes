# 4. Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

import os

# Current directory ke contents print karna

folder_path = r"C:\Users\abhid\OneDrive\Desktop\komal with SQL"

contents = os.listdir(folder_path)

for item in contents:
    print(item)