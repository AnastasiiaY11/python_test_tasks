books = {
    "book1": {"title": "1984", "author": "George Orwell", "year": 1949},
    "book2": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960}
}

for book_key in books:
    book_info = books[book_key]
    print(f"Book: {book_info['title']}, Author: {book_info['author']}, Year: {book_info['year']}")
