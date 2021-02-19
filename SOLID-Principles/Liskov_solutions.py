# To adhere to the Liskov substitution principle, we might need to rethink the 
# design of our classes, OR we might need to refactor them.

# Thinking about the Shoe and Deck classes that are somewhat related
# the shoe class has a method shuffle_burn

class Deck(list):
    pass

class Shoe(Deck):
    def shuffle_burn(self, penetration=0.25):
        # implementation of the shuffle burn
        pass

# We see that because Shoe has this method that the parent class doesn't,
# they are not exactly peers, and we couldn't use them interchangeably
# The questions we could ask is: is the distinction necessary?
# Could we move up the distinction to the super class?

# Refactoring
# One way, would be to separate shuffle, which is common to both the deck and the shoe
# This way we correctly extend the class.
class Deck1(list):
    def shuffle(self):
        pass

class Shoe1(Deck1):
    def burn(self):
        pass

# Rethinking
# Should the method shuffle_burn be separate at all?
# we could put that in the __init__ method of Shoe
class Shoe2(Deck):
    def __init__(self, *args):
        # perform burn
        pass
