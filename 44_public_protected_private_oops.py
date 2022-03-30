#Public(as it is name), Protected(name start with single '_' underscore),
# private(name start with double '__' underscore) access specifiers
'''Suppose we have one hardcord page with some information of someone and we want to share that info to everyone
then i stick that page out of home (its public). But we want to share that info only to our home members
then i stick that page into the home (its protected). But we want to share that info only with me
then i stick that page into my personal room (its private).'''


class Employee:
    no_of_leaves = 10 # its public anyone can access
    public_var = 8

    #this variable are only allowed to access for base class and objects which is created by the class
    _protected_var = 9

    # this variable are only allowed to access for base class but objects which is created by the class can also access with name mangling python
    __private_var = 98

    # __init__ is constructor
    def __init__(self, name, salary, role):  # self will get object name 'mayank' or 'subodh'
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Age is {self.salary}. Role is {self.role}"

mayank = Employee("Mayank", 25000, "Leader")
print(mayank._protected_var) # access '_protected_var' of 'Employee' class with the help of 'mayank' object of same class
print(mayank._Employee__private_var) # access '__private_var' of 'Employee' class with the help of 'mayank' object of same class and name mangling method
'''name mangling = write a '_'underscore and then add your class name 'Employee' and then
add your private variable '__private_var' which makes '_Employee__private_var' '''