# Create Employee Class
class Employee:
    def __init__(self, first_name, last_name, actual_salary):
        self.fname = first_name
        self.lname = last_name
        self.salary = actual_salary

    # Calculate Pay check Method
    def calculate_paycheck(self):
        return self.salary/52    