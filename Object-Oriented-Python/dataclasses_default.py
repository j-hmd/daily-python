# Dataclasses also provide more flexibility to initialize the values of the class
# with __post_init__ and the default, and field fucntions

from dataclasses import dataclass, field
from random import randrange

def random_price():
    return randrange(2, 7)

@dataclass
class Beverage:
    # default values. If one of the values doesn't have a default it should come first
    name: str = 'unknown'
    # if we need more flexibility with the value, we can use the field method
    temp: str = field(default = 'boiling hot')
    # and in the field method, the default_factory is a callable object to provide even more freedom
    price: float = field(default_factory=random_price)

    # the post init method allows you to add attributes that rely on other attributes and have more flexibility in the dataclass
    def __post_init__(self):
        self.description = f'{self.name} is {self.temp}'

b1 = Beverage()
print(b1.name)

b2 = Beverage('coffee')
print(b2.name)
print(b2.price)




