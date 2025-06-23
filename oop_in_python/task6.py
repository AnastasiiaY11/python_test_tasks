class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        
    def __str__(self):
        return f"{self.title} by {self.author} (Published: {self.year_published})"

my_book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year_published=1925)

print(my_book)

another_book = Book("1984", "George Orwell", 1949)
print(another_book)
