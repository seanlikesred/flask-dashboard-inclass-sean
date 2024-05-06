#from app.db import BaseModel

#class Book(BaseModel):

#    SHEET_NAME = "books"
#    COLUMNS = ["title", "author", "year"]

#    SEEDS = [
#        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
#        {"title": "1984", "author": "George Orwell", "year": 1949},
#        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
#        {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
#        {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
#        {"title": "To the Lighthouse", "author": "Virginia Woolf", "year": 1927},
#        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
#        {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851},
#        {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
#        {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "year": 1865},
#        {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year": 1997},
#        {"title": "Harry Potter and the Chamber of Secrets", "author": "J.K. Rowling", "year": 1998},
#    ]


#if __name__ == "__main__":

#    books = Book.all()
#    print("FOUND", len(books), "BOOKS")
#    if any(books):
#        for book in books:
#            print(book.title, book.author, book.year)
#    else:
#        Book.seed()

from pprint import pprint

from app.db import BaseModel

class Book(BaseModel):

    SHEET_NAME = "books"

    COLUMNS = ["title", "author", "year", "url"]

    #titles and images come from https://www.goodreads.com/shelf/show/science-fiction

    SEEDS = [
        {
            'title': 'Dune',
            'author': 'Frank Herbert',
            'year': 1965,
            'url': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1555447414i/44767458.jpg'
        },
        {
            'title': 'Enders Game',
            'author': 'Orson Scott Card',
            'year': 1985,
            'url': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1408303130i/375802.jpg'
        },
        {
            'title': 'The Martian',
            'author': 'Andy Weir',
            'year': 2011,
            'url': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1413706054i/18007564.jpg'
        },
        {
            'title': '1984',
            'author': 'George Orwell',
            'year': 1949,
            'url': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1657781256i/61439040.jpg'
        },
        {
            'title': 'Ready Player One',
            'author': 'Ernest Cline',
            'year': 2011,
            'url': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1500930947i/9969571.jpg'
        },
        {
            'title': 'Farenheit 451',
            'author': 'Ray Bradbury',
            'year': 1953,
            'url': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1383718290i/13079982.jpg'
        },
    ]


if __name__ == "__main__":

    print("------------")
    print("EXISTING RECORDS:")
    books = Book.all()
    print("FOUND", len(books), "BOOKS:")
    if any(books):
        for book in books:
            #breakpoint()
            pprint(dict(book))
    else:
        #if input("Seed products? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Product.seed()
        print("SEEDING RECORDS...")
        Book.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    book = Book.find(1)
    print(book.title)

    print("------------")
    print("FILTERING RECORDS...")
    matches = Book.where(title="Dune")
    print(len(matches))
    book = matches[0]
    print(book.title)

    print("------------")
    print("CREATING NEW BOOK...")
    params = {
        'title': 'The Hunger Games',
        'author': 'Suzzane Collins',
        'year': 2008,
        'url': 'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1586722975i/2767052.jpg'
    }
    Book.create(params)

