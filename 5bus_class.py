# 5. Create a Bus child class that inherits from the Vehicle class. 
# The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def calculate_fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()

        maintenance_charge = 0.1 * base_fare

        total_fare = base_fare + maintenance_charge

        return total_fare

bus_capacity = int(input("Enter the seating capacity of the bus: "))

bus_instance = Bus(capacity=bus_capacity)

fare = bus_instance.calculate_fare()
print(f"The total fare for the bus is: ₹{fare:.2f}")
