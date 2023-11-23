
class Vehicle:
    def __init__(self, max_speed, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_mileage(self, distance):
        if distance > 0:
            self.mileage += distance
            print(f"You traveled today {distance} km. Current mileage: {self.mileage} km.")
        else:
            print("Error: Distance can't be zero or negative number.")


my_vehicle = Vehicle(max_speed=180)
my_vehicle.increase_mileage(50)
my_vehicle.increase_mileage(120.5)
