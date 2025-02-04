# Employee Management System using OOP

class Employee:
    """Represents an employee."""

    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_info(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}"


class Manager(Employee):
    """Represents a manager who manages a team."""

    def __init__(self, name, emp_id, department, team_size):
        super().__init__(name, emp_id, department)
        self.team_size = team_size

    def display_info(self):
        return f"{super().display_info()}, Team Size: {self.team_size}"


# Create employee and manager objects
emp1 = Employee("Alice", 101, "HR")
mgr1 = Manager("Bob", 201, "IT", 5)

# Display details
print(emp1.display_info())  # Output: ID: 101, Name: Alice, Department: HR
print(mgr1.display_info())  # Output: ID: 201, Name: Bob, Department: IT, Team Size: 5
