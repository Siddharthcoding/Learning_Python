class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Siddharth", 3000000, 123456)
print(p.name, p.salary, p.pincode, p.company)