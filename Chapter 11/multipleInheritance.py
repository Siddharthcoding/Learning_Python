class Employee:
    company = "Google"
    def show(self):
        print(f"The name of employee is {self.name} and company is {self.company}")

class Coder:
    language = "C++"
    def printLanguage(self):
        print(f"The name of coder is {self.name} and language is {self.language}")

# Multiple inheritance allows us to inherit from more than one class.
class Programmer(Employee, Coder): 
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
b.showLanguage()
b.printLanguage()