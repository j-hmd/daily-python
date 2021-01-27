# Start with a class Book
class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price
        # Double underscore in python has a special meaning, this prevents derived classes from 
        # accessing this attriburte without name mangling
        self.__secret = "Secret attribute!"

    def setDiscount(self, discount):
        self._discount = discount  # the '_' tells others that this value is private to the class

    def getPrice(self):
        if hasattr(self, '_discount'): # hasattr also needs the paramter 'self'
            return self.price - (self.price * self._discount)
        else:
            return self.price

# Create Book object wand 
b1 = Book("War and peace", "Tolstoy", 35)
print (b1.name)

# Print the price of the book
print("Full price")
print(b1.getPrice())

# Set a discount for the book and print the new price
b1.setDiscount(0.5)
print("Discounted price:")
print(b1.getPrice())

# Can't access attribute like this:
# print(b1.__secret)
# We get: AttributeError: 'Book' object has no attribute '__secret'
print(b1._Book__secret)