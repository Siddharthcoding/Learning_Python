class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print("Addition:", v1 + v2)  # This will call the __add__ method
print("Multiplication:", v1 * v2)  # This will call the __mul__ method