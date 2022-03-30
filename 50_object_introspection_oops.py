class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property #property decorator
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter # setter for set attribute
    def email(self, string1):
        print("Setting now....")
        names = string1.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.deleter
    def email(self):
        self.fname = None #in oops we never delete we just use 'None'
        self.lname = None #in oops we never delete we just use 'None'

skillf = Employee("Skill", "F")
print(skillf.email)

print(type("This is string"))
print(id("This is string"))
print(id("This that"))
# o = "This is string"
# print(dir(o)) #if we use dir than it will tell how many things we can use
# print(dir(skillf)) #if we use dir than it will tell how many things we can use.. in this our email, ecplain, fname, lname is also added

import inspect
print(inspect.getmembers(skillf)) #all attributes of skillf