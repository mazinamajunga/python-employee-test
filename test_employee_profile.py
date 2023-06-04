import unittest
from employee_profile import Employee

# METHOD 1: 
# setUp() has been used to  prepare the test fixture and make the test code very dynamic.
class EmployeeTestCase(unittest.TestCase):
    """Test employee_profile.py"""
        
    def setUp(self):
        """Create an instance of the Employee class with initial values
        and define the annual raise for the salary.
        """
        annual_salary = 150000           # Annual base salary. This variable can be used as a global variable and the code still passes
        self.employee= Employee('Matt', 'James', annual_salary)             # CREATE AN INSTANCE OF THE class Employee
        self.employee.give_raise()                                          # Annual raise
        self.annual_salary = self.employee.annual_salary                    # Annual salary with default raise
        # Each of these is prefixed by self, so they can be used anywhere in the class.
        
    def test_give_default_raise(self):
        """Verify if the annual salary is properly increasing by default.
        """
        # Annual default raise
        self.employee.give_raise()
        # Annual salary with default raise
        self.annual_salary = self.employee.annual_salary
        # Comparing the value of the annual salary with the expected value
        self.assertEqual(self.annual_salary, self.employee.annual_salary)
        
        
    def test_give_custom_raise(self):
        """Verify if the annual salary is properly increasing by the custom amount.
        """
        # Annual custom raise
        self.employee.give_raise(8000)
        # Annual salary with custom raise
        self.annual_salary = self.employee.annual_salary
        # Comparing the value of the annual salary with the expected value
        self.assertEqual(self.annual_salary, self.employee.annual_salary)
        
if __name__ == "__main__":    # Entry point for running the tests.
    unittest.main()              # Testing the class
    
    
    
# SAME AS THE ABOVE ONE WITH SHORTER setUp() 
    
# import unittest
# from employee_profile import Employee

# class EmployeeTestCase(unittest.TestCase):
#     """Test employee_profile.py"""
    
#     def setUp(self):
#         """Create an instance of the Employee class with initial values."""
#         self.employee = Employee('Matt', 'James', 150000)

#     def test_give_default_raise(self):
#         """Verify if the annual salary is properly increasing by default."""
#         # Annual default raise
#         self.employee.give_raise()
#         # Annual salary with default raise
#         default_annual_salary = self.employee.annual_salary
#         # Comparing the value of the annual salary with the expected value
#         self.assertEqual(default_annual_salary, 155000)

#     def test_give_custom_raise(self):
#         """Verify if the annual salary is properly increasing by a custom amount."""
#         # Annual custom raise
#         self.employee.give_raise(8000)
#         # Annual salary with custom raise
#         custom_annual_salary = self.employee.annual_salary
#         # Comparing the value of the annual salary with the expected value
#         self.assertEqual(custom_annual_salary, 158000)   
    
# if __name__ == "__main__":    # Entry point for running the tests.
#     unittest.main()              
    
    

    
    # # THESE TEST BELOW WILL TEST THE "Employee class" WITHOUT THE setUp() METHOD.
    # def test_give_default_raise(self):
    #     """Verify if the annual salary is properly increasing by default.
    #     """
    #     # TO TEST A CLASS WE NEED TO CREATE AN INSTANCE OF THE CLASS.
    #     # CREATE AN INSTANCE OF THE class Employee
    #     employee_1 = Employee('Matt', 'James', 150000)
    #     # Annual default raise
    #     employee_1.give_raise()
    #     # Annual salary with default raise
    #     default_annual_salary = employee_1.annual_salary
    #     # Comparing the the value of first_employee with the default annual salary
    #     self.assertEqual(default_annual_salary, 155000)
        
#     def test_give_custom_raise(self):
#         """Verify if the annual salary is properly increasing by the custom amount.
#         """
#         # TO TEST A CLASS WE NEED TO CREATE AN INSTANCE OF THE CLASS.
#         # CREATE AN INSTANCE OF THE class Employee with the given values
#         employee_1 = Employee('Matt', 'James', 150000)
#         # Annual custom raise
#         employee_1.give_raise(8000)
#         # Annual salary with costum raise
#         custom_annual_salary = employee_1.annual_salary
#         # Comparing the the value of first_employee with the costum annual salary
#         self.assertEqual(custom_annual_salary, 158000)
        