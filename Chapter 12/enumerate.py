l = [7, 9, 1, 8, 76, 32]

# index = 0
# for item in l:
#     index += 1
#     print(f"The item number {index} is {item}")


for i, item in enumerate(l):
    # The enumerate function returns a tuple (index, item)
    print(f"The item number {i} is {item}")