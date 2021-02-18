# The liskov substitution principle says that we should be able to 
# use any subclass as its parent class without needing to modify behavior
# the choice of the implementation can be done at runtime

class Shuffler:
    @staticmethod # Allows to use the method without having to have an instance of the object
    def shuffle(deck):
        pass

class ShufflerRandom(Shuffler):
    @staticmethod
    def shuffle(deck):
        random.shuffle(deck)

class ShuffleReverse(Shuffler):
    @staticmethod
    def shuffle(deck):
        # Do some logic to reverse the list
        pass

# Then at runtime we don't have to worry about which one implementation to use
class Option:
    def __init__(self, s):
        self.shuffler = s

option = Option('s')

if option.shuffler == 's':
    shuffler = ShuffleReverse()
else:
    shuffler = ShufflerRandom()
