n = int(input("Enter a number: "))

print("Multiplication of the number in reverse is:")

for i in range(10, 0 , -1):
    print(f"{n} x {i} = {n * i}")