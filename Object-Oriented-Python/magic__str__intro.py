# This is one of python's "magic" fucntions
# It reminds me of operatorX() in c++, where it's a method that is provided, but you can overload

class Book:
    def __init__ (self, name, author, price):
        super().__init__()
        self.name = name
        self.author = author
        self.price = price
    
    # Overloading the __str__ method, which is more user facing, and we can use to print objects
    def __str__(self):
        return f"{self.name} by {self.author} costs {self.price}"

    # Overloading the __repr__ method, which is more for debugging purposes for some reason?
    def __repr__(self):
        return f"name={self.name}, author={self.author}, cost={self.price}"

b1 = Book("Catcher in the rye", "JD Salinger", 35.99)
b2 = Book("Pride and Prejudice", "Jane Austen", 24.50)

# These calls use __str__
print(b1)
print(b2)

# explicit call to __str__
print(str(b1))
# explicit call to __repr__
print(b2.__repr__())
