class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

my_tesla = ElectricCar(make="Tesla", model="Model S", year=2022, battery_size=100)

print(f"Make: {my_tesla.make}")
print(f"Model: {my_tesla.model}")
print(f"Year: {my_tesla.year}")
print(f"Battery Size: {my_tesla.battery_size}")