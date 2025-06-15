#Else block in try-except structure is executed if no exceptions occur in the try block.

try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No exceptions occurred. The input was processed successfully.")