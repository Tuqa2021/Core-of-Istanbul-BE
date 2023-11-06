import Bookstore
import Customer

from DecHigherOrderFunctions import operate_on_books
from DecHigherOrderFunctions import discount_all_books
from DecHigherOrderFunctions import restock_books


class Book:
    """Represents a book in the bookstore's inventory.

    Attributes:
        isbn (str): The ISBN of the book.
        title (str): The title of the book.
        author (str): The author of the book.
        price (float): The price of the book.
        quantity (int): The quantity of the book in stock.
    """

    def __init__(self, isbn, title, author, price, quantity):
        """Initializes a new Book instance.

        Args:
            isbn (str): The ISBN of the book.
            title (str): The title of the book.
            author (str): The author of the book.
            price (float): The price of the book.
            quantity (int): The quantity of the book in stock.

        Returns:
            None
        """

    def add_stock(self, quantity):
        """Adds stock to the book's inventory.

        Args:
            quantity (int): The quantity of stock to add.

        Returns:
            None
        """

    def sell_stock(self, quantity):
        """Sells a specified quantity of books from the inventory.

        Args:
            quantity (int): The quantity to be sold.

        Returns:
            bool: True if the sale is successful, False if there's insufficient stock.
        """

# Example usage:
bookstore = Bookstore(is_admin=True)
book1 = Book("978-0451524935", "1984", "George Orwell", 9.99, 10)
book2 = Book("978-0061120084", "To Kill a Mockingbird", "Harper Lee", 12.99, 15)
book3 = Book("978-0141987432", "Animal Farm", "George Orwell", 8.99, 8)

bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book3)

print("Before applying operations:")
bookstore.list_all_books()

customer1 = Customer("Alice", "alice@example.com")
customer2 = Customer("Bob", "bob@example.com")

customer1.purchase_book(book1, 2, "2023-11-05")
customer1.purchase_book(book2, 1, "2023-11-06")
customer2.purchase_book(book1, 3, "2023-11-07")

bookstore.process_sale(customer1, "978-0451524935", 2, "2023-11-05")
bookstore.process_sale(customer2, "978-0061120084", 3, "2023-11-06")

customer1.display_purchase_history()
customer2.display_purchase_history()

# Apply discount to all books
operate_on_books(bookstore, lambda b, book: discount_all_books(b, book, 10))

# Restock books below a certain stock level
operate_on_books(bookstore, lambda b, book: restock_books(b, book, 10, 10))

print("After applying operations:")
bookstore.list_all_books()
