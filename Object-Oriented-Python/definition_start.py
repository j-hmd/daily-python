# Difining classes in python

# This is a correct class implementation that does nothing
class Empty(): # We don't necessarily need to use the (), only if we're looking at inheritance
    pass

e1 = Empty()
print (e1)

# Book Class
class Book:
    # I think here we're "overriding the __init__ method, that is a special method in python."
    def __init__(self, title):  # Initializer function. Not quite the "constructor", because the object has already been constructed at this point.
        self.title = title  # Create an attribute named title, and pass it "title"

# Instantiating the book class
b1 = Book("War and peace") # We're only passig one argument, because on calls to objects, the first argument will always be the object itself.

# Looking at the book class:
print (b1)
print (b1.title)
