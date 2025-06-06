class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        return Complex(self.r * c2.r - self.i * c2.i, self.r * c2.i + self.i * c2.r)
    
    def __str__(self):    # This method is called when we print the object
        return f"{self.r} + {self.i}i"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)  # This will call the __add__ method
print(c1 * c2)  # This will call the __mul__ method