class Employee:
    language = "Python"          

Siddharth = Employee()
Siddharth.language = "JavaScript"  # Instance attribute, overrides class attribute
print(Siddharth.language)