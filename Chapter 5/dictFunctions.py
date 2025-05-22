marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92,
}

print(marks.items())   # Returns a view object that displays a list of a dictionary's key-value tuple pairs
print(marks.keys())    # Returns a view object that displays a list of all the keys in the dictionary
print(marks.values())   # Returns a view object that displays a list of all the values in the dictionary

marks.update({"Charlie": 98, "New": 100})  # Updates the dictionary with the key-value pairs from another dictionary
print(marks)

print(marks.get("NotPresent")) # Returns None if the key is not found
print(marks["NotPresent"])  # Raises KeyError if the key is not found