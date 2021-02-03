# Python doesn't have built in support for interfaces, but it can provide that functionality by having
# abstract methods and multiple inheritance

from abc import ABC, abstractmethod

class JSONify(ABC): # don't forget to add this inheritance from ABS
    @abstractmethod
    def ToJson(self):
        pass

class GraphicShape(ABC): 
    def __init__(self):
        super().__init__()

    @abstractmethod
    def GetArea(self): 
        pass

# We can add to the square class the functionality of JSONify
# through the abstractmethod implementation.
class Square(GraphicShape, JSONify):
    def __init__(self, side):
        super().__init__()
        self.side = side
    
    def GetArea(self):
        return  self.side ** 2

    def ToJson(self):
        return f"{{ \"square\" : {str(self.GetArea())} }}" # This is crazy useful way of making strings?

s1 = Square(3)
print(s1.GetArea())
print(s1.ToJson())