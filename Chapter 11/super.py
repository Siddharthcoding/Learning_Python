class Employee:
    a = 1
    def __init__(self) -> None:
        print("Constructor of Employee")

class Programmer(Employee):
    b = 2
    def __init__(self) -> None:
        print("Constructor of Programmer")

class Coder(Programmer):
    c = 3
    def __init__(self) -> None:
        super().__init__()       # Call the constructor of Programmer
        print("Constructor of Coder")

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

o = Coder()
print(o.a, o.b, o.c)