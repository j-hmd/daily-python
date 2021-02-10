# Data classes make the class definition more concise since python 3.7
# it automates the creation of __init__ with the attributes passed to the
# creation of the object.
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

b1 = Book("A Mao e a Luva", "Machado de Assis", 356, 29.99)
b2 = Book("Dom Casmurro", "Machado de Assis", 230, 24.50)
b3 = Book("Capitaes da Areia", "Jorge Amado", 178, 14.50)

# The data class also provides implementations for the __repr__ and __eq__ magic functions
print(b1.title)
print(b2.author)

print(b1 == b2)