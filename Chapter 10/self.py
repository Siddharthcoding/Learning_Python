class Employee:
    language = "Python"   

    # self is a reference to the current instance of the class and is used to access variables and methods associated with the instance.
    def get_info(self):     
        print(f"The language is {self.language}.")   

    @staticmethod    # Static method, does not require an instance to be called
    def greet():
        print("Good Morning!") 

Siddharth = Employee()
Siddharth.language = "JavaScript"  # Instance attribute, overrides class attribute
Siddharth.greet()       # It is internally called as Employee.greet(Siddharth)

Siddharth.get_info()     # It is internally called as Employee.get_info(Siddharth)
Employee.get_info(Siddharth)

