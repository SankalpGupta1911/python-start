
'''class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

mayank = Employee("Mayank", "Kumar")
print(mayank.explain())
print(mayank.email)
# Suppose fname have changed and we have to create new email
mayank.fname = "Karan"
print(mayank.email) # it will print old email with old fname. for this we have to create setter'''

'''solve fname change problem'''
'''class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

mayank = Employee("Mayank", "Kumar")
print(mayank.explain())
print(mayank.email())
# Suppose fname have changed and we have to create new email
mayank.fname = "Karan"
print(mayank.email()) # it will print new email with new fname.'''


'''i don't want to work email as a function. encapsulation will hide any class implementation'''
'''#use decorators
class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property #property decorator
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

mayank = Employee("Mayank", "Kumar")
print(mayank.explain())
print(mayank.email)
# Suppose fname have changed and we have to create new email
mayank.fname = "Karan"
print(mayank.email) # it will print new email with new fname.'''

'''Suppose we want change email and also change the attributes(fname, lname) of email with only change in email'''
'''class Employee:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property #property decorator
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter # setter for set attribute
    def email(self, string1):
        print("Setting now....")
        names = string1.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
        return f"{self.fname}.{self.lname}@gmail.com"

mayank = Employee("Mayank", "Kumar")
print(mayank.explain())
print(mayank.email)
# Suppose fname have changed and we have to create new email
mayank.fname = "Karan"
print(mayank.email) # it will print new email with new fname.
print(mayank.fname)
print(mayank.lname)
mayank.email = "Subodh.Gupta@gmail.com" #change email, fname, lname
print(mayank.fname)
print(mayank.lname)
print(mayank.email)'''


'''suppose we want to delete email name attribute with the help of deleter'''
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

mayank = Employee("Mayank", "Kumar")
print(mayank.explain())
print(mayank.email)
# Suppose fname have changed and we have to create new email
mayank.fname = "Karan"
print(mayank.email) # it will print new email with new fname.
print(mayank.fname)
print(mayank.lname)
mayank.email = "Subodh.Gupta@gmail.com" #change email, fname, lname
print(mayank.fname)
print(mayank.lname)
print(mayank.email)

del mayank.email #it finds deleter if we don't have deleter then it will throw error else it will delete attribute of email
print(mayank.fname)
print(mayank.lname)
print(mayank.email)