class Employee():
    """Represent an employee profile."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Initializing the employee attributes.

        Args:
            first_name (str): the employee's first name
            last_name (str): the employee's last name
            annual_salary (int): the employee's annual salary
        """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, given_raise=5000):
        """Add $5000 to the annual salary by default
        but also accept custom raise amount.
        
        Args:
            given_raise(int): the employee's raise.
        """                 
        self.annual_salary += given_raise
