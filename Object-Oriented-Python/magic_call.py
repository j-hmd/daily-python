# Calling an object as if it were a funciton

class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

b1 = Book("A mao e a luva", "Machado de Assis", 29.99)
print(b1)
# Here we can call the object, as if it were a funciton to modify its attributes
b1("Dom Casmurro", "Machado de Assis", 25.50)
print(b1)