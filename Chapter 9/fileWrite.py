data = "This is the text to be written"

f = open("file.txt", "w")  # Open the file in write mode

f.write(data)  # Write data to the file
f.close()  # Close the file