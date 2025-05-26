class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n ** 2
    
    def cube(self):
        return self.n ** 3
    
    def square_root(self):
        return self.n ** 0.5
    
    @staticmethod
    def hello():
        print("Hello there!")


a = Calculator(4)
a.hello()  # Calling the static method
print("Square:", a.square())
print("Cube:", a.cube())
print("Square Root:", a.square_root())