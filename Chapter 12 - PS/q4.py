a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

try:
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Infinite")