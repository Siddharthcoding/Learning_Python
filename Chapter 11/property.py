class Employee:
    a = 1

    @property      # This is a property, i.e. it allows us to access the method like an attribute
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter  # This is a setter, i.e. it allows us to set the value of the property
    def name(self, name):
        fname, lname = name.split(" ")
        self.fname = fname
        self.lname = lname

e = Employee()
e.name = "Siddharth Mishra"

print(e.name)  # This will call the name method of the class Employee