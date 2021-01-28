class Book:
    def __init__(self, title):
        self.title = title

class Magazine:
    def __init__(self, title):
        self.title = title

b1 = Book("War and peace")
m1 = Magazine("People")

# We can check the type of python objects with the type()
print("Compare the type of a Book instance, and the type of a Magazine instance")
print(type(b1) == type(m1))

# But we can also check agains the class itself, using the isinstance
# All python objects derinve from the 'object' class in python
print("Compare the instance of book, with the class Book")
print(isinstance(b1, Book))
