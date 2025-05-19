import os

# Select the directory whose contents you want to print
directory_path = '/'

# Use the os module to the contents of the directory
contents = os.listdir(directory_path)

# Print the contents of the directory
for item in contents:
    print(item)

# print(contents)