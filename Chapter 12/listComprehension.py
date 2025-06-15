myList = [1, 2, 9, 5, 3]

squaredList = []

# for item in myList:
#     squaredList.append(item ** 2)

# Using list comprehension to create a new list with squared values
# It performs item squared for each item in myList

squaredList = [item ** 2 for item in myList]

print(squaredList)