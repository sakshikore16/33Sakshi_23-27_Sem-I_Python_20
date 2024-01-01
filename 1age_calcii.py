# 1. Write a Python program to create a person class. 
# Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.

class Person:
    def __init__(self, name, country, birth_day, birth_month, birth_year):
        self.name = name
        self.country = country
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year

    def calculate_age(self, current_year):
        age = current_year - self.birth_year
        if (self.birth_day, self.birth_month) > (self.birth_day, self.birth_month, current_year):
            age -= 1
        return age

name = input("Enter the person's name: ")
country = input("Enter the person's country: ")
birth_day = int(input("Enter the birth day (DD): "))
birth_month = int(input("Enter the birth month (MM): "))
birth_year = int(input("Enter the birth year (YYYY): "))

person = Person(name, country, birth_day, birth_month, birth_year)

current_year = int(input("Enter the current year: "))

age = person.calculate_age(current_year)
print(f"{person.name} is {age} years old.")
