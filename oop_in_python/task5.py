class Vehicle:
    def __init__(self, make, model, year):
        print("Vehicle's __init__ called")
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size):
        print("ElectricCar's __init__ called")
        super().__init__(make, model, year)
        
        self.battery_size = battery_size

my_electric_car = ElectricCar(make="Tesla", model="Model X", year=2023, battery_size=120)

print("\n--- Vehicle Details ---")
print(f"Make: {my_electric_car.make}")
print(f"Model: {my_electric_car.model}")
print(f"Year: {my_electric_car.year}")
print(f"Battery Size: {my_electric_car.battery_size}")