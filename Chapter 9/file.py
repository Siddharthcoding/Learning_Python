# import os
# print("Current working directory:", os.getcwd())

f = open("file.txt")  # By default, the file is opened in read mode
data = f.read()

print(data)
f.close()