'''Python Class'''
"Car"
class Car:
    def __init__(self, brand= "Unknown", color= "White"):
        self.brand = brand
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")

car1 = Car()

car1.display_info()

print()

car2 = Car("Toyota", "Red")

car2.display_info()


"Animals"

class Animal:
  def speak(self):
    print("Animal makes a sound")

class Dog(Animal):
  def speak(self):
    return ("Woof!")

animal1 = Animal()
dog1 = Dog()

animal1.speak()
dog1.speak()


"Polymorphism (Method Overloading)"

class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b


class AdvanceMath(MathOperations):
    def add(self, a, b, c=None):
        if c is not None:
            return a * b * c
        else:
            return a * b
math1 = MathOperations()
math2 = AdvanceMath()
print(math1.add(13, 32, 57))
print(math2.add(19, 25, 33))