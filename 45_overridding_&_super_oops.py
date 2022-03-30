# overridding

'''------Start overridding class variable-----'''

'''class A:
    class_var1 = "I am in class A"

    def __init__(self):
        self.var1 = "I'm inside class A's constructor"
        self.class_var1 = "Instance variable in class A"

class B(A):
    class_var1 = "I am in class B"

a = A()
b = B()
print(b.class_var1) #it will print instance variable of class A
# Because first it goes and search instance variable in class B but it didn't find any instance variable in class B
# then it goes to class A and search instance variable in class A and got instance variable into class A'''



'''class A:
    class_var1 = "I am in class A"

    def __init__(self):
        self.var1 = "I'm inside class A's constructor"
        # self.class_var1 = "Instance variable in class A"

class B(A):
    class_var1 = "I am in class B"

a = A()
b = B()
print(b.class_var1) #it will print class variable of class B
# Because first it goes and search instance variable in class B but it didn't find any instance variable in class B
# then it goes and search instance variable in class A but it didn't find any instance variable in class A then it goes
# to class B and search class variable and got class variable into class B'''


'''class A:
    class_var1 = "I am in class A"

    def __init__(self):
        self.var1 = "I'm inside class A's constructor"
        # self.class_var1 = "Instance variable in class A"

class B(A):
    pass
    # class_var1 = "I am in class B"

a = A()
b = B()
print(b.class_var1) #it will print class variable of class B
# Because first it goes and search instance variable in class B but it didn't find any instance variable in class B
# then it goes and search instance variable in class A but it didn't find any instance variable in class A then it goes
# to class B and search class variable but it didn't find any class variable in class B then it goes
# to class A and search class variable and got class variable into class A'''

'''------End overridding class variable-----'''


'''------Start overridding method or constructor and access old method or constructor with the help of 'super()'-----'''
'''class A:
    class_var1 = "I am in class A"

    def __init__(self):
        self.var1 = "I'm inside class A's constructor"
        self.class_var1 = "Instance variable in class A"

class B(A):
    class_var1 = "I am in class B"
    def __init__(self):
        self.var1 = "I'm inside class B's constructor"
        self.class_var1 = "Instance variable in class B"

a = A()
b = B()
print(b.class_var1) #it will print instance variable of class B'''

'''class A:
    class_var1 = "I am in class A"

    def __init__(self):
        self.var1 = "I'm inside class A's constructor"
        self.class_var1 = "Instance variable in class A"

class B(A):
    class_var1 = "I am in class B"
    def __init__(self):
        self.var1 = "I'm inside class B's constructor"
        # self.class_var1 = "Instance variable in class B"

a = A()
b = B()
print(b.class_var1) #it will print class variable of class B
# because our class A constructor is override with class B constructor and we can't use constructor of class A without super()
# so that's bcoz it didn't find instance variable in class A and it prints class variable of class B'''


'''# Suppose we want to access our old constructor bcoz we have some instance variable in old constructor which is not in new constructor
# faulty program to understand we can't access 'spacial' instance variable with this program
class A:
    class_var1 = "I am in class A"

    def __init__(self):
        self.var1 = "I'm inside class A's constructor"
        self.class_var1 = "Instance variable in class A"
        self.special = "Instance variable spacial in class A"

class B(A):
    class_var1 = "I am in class B"
    def __init__(self):
        self.var1 = "I'm inside class B's constructor"
        self.class_var1 = "Instance variable in class B"

a = A()
b = B()
print(b.special) #print error - 'B' object has no attribute 'special' '''


'''# this program solve above problem
class A:
    class_var1 = "I am in class A"

    def __init__(self):
        self.var1 = "I'm inside class A's constructor"
        self.class_var1 = "Instance variable in class A"
        self.special = "Instance variable spacial in class A"

class B(A):
    class_var1 = "I am in class B"
    def __init__(self):
        super().__init__() # it access class A constructor
        self.var1 = "I'm inside class B's constructor" #override of class A instance variable
        self.class_var1 = "Instance variable in class B" #override of class A instance variable

a = A()
b = B()
print(b.special) #print instance variable of class A constructor
print(b.class_var1) #print instance variable of class B constructor bcoz first we access old constructor with super()
# but after that new constructor instance variable override that because it written after super()'''


# for access all instance variable of old constructor and print that we have to change the position of super()
class A:
    class_var1 = "I am in class A"
    variable1 = "I'm class variable of class A"

    def __init__(self):
        self.var1 = "I'm inside class A's constructor"
        self.class_var1 = "Instance variable in class A"
        self.special = "Instance variable spacial in class A"

class B(A):
    class_var1 = "I am in class B"
    variable1 = "I'm class variable of class B"
    def __init__(self):
        self.var1 = "I'm inside class B's constructor"
        self.class_var1 = "Instance variable in class B"
        super().__init__()  # it access class A constructor and also override of class B instance variable
        print(super().class_var1) # it will access and print class variable 'class_var1' of class A
        print(super().variable1) # it will access and print class variable 'variable1' of class A

a = A()
b = B()
print(b.special) #print instance variable of class A constructor
print(b.class_var1) #print instance variable of class A constructor bcoz first we written instance variable of class B and then
# access old(class A) constructor with super()