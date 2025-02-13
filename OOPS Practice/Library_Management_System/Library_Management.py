#IMPORTANT MODULES
import time
import pymysql

#Class definition for class Book
class Book:
    
    def __init__(self) -> None:
        self.title = input("Enter Title: ")
        self.author = input("Enter Author: ")
        self.ISBN = input("Enter ISBN: ")
        self.status = "Available"
        self.available_copies = 0
    
        copies = input("Please enter the number of available copies: ")
        if not copies.isdigit():  # Check if input is a non-negative integer
            print("Unvalid value entered, setting available copies to 0")
            self.available_copies = 0
            raise ValueError("Error: Available copies must be a non-negative integer.")
        else: 
            self.available_copies = int(copies)  # Convert to integer after validation    
        
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"Book: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nStatus: {status}\n"

#Class definition for class Library
class Library:

    '''
    Method - Add book
    Access level - Admin only
    Description - Allows you to add a book to library
    '''
    @classmethod
    def add_book(cls):
        try:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="Vivek1465",
                database="librarydb"
            )
            cursor = conn.cursor()
            book = Book()
            query = """INSERT INTO Books (title, author, isbn, status, available_copies) 
                    VALUES (%s, %s, %s, %s, %s);"""
            values = (book.title, book.author, book.ISBN, book.status, book.available_copies)
            cursor.execute(query,values)
            conn.commit()  # Commit transaction
            print("✅ Book added successfully!")
        except pymysql.MySQLError  as err:
             print("❌ Error Occurred:", err)
        finally:
            # Close connection
            cursor.close()
            conn.close()
    
    '''
    Method - Delete book
    Access level - Admin only
    Description - Allows you to delete a book to library
    '''
    @classmethod
    def remove_book(cls):
        try:
            ISBN = input("Please enter the ISBN of the book you want to delete: ").strip()
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="Vivek1465",
                database="librarydb"
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Books WHERE isbn = %s;",(ISBN,))
            book = cursor.fetchone()
            if book:
                query = """DELETE FROM Books WHERE isbn = %s;"""
                values = (ISBN,)
                cursor.execute(query,values)
                conn.commit()  # Commit transaction
                print("✅ Book removed successfully!")
            else:
                print("❌ Book not found!")
        except pymysql.MySQLError as err:
             print("❌ Error Occurred:", err)
        finally:
            # Close connection
            cursor.close()
            conn.close()
    
    '''
    Method - Add book
    Access level - Admin and User
    Description - Allows you to search a book in library
    '''
    @classmethod
    def search_book(cls):
        try:
            conn = pymysql.connect(
                host="localhost",
                user="root",
                password="Vivek1465",
                database="librarydb"
            )
            cursor = conn.cursor()
            search_choice = int(input("Choose search criteria:\n1. Title\n2. Author\n3. ISBN\nEnter choice: "))
            if search_choice == 1:
                title = input("Enter the book title: ").strip()
                cursor.execute("SELECT * FROM Books WHERE title LIKE %s;", (f"%{title}%",))
            elif search_choice == 2:
                author = input("Enter the author's name: ").strip()
                cursor.execute("SELECT * FROM Books WHERE author LIKE %s;",(f"%{author}%",))
            elif search_choice == 3:
                ISBN = input("Enter the ISBN: ").strip()
                cursor.execute("SELECT * FROM Books WHERE isbn = %s;",(ISBN,))
            else:
                print("❌ Invalid Option Selected")
                return
            
            books = cursor.fetchall()
            if books:
                print("\n📚 Matching Books:\n" + "-"*30)
                for book in books:
                    print(f"📖 Title: {book[1]}\n👨‍💼 Author: {book[2]}\n🔢 ISBN: {book[3]}\n📌 Status: {book[4]}\n📦 Available Copies: {book[5]}\n" + "-"*30)
            else:
                print("❌ No book found matching the search criteria!")
        except pymysql.MySQLError as err:
             print("❌ Error Occurred:", err)
        finally:
            # Close connection
            cursor.close()
            conn.close()
    
    '''
    Method - Borrow book
    Access level - Admin and User
    Description - Allows a user to borrow the book. Admin can also access this function.
    '''
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
    