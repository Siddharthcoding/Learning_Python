f = open("poem.txt")

data = f.read()  # Read the entire content of the file

if("twinkle" in data):
    print("twinkle found")
else:
    print("twinkle not found")