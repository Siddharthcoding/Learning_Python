class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Boww Boww Bowww Bowww Bowwww")


d = Dog()
d.bark()  # Calling the static method bark from the Dog class