class Vehicle:
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed

    def __str__(self):
        return f"Vehicle {self.number}, Max Speed: {self.max_speed} km/h"


class Bus(Vehicle):
    def __init__(self, number, max_speed, monthly_fuel_comsumption):
        super().__init__(number, max_speed)
        self.monthly_fuel_consumption = monthly_fuel_comsumption

    def __str__(self):
        return f"Bus {self.number}, Max Speed: {self.max_speed} km/h, Monthly Fuel Consumption: {self.monthly_fuel_consumption} liters"


class Tram(Vehicle):
    def __init__(self, number, max_speed, num_wagons):
        super().__init__(number, max_speed)
        if 0 < num_wagons < 4:
            self.num_wagons = num_wagons
        else:
            raise ValueError("Tram can have only 1 - 3 wagons!")

    def __str__(self):
        return f"Tram {self.number}, Max Speed: {self.max_speed} km/h, Wagons: {self.num_wagons}"


class Depot:
    def __init__(self, name, vehicle_type):
        self.name = name
        self.vehicle_type = vehicle_type
        self.vehicles_in_the_depot = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, self.vehicle_type):
            raise TypeError(f"{vehicle.__class__.__name__} is not a {self.vehicle_type.__name__} type!")
        self.vehicles_in_the_depot.append(vehicle)


    def total_fuel_consumption(self):
        if self.vehicle_type == Bus:
            return sum(bus.monthly_fuel_consumption for bus in self.vehicles_in_the_depot)
        return 0

    def __str__(self):
        result = f"Depot {self.name}, Vehicle Type: {self.vehicle_type.__name__}\n"
        for vehicle in self.vehicles_in_the_depot:
            result += f"  {vehicle}\n"
        if self.vehicle_type == Bus:
            result += f"  Total Fuel Consumption: {self.total_fuel_consumption()} liters\n"
        elif self.vehicle_type == Tram:
            result += f"  Total Number of Wagons: {sum(tram.num_wagons for tram in self.vehicles_in_the_depot)}\n"
        return result


bus1 = Bus(101, 60, 2000)
bus2 = Bus(102, 55, 1500)
tram1 = Tram(201, 50, 2)
tram2 = Tram(202, 45, 3)

bus_depot = Depot("Bus Depot", Bus)
tram_depot = Depot("Tram Depot", Tram)

bus_depot.add_vehicle(bus1)
bus_depot.add_vehicle(bus2)
tram_depot.add_vehicle(tram1)
tram_depot.add_vehicle(tram2)

print(bus_depot)
print(tram_depot)
