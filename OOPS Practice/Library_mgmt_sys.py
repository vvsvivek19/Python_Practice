class library:
    def __init__(self):
        self.books = []
        self.no_of_books = None
    
    def add_book(self):
        name = input("Enter Book Name-> ")
        if isinstance(name,str):
            self.books.append(name)
        else:
            print("Book name should be string")
    
    def get_num_of_books(self):
        self.no_of_books = len(self.books)
        print("Number of books are:",self.no_of_books)

obj = library()
obj.add_book()
obj.add_book()
obj.add_book()
obj.add_book()
obj.add_book()
obj.get_num_of_books()
    