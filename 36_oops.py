# object oriented programming

# Classes - Template
# Object - Instance of the Class
# oops use DRY(Do not repeat yourself) concept

# class student
class Student:
    pass #blank template

# two object of Student class
mayank = Student()
subodh = Student()

# few intance variables of objects
mayank.age = 23
mayank.salary = 25000
subodh.age = 30
subodh.list = ['mobile', 'charger', 'bike']

print(mayank.age, subodh.list)


# double underscore means these all variables is private
# it means you can't access there values directly so we need setters and getters
'''class Employee:
    __name = None
    __id = 0
    __salary = 0

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

mayank = Employee()
mayank.set_name("Mayank")
print(mayank.get_name())
mayank.set_id(40)
print(mayank.get_id())
mayank.set_salary(80000)
print(mayank.get_salary())'''

#same work with the help of constructor
class Employee:
    __name = None
    __id = 0
    __salary = 0

    def __init__(self, name, id, salary):
        self.__name = name
        self.__id = id
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_salary(self):
        return self.__salary

mayank = Employee("Mayank", 40, 800000)
print(mayank.get_name())
print(mayank.get_id())
print(mayank.get_salary())