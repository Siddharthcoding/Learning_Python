class Employee:
    language = "Python"          # Class attribute i.e, shared by all instances

Siddharth = Employee()
Siddharth.name = "Siddharth"     # Adding a new attribute, instance attribute
print(Siddharth.name, Siddharth.language)

Mark = Employee()
Mark.name = "Mark"               
print(Mark.name, Mark.language)