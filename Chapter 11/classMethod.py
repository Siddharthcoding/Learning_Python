class Test:
    a = 1

    @classmethod    # This is a class method, i.e. it belongs to the class, not the instance
    def show(cls):
        print(f"The value of a is {cls.a}")

ob = Test()
ob.a = 2
ob.show()  # This will call the show method of the class Test