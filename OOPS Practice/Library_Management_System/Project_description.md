📌 Key Features to Implement
We can break the features into core features (required) and additional features (enhancements for later).

1️⃣ Core Features (Essential for MySQL Integration)

✅ Database Connection & Setup
- Connect Python to MySQL using mysql-connector-python or SQLAlchemy.
- Create a database (LibraryDB) and required tables (Books, BorrowedBooks, Users).

✅ Book Management
- Add books (store title, author, ISBN, status). --> Done
- Remove books (delete from database by ISBN). --> Done
- Search books (by title, author, or ISBN). --> Done
- Display available books.
- Update book details (e.g., changing the author or title).

✅ Borrow & Return System
Borrow a book (mark as borrowed, store user details).
- In this step, you will implement the functionality to borrow a book, which involves:
    ✅ Checking if the user is new or already exists. If new then register them and then move borrowing
    ✅ Prevent duplicate borrowing (a book can’t be borrowed twice until returned).
    ✅ Checking if the book exists in the library.
    ✅ Ensuring there are available copies to borrow.
    ✅ Updating the Books table (reducing available copies).
    ✅ Adding an entry in the BorrowedBooks table.
- Return a book (update availability status).
 Show borrowed books (list books currently borrowed).

✅ User Management (Basic)
- Users should enter their name before borrowing a book.
- Store user details in a separate Users table (optional).
- Allow users to see their borrowing history.

2️⃣ Additional Features (Future Enhancements)
🚀 Advanced User System
- Register & login functionality for users.
- Admin & normal users (admin can add/remove books, normal users can only borrow/return).

🚀 Book Reservation System
- Users can reserve books and get notified when available.

🚀 Fine Calculation System
- If a book is not returned within X days, calculate fine.

🚀 Detailed Book Info
- Add book category, published year, total copies.

🚀 Logs & Reports
- Keep logs of all transactions (who borrowed what & when).
- Generate reports (most borrowed books, active users).

💡 How to Proceed?
1️⃣ Step 1 – Setup MySQL Database & Tables
2️⃣ Step 2 – Implement Add, Remove, Search, Display using MySQL
3️⃣ Step 3 – Implement Borrow & Return using MySQL
4️⃣ Step 4 – Enhance with User Management & Extra Features