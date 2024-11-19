# Define a class called 'Car'
class Car:
    # Constructor method to initialize the attributes
    def __init__(self, make, model, year):
        self.make = make      # Car manufacturer (e.g., 'Toyota')
        self.model = model    # Car model (e.g., 'Camry')
        self.year = year      # Car production year (e.g., 2021)
    
    # Method to display car details
    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")
    
    # Method to calculate car age
    def car_age(self, current_year):
        return current_year - self.year

# Create an object (instance) of the Car class
my_car = Car("Toyota", "Camry", 2021)

# Call the display_info method on the object
my_car.display_info()

# Calculate and display the car's age
current_year = 2024
age = my_car.car_age(current_year)
print(f"The car is {age} years old.")
