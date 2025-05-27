class Employee:
    company = "Google"
    def show(self):
        print(f"The name of employee is {self.name} and company is {self.company}")

# Inheritance allows us to create a new class that is based on an existing class.
class Programmer(Employee): 
    company = "Microsoft"
    def showLanguage(self):
        print(f"The name of programmer is {self.name} and language is {self.language}")


a = Employee()
a.name = "Siddharth"
a.show()

b = Programmer()
b.name = "Rohan"
b.language = "Python"
b.show()