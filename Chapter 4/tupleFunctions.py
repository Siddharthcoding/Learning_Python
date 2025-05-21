t = (1, 2, 2, 3, 2)

print(len(t))  # Getting the length of the tuple

print(t.count(2))  # Counting the occurrences of 2 in the tuple

print(t.index(2))  # Getting the index of the first occurrence of 2 in the tuple

print(3 in t)  # Checking if 3 is in the tuple , returns a boolean value

print(t[1:4])  # Slicing the tuple

# t[0] = 5  # This will raise a TypeError because tuples are immutable

a = (1, 2)
b = (3, 4)

c = a + b  # Concatenating tuples
print(c)

d = a * 3  # Repeating tuples
print(d)

t = (10, 20, 30)
a, b, c = t
print(a, b, c)  # Unpacking the tuple, i.e. assigning the values of the tuple to variables
