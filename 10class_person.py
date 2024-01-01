# 10. Create three classes, “Person,” “Employee,” and “Student.” 
# Use multiple inheritance to create a class “PersonInfo” that 
# inherits from both “Employee” and “Student.” 
# Add attributes and methods specific to each class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self, employee_id, salary, name, age):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}, Salary: ${self.salary}")


class Student(Person):
    def __init__(self, student_id, grade, name, age):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade

    def display_student_info(self):
        print(f"Student ID: {self.student_id}, Grade: {self.grade}")


class PersonInfo(Employee, Student):
    def __init__(self, employee_id, salary, student_id, grade, name, age):
        Employee.__init__(self, employee_id, salary, name, age)
        Student.__init__(self, student_id, grade, name, age)


name = input("Enter name: ")
age = input("Enter age: ")

employee_id = input("Enter employee ID: ")
salary = input("Enter salary: ")

student_id = input("Enter student ID: ")
grade = input("Enter marks: ")

person_info = PersonInfo(employee_id, salary, student_id, grade, name, age)

person_info.display_info()
person_info.display_employee_info()
person_info.display_student_info()
