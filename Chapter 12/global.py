a = 90

def fun():
    # Using the global keyword to modify the global variable 'a'
    global a
    a = 100
    print("Inside fun:", a)

fun()
print("Outside fun:", a)