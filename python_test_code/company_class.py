# This is for company class and this should have access to employee class.
from employee_class import Employee

# Define Company Class
class Company:
    def __init__(self):
        self.employees = []

    # define method
    def add_employee(self,new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current Employees:")
        for employee_list in self.employees:
            print(employee_list.fname, employee_list.lname)
        print("-------------------------------------")  

    def pay_employee(self):
        print("Paying Employee:")
        for employee_list in self.employees:
            print("Pay For:", employee_list.fname, employee_list.lname)
            print(f"Amount: ${employee_list.calculate_paycheck():,.2f}")  
            print("----------------------------------")

#main function
def main():
    my_company = Company()

    employee1 = Employee("Naveen", "S", 50000)
    my_company.add_employee(employee1)
    employee2 = Employee("Bipsa", "P", 60000)
    my_company.add_employee(employee2)
    employee3 = Employee("Geetha", "K", 70000)
    my_company.add_employee(employee3)    

    #print(my_company.employees)
    my_company.display_employees()
    my_company.pay_employee()

main()