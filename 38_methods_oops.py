# Methods
# class Employee
'''class Employee:
    no_of_leaves = 8

    def printdetails(self): #methods implement in class
        return f"Name is {self.name}. Salary is {self.salary}. Age is {self.age} "

# two object of Employee class
mayank = Employee()
subodh = Employee()

# few intance variables of objects
mayank.name = "Mayank"
mayank.age = 23
mayank.salary = 25000
subodh.name = "Subodh"
subodh.age = 30
subodh.salary = 45000

print(mayank.printdetails()) # printdetails pass one argument and it is 'mayank'
print(subodh.printdetails()) # printdetails pass one argument and it is 'rohan' '''


# argument pass with class is work with the help of constructor
# class Employee
'''class Employee:
    no_of_leaves = 8

    # __init__ is constructor
    def __init__(self, name, salary, age): #self will get object name 'mayank' or 'subodh'
        self.name = name
        self.salary = salary
        self.age = age

mayank = Employee("Mayank", 25000, 23) #if we provide argument to a class name then it will handle by __init__
print(f"Name is {mayank.name}. Salary is {mayank.salary}. Age is {mayank.age} ")
subodh = Employee("Subodh", 40000, 30) #if we provide argument to a class name then it will handle by __init__
print(f"Name is {subodh.name}. Salary is {subodh.salary}. Age is {subodh.age} ")'''


# class methods to change class variables value
'''class Employee:
    no_of_leaves = 8

    #class method
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    # __init__ is constructor
    def __init__(self, name, salary, age): #self will get object name 'mayank' or 'subodh'
        self.name = name
        self.salary = salary
        self.age = age

mayank = Employee("Mayank", 25000, 23) #if we provide argument to a class name then it will handle by __init__
print(f"Name is {mayank.name}. Salary is {mayank.salary}. Age is {mayank.age} ")
subodh = Employee("Subodh", 40000, 30) #if we provide argument to a class name then it will handle by __init__
print(f"Name is {subodh.name}. Salary is {subodh.salary}. Age is {subodh.age} ")
print(mayank.no_of_leaves)
print(mayank.__dict__)
mayank.change_leaves(34) #access by instance name and change the value of no_of_leave
print(mayank.__dict__)
print(mayank.no_of_leaves)
print(Employee.__dict__)
Employee.change_leaves(54) #access by class name and change the value of no_of_leave
print(Employee.__dict__)
print(Employee.no_of_leaves)
print(mayank.no_of_leaves)'''

# class method used as alternative constructor and how to make instance with the class method
class Employee:
    no_of_leaves = 8

    #class method
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    # class method
    @classmethod
    def from_string(cls, str_val):
        #1st method of split and return
        # params = str_val.split("-") #it will create list of ['Rohan', '45000', '28']
        # return cls(params[0], params[1], params[2])

        #2nd method of split and return
        return cls(*str_val.split("-")) #it will also return list of ['Rohan', '45000', '28']


    # __init__ is constructor
    def __init__(self, name, salary, age): #self will get object name 'mayank' or 'subodh'
        self.name = name
        self.salary = salary
        self.age = age

mayank = Employee("Mayank", 25000, 23) #if we provide argument to a class name then it will handle by __init__
subodh = Employee("Subodh", 40000, 30) #if we provide argument to a class name then it will handle by __init__
rohan = Employee.from_string("Rohan-45000-28") # create instance with string
print(f"Name is {rohan.name}. Salary is {rohan.salary}. Age is {rohan.age} ")
print(rohan.no_of_leaves) #it is same instance as another instances
# print(f"Name is {mayank.name}. Salary is {mayank.salary}. Age is {mayank.age} ")
# print(f"Name is {subodh.name}. Salary is {subodh.salary}. Age is {subodh.age} ")
