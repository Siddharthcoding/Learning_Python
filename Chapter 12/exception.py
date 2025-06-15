try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError as e:
    print(f"Invalid input: {e}. Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
print("Thank You")

