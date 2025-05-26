data = "\nThis is the text to be written"

f = open("file.txt", "a") # Open the file in append mode, which allows adding data to the end of the file without overwriting existing content

f.write(data)  # Write data to the file
f.close()  # Close the file