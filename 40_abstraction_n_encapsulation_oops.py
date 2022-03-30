# abstraction and encapsulation
'''Abstraction is typical code which we write to run and encapsulation is the way to run
the code which is written in abstraction. encapsulation is like a capsule which has multiple
things but we just see capsule'''
class Employee:
    no_of_leaves = 8

    #static method
    @staticmethod
    def printgood(string_val):
        return "This is good " + string_val

    # __init__ is constructor
    def __init__(self, name, salary, age):  # self will get object name 'mayank' or 'subodh'
        self.name = name
        self.salary = salary
        self.age = age

    # class method
    @classmethod
    def from_string(cls, str_val):
        return cls(*str_val.split("-"))  # it will also return list of ['Rohan', '45000', '28']

mayank = Employee("Mayank", 25000, 23) #if we provide argument to a class name then it will handle by __init__
subodh = Employee("Subodh", 40000, 30) #if we provide argument to a class name then it will handle by __init__
rohan = Employee.from_string("Rohan-45000-28") # create instance with string
print(rohan.printgood("Shera")) # static method access with the help of instance
print(Employee.printgood("Veerji")) # static method access with the help of class