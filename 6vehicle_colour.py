# 6. Define a class attribute “color” with a default value white. 
# i.e., Every Vehicle should be white.

class Vehicle:
    colour = "white"

user_colour = input("Enter the colour of the vehicle: ")

vehicle_instance = Vehicle()
vehicle_instance.colour = user_colour if user_colour else Vehicle.colour

print("The colour of the vehicle is:", vehicle_instance.colour)
