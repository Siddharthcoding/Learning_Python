# This code uses the walrus operator to assign the length of the list to n
# Walrus operator allows assignment within an expression

if(n:= len([1, 2, 3, 4, 5])) > 0:
    print(f"List has {n} elements")
