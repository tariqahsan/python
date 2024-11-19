# Base class 1: Mammal
class Mammal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing air.")

# Base class 2: Fish
class Fish:
    def swim(self):
        print(f"{self.name} is swimming.")

# Base class 3: Bird
class Bird:
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class: Platypus (inherits from Mammal, Fish, Bird)
class Platypus(Mammal, Fish, Bird):
    def __init__(self, name):
        # Call the constructor of Mammal (primary base class)
        super().__init__(name)

    def lay_eggs(self):
        print(f"{self.name} lays eggs.")

# Using the derived class
platypus = Platypus("Perry")
platypus.breathe()  # Inherited from Mammal
platypus.swim()     # Inherited from Fish
platypus.fly()      # Inherited from Bird (although platypuses don't fly!)
platypus.lay_eggs() # Method from Platypus class
