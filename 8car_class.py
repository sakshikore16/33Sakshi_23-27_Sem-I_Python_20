# 8. Create a class called “Car” with attributes like make, model, and year.
# Then, create an object of the “Car” class and print its details.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
year = input("Enter the year of the car: ")

mycar = Car(make=make, model=model, year=year)

print("\n----- Car Details -----")
print("Make:", mycar.make)
print("Model:", mycar.model)
print("Year:", mycar.year)
