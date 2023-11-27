from datetime import datetime


class Tank:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.water_level = 0
        self.operations_history = []

    # REJESTRACJA HISTORII
    def record_operation(self, operation_type, volume, success, from_tank=None, to_tank=None):
        timestamp = datetime.now()
        operation_data = (self.name, volume, self.water_level, success, operation_type, from_tank, to_tank, timestamp)
        self.operations_history.append(operation_data)

    # NAPEŁNIAMY WODĘ
    def pour_water(self, volume):
        if volume > 0:
            if self.water_level + volume <= self.capacity:
                self.water_level += volume
                self.record_operation("pour_water", volume, success=True)
            else:
                self.record_operation("pour_water", volume, success=False)
                print("Cannot pour more water than the tank's capacity.")

    # WYLEWAMY WODĘ
    def pour_out_water(self, volume):
        if volume > 0:
            if volume <= self.water_level:
                self.water_level -= volume
                self.record_operation("pour_out_water", volume, success=True)
            else:
                self.record_operation("pour_out_water", volume, success=False)
                print("Cannot pour out more water than is available in the tank.")

    # PRZELEWAMY WODĘ DO INNEGO ZBIORNIKA
    def transfer_water(self, from_tank, volume):
        # I. condition - poziom wody do przelania musi być większy od zera
        if volume > 0:

            # II. condition - poziom wody w tanku, z którego będzie brana woda,
            # musi być wyższy albo równy ilości wody do transferu
            if from_tank.water_level >= volume:

                # III. condition - poziom wody po przelaniu musi mieścić się w capacity tanku,
                # do którego ma być przelana woda
                if self.water_level + volume <= self.capacity:
                    # Operacje zmiany wartości wody w zbiornikach
                    from_tank.water_level -= volume
                    self.water_level += volume

                    # Zapisz operację w historii obu zbiorników
                    self.record_operation("transfer_water_out", volume, success=True, from_tank=from_tank, to_tank=self)
                    from_tank.record_operation("transfer_water_in", volume, success=True, from_tank=from_tank,
                                               to_tank=self)

                else:
                    self.record_operation("transfer_water_out", volume, success=False, from_tank=from_tank)
                    print("Cannot transfer more water than the receiving tank's capacity.")
            else:
                self.record_operation("transfer_water_out", volume, success=False, from_tank=from_tank)
                print("Cannot transfer more water than is available in the source tank.")
        else:
            print("Water volume must be greater than zero!")

    def check_state(self):
        current_water_level = 0

        for operation in self.operations_history:
            if operation[3]:  # Sprawdź, czy operacja była udana
                if operation[4] == "pour_water" and operation[0] == self.name:
                    current_water_level += operation[1]
                elif operation[4] == "pour_out_water" and operation[0] == self.name:
                    current_water_level -= operation[1]
                elif operation[4] == "transfer_water_out":
                    # Źródło wody (from_tank) odejmuje wodę
                    current_water_level += operation[1]
                elif operation[4] == "transfer_water_in":
                    # Docelowy zbiornik dodaje wodę
                    current_water_level -= operation[1]

        # print("Current water level:", current_water_level)
        # print("Expected water level:", self.water_level)
        return current_water_level == self.water_level


def find_tank_with_max_water(tanks):
    max_water_tank = max(tanks, key=lambda tank: tank.water_level, default=None)
    return max_water_tank


def find_most_filled_tank_percentage(tanks):
    most_filled_tank = max(tanks, key=lambda tank: tank.water_level / tank.capacity if tank.capacity > 0 else 0,
                           default=None)
    if most_filled_tank:
        # KONWERSJA NA PROCENTY
        fill_percentage = (most_filled_tank.water_level / most_filled_tank.capacity) * 100
        return most_filled_tank, fill_percentage
    else:
        return None


def find_empty_tanks(tanks):
    empty_tanks = [tank for tank in tanks if tank.water_level == 0]
    return empty_tanks


def find_tank_with_most_failures(tanks):
    failure_counts = {}
    for tank in tanks:
        for operation in tank.operations_history:
            # Check if the operation was not successful
            if not operation[3]:
                tank_name = operation[0]
                failure_counts[tank_name] = failure_counts.get(tank_name, 0) + 1
    return max(failure_counts, key=failure_counts.get, default=None)


def find_tank_with_most_operations(tanks, operation_type):
    operation_counts = {}
    for tank in tanks:
        for operation in tank.operations_history:
            if operation[4] == operation_type:
                tank_name = operation[0]
                operation_counts[tank_name] = operation_counts.get(tank_name, 0) + 1
    return max(operation_counts, key=operation_counts.get, default=None)


tank1 = Tank("Tank1", 100)
tank2 = Tank("Tank2", 150)

tank1.pour_water(50)
tank2.transfer_water(tank1, 30)
tank1.pour_out_water(20)
tank1.pour_water(50)
tank2.transfer_water(tank1, 30)
tank1.transfer_water(tank2, 60)
tank1.transfer_water(tank2, 60)

tanks = [tank1, tank2]

max_water_tank = find_tank_with_max_water(tanks)
print("Tank with max water:", max_water_tank.name if max_water_tank else "There isn't such a tank.")

most_filled_tank, fill_percentage = find_most_filled_tank_percentage(tanks)
if most_filled_tank:
    print(f"Most filled tank: {most_filled_tank.name}, Fill Percentage: {fill_percentage}%")
else:
    print("There isn't such a tank.")

empty_tanks = find_empty_tanks(tanks)
print("Empty tanks:", [tank.name for tank in empty_tanks])

print("Tank with most failures:", find_tank_with_most_failures(tanks))

print("Tank with most pour_water operations:", find_tank_with_most_operations(tanks, "pour_water"))

print("Is state consistent for tank1?", tank1.check_state())
print("Is state consistent for tank2?", tank2.check_state())
