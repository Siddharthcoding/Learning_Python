class Employee:
    language = "Javascript"   

    def __init__(self, name, language):  # Constructor method, called when an instance is created, It is a dunder method
        print("Creating an object")
        self.name = name                # Instance attribute, unique to each instance
        self.language = language

    # self is a reference to the current instance of the class and is used to access variables and methods associated with the instance.
    def get_info(self):     
        print(f"The language is {self.language}.")   

    @staticmethod    # Static method, does not require an instance to be called
    def greet():
        print("Good Morning!") 

Siddharth = Employee("Siddharth", "Python")  # Instance of Employee, constructor is called

print(Siddharth.name + " is learning " + Siddharth.language)
