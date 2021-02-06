# The python data model allows us to override a lot of other methods
# in order to compare the objects to one another.
# For example, the __eq__ (equality), __ge___ (>=), __lt__ (<)

class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def __eq__(self, lhs):
        if not isinstance(lhs, Book):
            raise ValueError("Can't perform comaparison on non book objects.")
        return (self.name == lhs.name and \
            self.author == lhs.author and \
            self.price == lhs.price)

    def __ge__(self, lhs):
        return self.price >= lhs.price
    
    def __lt__(self, lhs):
        return self.price < lhs.price

b1 = Book("Catcher in the rye", "JD Salinger", 32.99)
b2 = Book("Pride and prejudice", "Jane Austen", 24.50)
b3 = Book("Catcher in the rye", "JD Salinger", 32.99)
b4 = Book("War and Peace", "Leo Tolstoy", 35.99)

# Before the overriding of the equality operator, this would evaluate to false,
# because python comapres with the instance in memory, and not the attributes
print(b1==b3)
print(b2>b3)
print(b1<b4)

# Because our objects can now be compared to each other, we can sort them!
# Sorting them from smallest to biggest
books = [b1, b2, b3, b4]
books.sort()
print([book.name for book in books])
