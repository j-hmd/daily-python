class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title 
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self):
        return f"{self.title} by {self.author} costs {self.price}"
    
    # We have to call this using the super(), otherwise we'll be stuck in a loop
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    def __setattr__(self, attrname, value):
        if attrname == "price":
            if type(value) is not float:
                raise ValueError("Error: Price must be float.")
        return super().__setattr__(attrname, value) # careful with logic, if there was an else, the value would never be returned
    
    # The getattr method is only called if the __getattribute__ fails, or if it's not defined.
    def __getattr__(self, name):
        return name + " is not present!"
    
b1 = Book("Pride and Prejudice", "Jane Austen", 34.99)
print(b1)

# Get a value error, must be a float
#b1.price = 10
print(b1.nothing)