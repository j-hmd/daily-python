# We can use composition to represent a "has a" relationship thta
# breaks down a monolithic class, into smaller ones, with the appropriate 
# distribution of functionality

class Book:
    def __init__(self, name, author=None):
        self.name = name
        self.author = author
    
    # Book has chapters
    chapters = []

    # Method to add chapters
    def AddChapter(self, chapter):
        self.chapters.append(chapter)
    
    # Method: print book total pages
    def GetTotalPages(self):
        total_pages = 0
        for ch in self.chapters:
            total_pages += ch.pagecount
        return total_pages

class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # Magic method?
    def __str__(self):
        return f"{self.fname} {self.lname}"

class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount

b1_author = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", b1_author)

print(b1.author)

b1.AddChapter(Chapter("Chapter 1", 170))
b1.AddChapter(Chapter("Chapter 2", 49))

print(b1.name)
print(b1.GetTotalPages())