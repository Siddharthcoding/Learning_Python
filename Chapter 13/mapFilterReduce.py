from functools import reduce

nums = [1, 2, 3, 4, 5]

square = lambda x: x * x

# Map applies the function to each item in the iterable
sqList = map(square, nums)
print(list(sqList))

# Filter filters the items in the iterable based on the function
filterEven = lambda x: x % 2 == 0

evenList = filter(filterEven, nums)
print(list(evenList))

# Reduce applies the function cumulatively to the items in the iterable
sum = lambda a, b: a + b
total = reduce(sum, nums)

print(total)