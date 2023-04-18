import csv
 
#NOTE: the structure of books.csv file Book ID, Title, Author, Category, Quantity, Unit Price, Total Price

# Welcome message
print('''
******* Welcome to THE BOOKSHOP INVENTORY SYSTEM  *******
******* coded with love by Mustafa twitter@mu57f4 *******
''')
print()


# Read data
def read_data():
    books = []
    with open("books.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            books.append(row)
    return books

database = read_data()

# List data
def list_data(database):
    for book in database:
        print("Book ID:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Category:", book[3])
        print("Quantity:", book[4])
        print("Unit price:", book[5])
        print("Total price:", book[6])
        print()
    print(len(database))

# Search by title
def search_by_title(database):
    title = input("Enter title or part of it: ")
    found = False
    for book in database:
        if title in book[1]:
            print()
            print("Book ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Category:", book[3])
            print("Quantity:", book[4])
            print("Unit price:", book[5])
            print("Total price:", book[6])
            print()
            found = True
    if not found:
        print("ERROR: No books found with the given title.")

# Search by author
def search_by_author(database):
    author = input("Enter author or part of it: ")
    found = False
    for book in database:
        if author in book[2]:
            print()
            print("Book ID:", book[0])
            print("Title:", book[1])
            print("Author:", book[2])
            print("Category:", book[3])
            print("Quantity:", book[4])
            print("Unit price:", book[5])
            print("Total price:", book[6])
            print()
            found = True
    if not found:
        print("ERROR: No books found with the given author.")

# Add a new book
def add_book(books):
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    category = input("Enter category: ")
    quantity = input("Enter quantity: ")
    unit_price = input("Enter unit price: ")
    total_price = int(quantity) * int(unit_price)
    book = [book_id, title, author, category, quantity, unit_price, total_price]
    database.append(book)
    print("Successfully added new book.")
    print()

# Delete a book
def delete_book(database):
    book_id = input("Enter book ID: ")
    found = False
    for book in database:
        if book[0] == book_id:
            database.remove(book)
            found = True
    if found:
        print("Successfully deleted book.")
        print()
    else:
        print("ERROR: No books found with given ID.")
        print()

# Add to current stock of books book+1
def add_to_stock(database):
    book_id = input("Enter book Name: ")
    book_quantity = input("Enter the quantity: ")
    success = False
    for book in database:
        if book[0] == book_id:
            book[4] = int(book[4]) + int(book_quantity)
            book[6] = int(book[4]) * int(book[5])
            success = True
    if success:
        print("Successfully added to stock.")
        print()
    else:
        print("ERROR: No book found with given ID.")
        print()

# remove from the current stock of books
def remove_from_stock(database):
    book_title = input("Enter book Name: ")
    book_quantity = input("Enter the quantity: ")
    success = False
    for book in database:
        if book[0] == book_title:
            book[4] = int(book[4]) - int(book_quantity)
            book[6] = int(book[4]) * int(book[5])
            success = True
    if success:
        print("Successfully removed from stock.")
        print()
    else:
        print("ERROR: No book found with given ID.")
        print()

# show the total value of books in the database
def all_value(database):
    all_value_books = 0
    for book in database:
        all_value_books += int(book[6])
    print("The value of all books in the shop is:", all_value_books)
    print()

# Save the changes in the database
def save_changes(database):
    books_db = open('books.csv', 'w')
    with books_db:
        writer = csv.writer(books_db)
        writer.writerows(database)
    print("The Database Updated Successfully.")
    print()


while True:
    # Print the menu
    print('******************* MENU *******************')
    print('1. Read Data                               *')
    print('2. List Data                               *')
    print('3. Search by Title                         *')
    print('4. Search by Author                        *')
    print('5. Add a New Book                          *')
    print('6. Delete a Book                           *')
    print('7. Add to the Current Stock of a Book      *')
    print('8. Remove from the Current Stock of a Book *')
    print('9. Show Total Value of the Books           *')
    print('10. Save Data                              *')
    print('11. Exit the Program                       *')
    print("********************************************")
    print()

    # Prompt the user to select an option
    choice = int(input('Enter your choice: '))

    if choice == 1:
        read_data()
        database = read_data()
        print("Successfully read data from file")
        print()
    elif choice == 2:
        list_data(database)
    elif choice == 3:
        search_by_title(database)
    elif choice == 4:
        search_by_author(database)
    elif choice == 5:
        add_book(database)
    elif choice == 6:
        delete_book(database)
    elif choice == 7:
        add_to_stock(database)
    elif choice == 8:
        remove_from_stock(database)
    elif choice == 9:
        all_value(database)
    elif choice == 10:
        save_changes(database)
    elif choice == 11:
        print("Good-Bye :)")
        quit()
    else:
        print("ERROR: Invalid Choice, Please enter a valid choice.")
        print()
