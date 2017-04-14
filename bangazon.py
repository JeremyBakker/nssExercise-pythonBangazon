class Department():
    '''Parent class for all departments

    Properties: name, supervisor, employee_count
    
    Methods: __init__, add_employee, get_employees
    '''

    def __init__(self):
        self.employees = set()

    @property
    def name(self):
        try:
            return self.__name
        except AttributeError:
            return ''

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def supervisor(self):
        try:
            return self.__supervisor 
        except AttributeError:
            return ''

    @supervisor.setter
    def supervisor(self, val):
        self.__supervisor = val

    @property
    def employee_count(self):
        try: 
            return self.__employee_count
        except AttributeError:
            return ''

    @employee_count.setter
    def employee_count(self, val):
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

class HR(Department):
    '''Class for representing Human Resources department.

    Methods: __init__, add_policy
    '''

    def __init__(self, name, supervisor, employee_count):
        Department.__init__(self)
        self.policies = dict()
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count

    def add_policy(self, policy_name, policy_text):
        '''Adds a policy, as a tuple, to the set of policies

        Arguments:
            policy_name (string)
            policy_text(string)
        '''
        self.policies[policy_name] = policy_text
        
class Admin(Department):
    '''Class for representing the Administration Department

    Methods: __init__
    '''

    def __init__(self, name, supervisor, employee_count):
        Department.__init__(self)
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count

class Sales(Department):
    '''Class for representing the Sales Department

    Methods: __init__
    '''

    def __init__(self, name, supervisor, employee_count):
        Department.__init__(self)
        self.name = name
        self.supervisor = supervisor
        self.employee_count = employee_count


hr_department = HR("Human Resources", "Shawn", 2)
admin_department = Admin("Administration", "Elijah", 4)
sales_department = Sales("Sales", "Savannah", 6)
print(hr_department.name)
print(admin_department.name)
print(sales_department.name)

hr_department.add_policy("1.1", "Policy 1.1")
hr_department.add_policy("1.2", "Policy 1.2")
print(hr_department.policies)