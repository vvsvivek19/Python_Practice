import mysql.connector
#Class definition for class Book
class Book:
    
    def __init__(self) -> None:
        self.title = input("Enter Title: ")
        self.author = input("Enter Author: ")
        self.ISBN = input("Enter ISBN: ")
        self.status = "Available"
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nStatus: {status}\n"

#Class definition for class Library
class Library:
    books = []
    
    @classmethod
    def add_book(cls):
        book = Book()
        cls.books.append(book)
        print("Book added successfully")
    
    @classmethod
    def remove_book(cls):
        isbn = input("Enter ISBN of the book to remove: ").strip()
        for book in cls.books:
            if book.ISBN == isbn:
                cls.books.remove(book)
                print("Book removed successfully")
                return
        print("Book not found!\n")
    
    @classmethod
    def search_book(cls):
        title = input("Enter title of the book to search: ").strip()
        for book in cls.books:
            if book.title == title.lower():
                print("Book found, below are the details")
                print(book)
                return
        print("Book not found!\n")
    
    @classmethod
    def borrow_book(isbn: str,cls):
        isbn = input("Enter ISBN of the book to borrow: ").strip()
        for book in cls.books:
            if book.ISBN == isbn:
                if book.is_borrowed:
                    print("Book is already borrowed!\n")
                else:
                    book.is_borrowed = True
                    print("Book borrowed successfully!\n")
                return
        print("Book not found!\n")

    
    @classmethod
    def return_book(isbn: str,cls):
        isbn = input("Enter ISBN of the book to return: ").strip()
        for book in cls.books:
            if book.ISBN == isbn:
                if not book.is_borrowed:
                    print("This book was not borrowed!\n")
                else:
                    book.is_borrowed = False
                    print("Book returned successfully!\n")
                return
        print("Book not found!\n")
    
    @classmethod
    def display_books(cls):
        if not cls.books:
            print("No books available in the library.\n")
            return
        print("\nLibrary Collection:")
        for book in cls.books:
            print(book)

while True:
    time.sleep(0.1)
    print("****************************************************")
    print("           Welcome to Central Library")
    print("*****************************************************")
    print("Please choose from below")
    time.sleep(0.1)
    print("1. Add Book")
    time.sleep(0.1)
    print("2. Remove Book")
    time.sleep(0.1)
    print("3. Search Book")
    time.sleep(0.1)
    print("4. Borrow Book")
    time.sleep(0.1)
    print("5. Return Book")
    time.sleep(0.1)
    print("6. Display Book")
    time.sleep(0.1)
    print("7. Exit")
    try:
        choice = int(input("Please Enter the choice from 1 to 7: "))
        if choice >=1 and choice <=7:
            pass
        else:
            print("Invalid input! Please enter a number between 1 and 7.")
            continue    
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 7.")
        continue

    if choice == 1:
        Library.add_book()
    elif choice == 2:
        Library.remove_book()
    elif choice == 3:
        Library.search_book()
    elif choice == 4:
        Library.borrow_book()
    elif choice == 5:
        Library.return_book()
    elif choice == 6:
        Library.display_books()
    elif choice == 7:
        print("Knowledge is power....")
        print("Please visit our library again")
        break
    