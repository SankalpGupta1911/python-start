'''B inheritate A
C inheritate A
D inheritate B,C'''

'''class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

a=A()
b=B()
c=C()
d=D()
d.met() #return class A method'''

'''class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    pass

class D(B, C):
   pass

a=A()
b=B()
c=C()
d=D()
d.met() #return class B method'''

'''class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(B, C):
   pass

a=A()
b=B()
c=C()
d=D()
d.met() #it is also return class B method because class D have inheritate first class B then class C'''


class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(B, C):
    def met(self):
        print("This is a method from class D")

a=A()
b=B()
c=C()
d=D()
d.met() #return class D method