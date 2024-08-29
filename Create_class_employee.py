class Employee:
    num_employees = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.num_employees += 1

    @classmethod
    def average_salary(cls, employees):
        if len(employees) == 0:
            return 0  # Avoid division by zero if the list is empty
        total_salary = sum(emp.salary for emp in employees)
        return total_salary / len(employees)

    def __str__(self):
        return f"Employee(name={self.name}, family={self.family}, salary={self.salary}, department={self.department})"


class FulltimeEmployee(Employee):
    def __init__(self, name, family, salary, department, benefits):
        super().__init__(name, family, salary, department)
        self.benefits = benefits

    def __str__(self):
        return (f"FulltimeEmployee(name={self.name}, family={self.family}, salary={self.salary}, "
                f"department={self.department}, benefits={self.benefits})")


# Create instances of Employee and FulltimeEmployee
employee1 = Employee("Sai Likhit", "Family 1", 75000, "manager")
employee2 = Employee("Swetha", "Family 2", 80000, "IT")
employee3 = Employee("Prudhvi", "Family3", 115000, "Team lead")
employee4 = Employee("Akash", "Family 4", 125000, "Team lead")

fulltime_employee1 = FulltimeEmployee("Manish Katiki", "Family 5", 95000, "hospital", "Healthcare")
fulltime_employee2 = FulltimeEmployee("Partha Saradhi", "Family 6", 95000, "Finance", "manager")

# List of all employees
employees = [employee1, employee2, employee3, employee4, fulltime_employee1, fulltime_employee2]

# Call member functions and print results
avg_salary = Employee.average_salary(employees)
print(f"Total number of employees: {Employee.num_employees}")
print(f"Average salary: {avg_salary}")

# Print details of each employee
print("\nEmployee details:")
for emp in employees:
    print(emp)
