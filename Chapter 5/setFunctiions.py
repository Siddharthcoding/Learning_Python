A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.add(10)  # Add an element to the set
print(A)

A.remove(10)  # Remove an element from the set
print(A)

A.discard(10)  # Discard an element from the set (no error if not present)
print(A)

print(A.pop())  # Remove and return an arbitrary element from the set

print(A.union(B)) # Union of two sets
print(A | B)  # Union of two sets using the | operator

print(A.intersection(B))  # Intersection of two sets
print(A & B)  # Intersection of two sets using the & operator

print(A.difference(B))  # Difference of two sets
print(A - B)  # Difference of two sets using the - operator

print(A.symmetric_difference(B))  # Symmetric difference of two sets
print(A ^ B)  # Symmetric difference of two sets using the ^ operator

print(A.issubset(B))  # Check if A is a subset of B
print(A.issuperset(B))  # Check if A is a superset of B