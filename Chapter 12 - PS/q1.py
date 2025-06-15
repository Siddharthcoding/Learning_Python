try:
    with open("1.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the file path.")

try:
    with open("2.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the file path.")

try:
    with open("3.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the file path.")