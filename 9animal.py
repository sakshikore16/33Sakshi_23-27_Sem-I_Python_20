# 9. Create a base class called “Animal” and two subclasses: 
# “Dog” & “Cat.” Add methods & attributes specific to each subclass.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

    def wag_tail(self):
        return f"{self.name} is wagging its tail."

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "Meow!"

    def purr(self):
        return f"{self.name} is purring."

def get_user_input(prompt):
    return input(prompt)

# Get user input for Dog instance
user_dog = Dog(
    get_user_input("Enter the name of the dog: "),
    get_user_input("Enter the age of the dog: "),
    get_user_input("Enter the breed of the dog: ")
)

# Get user input for Cat instance
mycat = Cat(
    get_user_input("Enter the name of the cat: "),
    get_user_input("Enter the age of the cat: "),
    get_user_input("Enter the color of the cat: ")
)

# Displaying information
print("\n----- Dog Details -----")
print("Name:", user_dog.name)
print("Age:", user_dog.age)
print("Breed:", user_dog.breed)
print("Sound:", user_dog.make_sound())
print("Tail Wagging:", user_dog.wag_tail())
print()

print("----- Cat Details -----")
print("Name:", mycat.name)
print("Age:", mycat.age)
print("Color:", mycat.color)
print("Sound:", mycat.make_sound())
print("Purring:", mycat.purr())
