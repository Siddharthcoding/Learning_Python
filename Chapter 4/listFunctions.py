data = ["Apple", "Mango", 4, 21.5, True, "Bird"]

print(data)
data.append("Siddharth")  # Adding an element to the list from the end
print(data)

print(data.index(4))   # Getting the index of the first occurrence of 4

l1 = [1, 27, 39, 14, 5]

l1.sort()  # Sorting the list in ascending order
print(l1)

l1.reverse()  # Reversing the list
print(l1)

l1.insert(3, 4)  # Inserting an element at index 3
print(l1)

l1.remove(4)  # Removing the first occurrence of 4 from the list
print(l1)

l1.pop(2)  # Removing the element at index 2
print(l1)

print(len(l1))  # Getting the length of the list

print(l1.index(14))  # Getting the index of the first occurrence of 14