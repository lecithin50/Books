class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Reset file pointer to beginning
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            print("Book:", book_info[0])
            print("Author:", book_info[1])
            print("Release Date:", book_info[2])
            print("Number of Pages:", book_info[3])
            print()

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter book title to remove: ")
        self.file.seek(0)  # Reset file pointer to beginning
        books = self.file.readlines()
        updated_books = [book for book in books if title not in book]
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        print("Book removed successfully.")

    def search_book(self):
        keyword = input("Enter book title or author to search: ")
        self.file.seek(0)  # Reset file pointer to beginning
        books = self.file.readlines()
        found_books = [book.strip() for book in books if keyword in book]
        if found_books:
            print("Found Books:")
            for book in found_books:
                print(book)
        else:
            print("No books found matching the search criteria.")

    def update_book(self):
        title = input("Enter book title to update: ")
        self.file.seek(0)  # Reset file pointer to beginning
        books = self.file.readlines()
        updated_books = []
        for book in books:
            if title in book:
                new_author = input("Enter new author (press enter to keep current): ")
                new_release_date = input("Enter new release date (press enter to keep current): ")
                new_num_pages = input("Enter new number of pages (press enter to keep current): ")
                book_info = book.strip().split(',')
                if new_author:
                    book_info[1] = new_author
                if new_release_date:
                    book_info[2] = new_release_date
                if new_num_pages:
                    book_info[3] = new_num_pages
                book = ','.join(book_info) + '\n'
            updated_books.append(book)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        print("Book updated successfully.")

    def count_books(self):
        self.file.seek(0)  # Reset file pointer to beginning
        books = self.file.readlines()
        print("Total number of books:", len(books))

    def sort_books(self, by='title'):
        self.file.seek(0)  # Reset file pointer to beginning
        books = [book.strip().split(',') for book in self.file.readlines()]
        if by == 'title':
            sorted_books = sorted(books, key=lambda x: x[0])
        elif by == 'author':
            sorted_books = sorted(books, key=lambda x: x[1])
        else:
            print("Invalid sorting option. Sorting by title by default.")
            sorted_books = sorted(books, key=lambda x: x[0])
        for book in sorted_books:
            print("Book:", book[0])
            print("Author:", book[1])
            print("Release Date:", book[2])
            print("Number of Pages:", book[3])
            print()

# Create an object named “lib” with “Library” class
lib = Library()

# Create a menu to interact with the “lib” object
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Search Book")
    print("5) Update Book")
    print("6) Count Books")
    print("7) Sort Books")
    print("q) Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.search_book()
    elif choice == "5":
        lib.update_book()
    elif choice == "6":
        lib.count_books()
    elif choice == "7":
        sorting_option = input("Enter sorting option (title/author): ")
        lib.sort_books(sorting_option.lower())
    elif choice == "q":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 7.")
