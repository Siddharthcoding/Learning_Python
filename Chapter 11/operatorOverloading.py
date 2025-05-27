class Test:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = Test(5)
m = Test(10)

# Using the __add__ method to overload the + operator
print(n + m)  # This will call the __add__ method of the class Test