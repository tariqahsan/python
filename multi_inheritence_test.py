# Base class 1
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

# Base class 2
class Walker:
    def walk(self):
        print(f"{self.name} is walking.")

# Base class 3
class AnimalType:

    def __init__(self, group):
        self.group = group
    def type(self):
        print(self.group)

# Derived class (inheriting from both Animal and Walker) example of multiple inheritense
class Dog(Animal, Walker, AnimalType):
    def bark(self):
        print(f"{self.name} is barking.")

# Using the derived class
dog = Dog("Buddy", "Mammal")
dog.eat()   # Inherited from Animal
dog.walk()  # Inherited from Walker
dog.bark()  # Method from Dog class
dog.type()
