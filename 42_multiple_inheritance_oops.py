# Multiple inheritance

class Employee:
    no_of_leaves = 8
    testing = 7
    #static method
    @staticmethod
    def printgood(string_val):
        return "This is good " + string_val

    def printdetails(self):
        return f"Name is {self.name}. Age is {self.salary}. Role is {self.role}"

    # __init__ is constructor
    def __init__(self, name, salary, role):  # self will get object name 'mayank' or 'subodh'
        self.name = name
        self.salary = salary
        self.role = role

    # class method
    @classmethod
    def from_string(cls, str_val):
        return cls(*str_val.split("-"))  # it will also return list of ['Rohan', '45000', '28']

class Player:
    no_of_games = 4
    testing = 9
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name is {self.name}. Game is {self.game}."

#order of argument is important 'Coolprogrammer' construtor(__init__) use 'Employee' constructor(__init__) because it is 1st argument
class Coolprogrammer(Employee, Player):
    pass

mayank = Employee("Mayank", 25000, "Leader") #if we provide argument to a class name then it will handle by __init__
subodh = Employee("Subodh", 40000, "Instructor") #if we provide argument to a class name then it will handle by __init__

shubham = Player("Shubham", ["Cricket, TT"])
print(shubham.printdetails())
karan = Coolprogrammer("Karan", 45000, "Cool Programmer")
print(karan.printdetails()) # it print 'printdetails()' from 'Employee' class because in 'Coolprogrammer' we wrote 1st argument is 'Employee'
print(karan.testing) # it print 'testing' from 'Employee' class because in 'Coolprogrammer' we wrote 1st argument is 'Employee'