name = "Siddharth"

print(len(name))    # Length of the string
print(name.lower())   # Convert to lower case
print(name.upper())   # Convert to upper case
print(name.swapcase()) # Swap case of the string
print(name.startswith("Sid"))  # Check if string starts with "Sid", returns boolean value
print(name.endswith("th"))  # Check if string ends with "arth", returns boolean value

print(name.find("id"))  # Find the first index of "Sid" in the string, returns -1 if not found
print(name.count('h'))   # Count the number of occurrences of 'h' in the string
print(name.replace('h', 'z'))  # Replace all occurences of 'h' with 'z' in the string

s = "  Hello World  "

print(s.strip())  # Remove leading and trailing spaces

s = "hello world"

print(s.capitalize())   # Capitalize the first letter of the string
print(s.title())       # Capitalize the first letter of each word in the string

s = "apple,banana,grape"
print(s.split(","))    # Split the string into a list using ',' as the delimiter

words = ['Hello', 'World']
print(" ".join(words))   # Join the list of words into a string using ' ' as the delimiter

print("Abc".isalpha())  # Check if the string contains only alphabetic characters, returns boolean value
print("123".isdigit())  # Check if the string contains only digits, returns boolean value
print("123abc".isalnum())  # Check if the string contains only alphanumeric characters, returns boolean value
