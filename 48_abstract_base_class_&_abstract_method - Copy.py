
# in this we ordered the program that every class must have printarea()
# 1st way
# from abc import ABCMeta, abstractmethod
# class Shape(metaclass=ABCMeta):

# 2nd way(only above 3.4 python version)- we just have to change two lines and remaining program same
from abc import ABC, abstractmethod
class Shape(ABC):

    @abstractmethod # it is used for telling that 'printarea' method must have in every class
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())
# tryobj = Shape() #it will throw error bcoz you can't create object of abstract base class