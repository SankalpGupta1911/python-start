# Dunder methods = start with '__' double underscore or end with '__' double underscore

# Mapping Operators to Functions = https://docs.python.org/3/library/operator.html#mapping-operators-to-functions

class Employee:
    no_of_leaves = 8

    # It is Dunder methods and dunder init is a special method bcoz it is constructor
    # __init__ is constructor
    def __init__(self, name, salary, role):  # self will get object name 'mayank' or 'subodh'
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"Name is {self.name}. Age is {self.salary}. Role is {self.role}"

    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    # It is Dunder add and dunder add is a special method and it help for operator overloading
    def __add__(self, other):
        return self.salary + other.salary

    # It is Dunder truediv
    def __truediv__(self, other):
        return self.salary / other.salary

    # It is Dunder repr
    def __repr__(self):
        return f"Employee('{self.name}', '{self.salary}', '{self.role}')"

    # It is Dunder str
    def __str__(self):
        return f"Name is {self.name}. Age is {self.salary}. Role is {self.role}"

mayank = Employee("Mayank", 25000, "Programmer")
rohan = Employee("Rohan", 2500, "Cleaner")
print(mayank + rohan) # if we add two objects then behind the scenes it will run dunder add method
print(mayank / rohan) # if we divide two objects then behind the scenes it will run dunder truediv method
print(mayank) # by default it finds dunder str but if it didn't find then it will run dunder repr method
print(repr(mayank)) # it will run dunder repr method
print(str(mayank)) # it will run dunder str method

'''Suppose we don't have only dunder repr then no need to specify repr in print it goes directly to dunder repr but
if we have both dunder str and dunder repr then it will by default goes to dunder str and no need to mention str in
print and if we have both dunder str and dunder repr then we want to go dunder repr then you have to mention repr in print
and if we have only dunder repr but we mention str there also it goes to dunder repr'''