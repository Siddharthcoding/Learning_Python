a = 21
t = type(a)
print(t)      # <class 'int'>

b = "Siddharth"
t = type(b)
print(t)      # <class 'str'>

c = "3.14"
d = float(c)  # Convert string to float
t = type(d)
print(t)

int("10")   # 10
float("10.5")  # 10.5
bool(0)    # False
str(100)  # '100'
list("hello")  # ['h', 'e', 'l', 'l', 'o']
tuple([1, 2, 3])  # (1, 2, 3)
set([1, 2, 2, 3])  # {1, 2, 3}
dict([1, 'a'], [2, 'b'])  # {1: 'a', 2: 'b'}