n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print(" "*(n-i), end="")   # end parameter is used to avoid new line
    print("* "*(2*i - 1), end="")
    print("")