class Employee:
    HIGH_SALARY_THRESHOLD = 100000  

    def __init__(self, name, salary):
        self.name = name
        self.salary = float(salary)
        
    def __str__(self):
        return f"Employee name: {self.name}, Salary: {int(self.salary)}"

    @classmethod
    def from_string(cls, emp_string):
        name, salary = emp_string.split(', ')
        return cls(name, float(salary))

    @staticmethod
    def is_high_salary(salary):
        return salary > Employee.HIGH_SALARY_THRESHOLD

emp_string_1 = "Alice, 120000"
employee1 = Employee.from_string(emp_string_1)

print(employee1)

is_high = Employee.is_high_salary(employee1.salary)
print(f"Is the salary high? {is_high}")
