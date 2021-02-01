# The commonalities between the classes Book, Magazine and Newspaper hint at the 
# need for better organized code structure, which reduces repetition between the 
# attributes of these classes.
# The 'design pattern' in this case seems a little odd to me, but this is just to 
# demonstrate the syntax of python inheritance.

class Publication:
    def __init__(self, title, price):
        self.title = title 
        self.price = price

class Periodical(Publication):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period

class Book(Publication):
    def __init__(self, title, price, pages, author):
        super().__init__(title, price)
        self.pages = pages
        self.author = author

class Magazine(Periodical):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price, publisher, period)

class Newspaper(Periodical):
    def __init__(self, title, price, publisher, period):
        super().__init__(title, price, publisher, period)


# Including inheritance in the design would not change how the classes
# are instantiated here.
b1 = Book("Pride and Prejudice", 16.99, 255, "Jane Austen")
m1 = Magazine("The New Yorker", 9.99, "The new yorker?", "Weekly")
n1 = Newspaper("The Atlantic", 3.50, "no idea", "Daily" )

print(b1.author)
print(m1.title + " costs", m1.price)
print(n1.publisher + " " + n1.period)
