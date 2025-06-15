a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Division by zero is not allowed. Please enter a non-zero second number.")
else:
    print(f"Thr division {a}/{b} is {a/b}")