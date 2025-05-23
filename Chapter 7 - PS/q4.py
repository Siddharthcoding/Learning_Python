num = int(input("Enter a number: "))

for i in range(2, num//2):   # Range can only have integer values not float
    if(num % i == 0):
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")