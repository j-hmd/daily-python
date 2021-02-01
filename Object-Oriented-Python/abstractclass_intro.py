# Abstract classes are a way to tell the user of the class that 
# this class is only a blue print, and we have contraints: can't instantiate the abstract class
# and there are certain methods that the concrete classes have to implement

# which states for abstract base class
# I wonder if there are other ways to implement abstract base classes in python
from abc import ABC, abstractmethod

class shape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod #enforces that other classes have to implement this method
    def GetArea(self):
        pass

class square(shape):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def GetArea(self):
        return self.side * self.side # Don't forget that we have to put the self.attribute!

class circle(shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def GetArea(self):
        return 3.14 * (self.radius  ** 2)

# This will fail now that we have an abstract base class
# s1 = shape()

s1 = square(3)
c1 = circle(10)

print(s1.GetArea())
print(c1.GetArea())

