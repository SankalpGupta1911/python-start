# Single inheritance

'''class Employee:
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

class Programmer(Employee): #inherit Employee class

    def printprog(self):
        return f"Name is {self.name}. Salary is {self.salary}. Age is {self.age}."

mayank = Employee("Mayank", 25000, 23) #if we provide argument to a class name then it will handle by __init__
subodh = Employee("Subodh", 40000, 30) #if we provide argument to a class name then it will handle by __init__

shubham = Programmer("Shubham", 55000, 25)
karan = Programmer("Karan", 75000, 21)
print(shubham.printprog())
print(karan.printprog())
amit = Programmer.from_string("Amit-740000-40") #inherit 'from_string' into 'Programmer'
print(amit.printprog())'''




# we inheritate but we add one more argument. for this we have to create another '__init__'
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

class Programmer(Employee): #inherit Employee class
    no_of_holiday = 20

    # we will tell you later correct way for this and for not write same code('name','salary','age') again. with help of 'super'
    def __init__(self, name, salary, age, language):
        self.name = name
        self.salary = salary
        self.age = age
        self.language = language

    def printprog(self):
        return f"Name is {self.name}. Salary is {self.salary}. Age is {self.age}. Lang is {self.language}  "

mayank = Employee("Mayank", 25000, 23) #if we provide argument to a class name then it will handle by __init__
subodh = Employee("Subodh", 40000, 30) #if we provide argument to a class name then it will handle by __init__

shubham = Programmer("Shubham", 55000, 25, ["Python", "PHP"])
karan = Programmer("Karan", 75000, 21, ["Python", "React"])
print(shubham.printprog())
print(karan.printprog())
print(karan.no_of_holiday)