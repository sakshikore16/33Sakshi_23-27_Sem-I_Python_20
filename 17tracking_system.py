# 17. Develop a time tracking system for employees with classes 
# for employees, projects, and time entries. Implement methods 
# for logging hours, generating timesheets, & calculating overtime.

class Employee:
    def __init__(self, employee_id, name):
        self.employee_id, self.name, self.projects = employee_id, name, []

    def log_hours(self, project, hours):
        project.add_time_entry(TimeEntry(hours))

    def generate_timesheet(self):
        timesheet = f"Timesheet for {self.name} (Employee ID: {self.employee_id}):\n"
        timesheet += "\n".join(project.generate_project_timesheet() for project in self.projects)
        return timesheet

    def calculate_overtime(self):
        total_hours = sum(project.calculate_total_hours() for project in self.projects)
        regular_hours, overtime_hours = min(total_hours, 40), max(0, total_hours - 40)
        return regular_hours, overtime_hours

class Project:
    def __init__(self, project_id, name):
        self.project_id, self.name, self.time_entries = project_id, name, []

    def add_time_entry(self, entry):
        self.time_entries.append(entry)

    def generate_project_timesheet(self):
        return f"\nProject: {self.name} (Project ID: {self.project_id})\n" + "".join(entry.generate_time_entry() for entry in self.time_entries)

    def calculate_total_hours(self):
        return sum(entry.hours for entry in self.time_entries)


class TimeEntry:
    def __init__(self, hours):
        self.hours = hours

    def generate_time_entry(self):
        return f"  Hours: {self.hours}\n"

employee = Employee(input("Enter your Employee ID: "), input("Enter your name: "))

projects = [Project("P001", "Project Alpha"), Project("P002", "Project Beta")]
employee.projects.extend(projects)

for project in projects:
    hours = float(input(f"Enter hours worked on {project.name}: "))
    employee.log_hours(project, hours)

print(employee.generate_timesheet())

regular, overtime = employee.calculate_overtime()
print(f"\nTotal Regular Hours: {regular}\nTotal Overtime Hours: {overtime}")
