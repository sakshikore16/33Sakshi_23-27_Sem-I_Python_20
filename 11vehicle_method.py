# 11. Create a base class called “Vehicle” with a method called “drive.” 
# Implement two subclasses, “Car” and “Bicycle,” that inherit 
# from “Vehicle” & override the “drive” method with their own implementations.

class Vehicle:
    def drive(self):
        print("Generic vehicle is being driven.")


class Car(Vehicle):
    def drive(self):
        print("Car is on the road, driving smoothly.")


class Bicycle(Vehicle):
    def drive(self):
        print("Bicycle is pedaling along the path.")


vehicle_type = input("Enter vehicle type (Car/Bicycle): ").lower()

if vehicle_type == "car":
    vehicle = Car()
elif vehicle_type == "bicycle":
    vehicle = Bicycle()
else:
    print("Invalid vehicle type. Please enter 'Car' or 'Bicycle'.")
    exit()

vehicle.drive()
