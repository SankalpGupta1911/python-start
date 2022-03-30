# difference between class variables and instance variables
# class Employee
class Employee:
    no_of_leaves = 8
    pass #blank template

# two object of Employee class
mayank = Employee()
subodh = Employee()

# few intance variables of objects
mayank.age = 23
mayank.salary = 25000
subodh.age = 30
subodh.list = ['mobile', 'charger', 'bike']

# 'no_of_leaves' is class variable
print(mayank.no_of_leaves) #class variable access with the help 'mayank'
print(Employee.no_of_leaves) #class variable access with the help of class 'Employee'
'''we cant change the value of class variable only with the help of class'''
Employee.no_of_leaves = 10
print(Employee.no_of_leaves)
print(mayank.no_of_leaves)
'''instance variable can't change the value of class variable and if we try to change the
value from instance variable then it will create their own variable'''
print(mayank.__dict__) #print dictionary of mayank
mayank.no_of_leaves = 20 # it creates new instance variable
print(mayank.__dict__) #again print dictionary of mayank
print(Employee.no_of_leaves)
print(mayank.no_of_leaves)
