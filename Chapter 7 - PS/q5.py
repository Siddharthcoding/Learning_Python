n = int(input("Enter the value of n: "))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f"The sum of first {n} natural numbers is: {sum}")