'''This module creates departments for a fictitious company.

    Classes: Department, HR, Admin, Sales
'''

class Department():
    '''Parent class for all departments

    Properties: name, supervisor, employee_count
    
    Methods: __init__, add_employee, get_employees, meet
    '''

    def __init__(self, name, supervisor, employee_count):
        '''Initializes the 'Department' class.

        Arguments:
        name (string)
        supervisor (string)
        employee_count(integer)
        '''

        self.employees = set()
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.budget = 40000

    @property
    def name(self):
        '''Gets the department name.'''
        try:
            return self.__name
        except AttributeError:
            return ''

    @name.setter
    def name(self, val):
        '''Sets the department name.'''
        self.__name = val

    @property
    def supervisor(self):
        '''Gets the department supervisor.'''
        try:
            return self.__supervisor 
        except AttributeError:
            return ''

    @supervisor.setter
    def supervisor(self, val):
        '''Sets the department supervisor.'''
        self.__supervisor = val

    @property
    def employee_count(self):
        '''Gets the employee count.'''
        try: 
            return self.__employee_count
        except AttributeError:
            return ''

    @employee_count.setter
    def employee_count(self, val):
        '''Sets the employee count.
        '''
        self.__employee_count = val

    def add_employee(self, employee):
        '''Adds an employee to the 'employees' set.

        Arguments:
        employee(string)
        '''

        self.employees.add(employee)

    def get_employees(self):
        '''Returns the 'employees' set.

        Arguments: 
        NONE
        '''
        return employees

    def meet(self):
        '''Prints a message identifying a meeting location.
        '''
        print("Everyone meet in {}'s office.".format(self.supervisor))

    def get_budget(self):
      '''Returns base budget for Department'''
      return self.budget


class HR(Department):
    '''Class for representing Human Resources department.

    Methods: __init__, add_policy
    '''

    def __init__(self, name, supervisor, employee_count):
        '''Initializes the 'HR' class, which builds on the 'Department' class.
        '''
        
        super().__init__(name, supervisor, employee_count)
        self.policies = dict()
        self.budget = super().get_budget() - 222

    def add_policy(self, policy_name, policy_text):
        '''Adds a policy, as a tuple, to the set of policies

        Arguments:
            policy_name (string)
            policy_text(string)
        '''
        self.policies[policy_name] = policy_text

    def meet(self):
        '''Prints a message identifying a meeting location for the Human Resources department
        '''
        print("Everyone meet in the Human Resources conference room.")
        
class Admin(Department):
    '''Class for representing the Administration Department

    Methods: __init__
    '''

    def __init__(self, name, supervisor, employee_count):
        '''Initializes the 'Admin' class, which builds on the 'Department' class.
        '''
        super().__init__(name, supervisor, employee_count)
        self.budget = super().get_budget() + 111

    def meet(self):
        '''Prints a message identifying a meeting location for the Human Resources department
        '''
        print("Everyone meet in the board room.")

class Sales(Department):
    '''Class for representing the Sales Department

    Methods: __init__
    '''

    def __init__(self, name, supervisor, employee_count):
        '''Initializes the 'Sales' class, which builds on the 'Department' class.
        '''
        Department.__init__(self, name, supervisor, employee_count)
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count
        self.budget = super().get_budget() + 3333

    def meet(self):
        '''Prints a message identifying a meeting location for the Human Resources department
        '''
        print("Call 1-800-263-3476. The pass code to access the conference call is #2937.")

hr_department = HR("Human Resources", "Shawn", 2)
admin_department = Admin("Administration", "Elijah", 4)
sales_department = Sales("Sales", "Savannah", 6)
print(hr_department.name)
print(admin_department.name)
print(sales_department.name)

hr_department.add_policy("1.1", "Policy 1.1")
hr_department.add_policy("1.2", "Policy 1.2")
print(hr_department.policies)
print(sales_department.meet())
print(sales_department.budget)
