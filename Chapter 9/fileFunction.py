f = open("file.txt")

# lines = f.readlines()  # Read all lines from the file into a list
# print(lines, type(lines))  # Print the list of lines and its type

# Read lines one by one, till the end of the file i.e ""

# line1 = f.readline()  # Read the first line from the file
# print(line1, type(line1))

# line2 = f.readline()  # Read the second line from the file
# print(line2, type(line2))

# line3 = f.readline()  # Read the third line from the file
# print(line3, type(line3))

line = f.readline()  
while(line != ""):  # Read lines one by one until the end of the file
    print(line)  
    line = f.readline()  # Read the next line

f.close()  # Close the file
