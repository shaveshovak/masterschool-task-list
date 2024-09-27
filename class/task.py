# Employee class
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, percentage):
        # Increase salary by a given percentage
        self.salary += self.salary * (percentage / 100)

    def __str__(self):
        # Return string representation of the employee details
        return f"Employee Name: {self.name}, Position: {self.position}, Salary: {self.salary:.2f}"


# Manager class (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, position, salary):
        super().__init__(name, position, salary)
        self.employees_under = []  # List to store employees managed by this manager

    def add_employee(self, employee):
        # Add an employee under this manager
        if employee not in self.employees_under:
            self.employees_under.append(employee)

    def remove_employee(self, employee):
        # Remove an employee from this manager's list
        if employee in self.employees_under:
            self.employees_under.remove(employee)

    def list_employees(self):
        # List all employees managed by the manager
        if not self.employees_under:
            print(f"{self.name} manages no employees.")
        else:
            print(f"{self.name} manages the following employees:")
            for emp in self.employees_under:
                print(f" - {emp.name} ({emp.position}, Salary: {emp.salary:.2f})")

    def __str__(self):
        # Return string representation of the manager details
        return f"Manager Name: {self.name}, Position: {self.position}, Salary: {self.salary:.2f}"


# Example usage
if __name__ == "__main__":
    # Creating some employee objects
    emp1 = Employee("Alice", "Developer", 50000)
    emp2 = Employee("Bob", "Designer", 45000)
    emp3 = Employee("Charlie", "Tester", 40000)

    # Creating a manager object
    manager = Manager("Diana", "Team Lead", 70000)

    # Adding employees under the manager
    manager.add_employee(emp1)
    manager.add_employee(emp2)

    # Listing employees under the manager
    manager.list_employees()

    # Giving a raise to an employee
    emp1.give_raise(10)
    print(f"\nAfter raise:\n{emp1}")

    # Removing an employee and listing again
    manager.remove_employee(emp2)
    print("\nAfter removing Bob:")
    manager.list_employees()

    # Manager's details
    print("\nManager details:")
    print(manager)