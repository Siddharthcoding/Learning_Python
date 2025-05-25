def nSum(n):
    if(n == 0):
        return 0
    else:
        return n + nSum(n - 1)
    
n = int(input("Enter the number to find the sum: "))
print(f"The sum of first {n} natural numbers is {nSum(n)}")