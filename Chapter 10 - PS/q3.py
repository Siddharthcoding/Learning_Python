class Test:
    a = 4

o = Test()

print(o.a)  # Prints class attribute because instance does not have its own 'a' attribute
o.a = 5     # Now 'o' has its own instance attribute 'a', which overrides the class attribute
print(o.a)  

print(Test.a)  # Class attribute remains unchanged