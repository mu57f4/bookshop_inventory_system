## THE BOOKSHOP INVENTORY SYSTEM

A simple Python script that simulates an inventory system for a bookshop.

### Features
- Read data from a CSV file (`books.csv`) that contains book information including Book ID, Title, Author, Category, Quantity, Unit Price, and Total Price.
- List all the books in the inventory with their details.
- Search for books by title, displaying all matching results.
- Search for books by author, displaying all matching results.
- Add a new book to the inventory, prompting the user to enter book details.
- Delete a book from the inventory by Book ID.
- Add to the current stock of a book, updating the quantity and total price.
- Remove from the current stock of a book, updating the quantity and total price.
- Calculate the total value of all books in the shop.
- Save changes to the inventory back to the CSV file.

### Getting Started
1. Clone the repository to your local machine.
2. Make sure you have Python installed.
3. Run the script using `python bookshop.py` command in your terminal.

### Usage
1. Upon running the script, you will see a menu with various options.
2. Select an option by entering the corresponding number and pressing Enter.
3. Follow the prompts to perform the desired operation, such as searching for books, adding or deleting a book, updating stock, etc.
4. The script will display the results or status of the operation.
5. You can exit the script by choosing the "Exit" option from the menu.

### Data Structure
The script reads data from a CSV file (`books.csv`) with the following structure:
- Book ID: Identifier for the book.
- Title: Title of the book.
- Author: Author of the book.
- Category: Category of the book.
- Quantity: Quantity of the book in stock.
- Unit Price: Unit price of the book.
- Total Price: Total price of the book (calculated as Quantity * Unit Price).

### Contributing
Contributions are welcome! If you would like to improve the functionality or fix any issues, feel free to create a pull request.

### Contact
If you have any questions, suggestions, or feedback, please feel free to contact the author Mustafa via Twitter at [@mu57f4](https://twitter.com/mu57f4).