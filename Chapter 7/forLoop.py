for i in range(5):  # range(5) generates numbers from 0 to 4
    print(i)

for i in range(1, 6):  # range(1, 6) generates numbers from 1 to 5
    print(i)

# The range function can also be used to generate a sequence of numbers with a specific step size.
    
for i in range(1, 10, 2):  # range(1, 10, 2) generates numbers from 1 to 9 with a step of 2
    print(i)

# The range function can also be used to generate a sequence of numbers in reverse order.
    
for i in range(10, 0, -1):  # range(10, 0, -1) generates numbers from 10 to 1
    print(i)

l = [1, 2, 3, 4, 5]

for i in l:  # Iterating through the list
    print(i)