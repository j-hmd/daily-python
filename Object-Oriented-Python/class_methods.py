class Book:
    # Class variable
    BOOK_TYPES = ("NOVEL", "BIOGRAPHY")
    
    def __init__(self, title, bookType):
        self.title = title
        if not bookType in Book.BOOK_TYPES: # Have to specify here that we're accessing the class' variable!
            raise ValueError(f"{bookType} is not a valid book type") # Seems like we use 'f' to be able to access the parameter bookType...
        else:
            self.bookType = bookType

    # Example of istance method, which is applied to an instance of 
    # that class
    def GetTitle(self):
        return self.title
    
    # We could create an class method, that is applicable
    # to the whole class, usually denoted in CAPS
    @classmethod
    def GetBookTypes(cls):
        return cls.BOOK_TYPES

    # Private variable to the class
    __book_list = None # Need more info on what this means in python

    # Static methods function like global functions, and could be used
    # to implement a singleton pattern for example.
    # It's a good way no namespace the otherwise global method.
    @staticmethod
    def GetBookList():
        if Book.__book_list == None:
            Book.__book_list = []
        
        return Book.__book_list
        

# Class methods are accessible via the class itself and not an instance of the class
print("Books: ", Book.GetBookTypes())

b1 = Book("War and Peace", "NOVEL")
b2 = Book("Steve Jobs", "BIOGRAPHY")
print(b1.GetTitle)

sBookList = Book.GetBookList()
sBookList.append(b1)
sBookList.append(b2)
print(sBookList[0].title, "and", sBookList[1].title)


