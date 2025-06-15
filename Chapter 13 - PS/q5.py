from functools import reduce

nums = [1, 2, 3, 4, 5, 9, 15, 10, 6]

def greater(a, b):
    if a > b:
        return a
    else:
        return b
    
print(reduce(greater, nums))