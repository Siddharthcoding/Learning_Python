# Using 'with' statement to open the file, which ensures it is properly closed after the block is executed

with open("file.txt") as f:  
    print(f.read())

# The 'with' statement automatically closes the file after the block is executed, even if an error occurs