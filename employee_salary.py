from employee_profile import Employee

# Creating an instance of the Employee class
employee = Employee('matt', 'james', 150000)

# Accessing the initial annual salary
print(employee.annual_salary)

# Giving a default raise of $5000
employee.give_raise()
print(employee.annual_salary)

# Giving a custom raise of $10000
employee.give_raise(8000)
print(employee.annual_salary)



