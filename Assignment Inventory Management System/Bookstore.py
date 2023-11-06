import Transaction
from DecHigherOrderFunctions import requires_admin
from DecHigherOrderFunctions import transaction_logging

class Bookstore:
    def __init__(self, is_admin=False):
        self.inventory = {}
        self.is_admin = is_admin

    @requires_admin
    def add_book(self, book):
        if book.isbn in self.inventory:
            print(f"Book with ISBN {book.isbn} already exists in the inventory.")
        else:
            self.inventory[book.isbn] = book
            print(f"Added '{book.title}' to the inventory.")

    @requires_admin
    def remove_book(self, isbn):
        if isbn in self.inventory:
            del self.inventory[isbn]
            print(f"Removed book with ISBN {isbn} from the inventory.")
        else:
            print(f"Book with ISBN {isbn} is not found in the inventory.")

    def find_book_by_isbn(self, isbn):
        if isbn in self.inventory:
            return self.inventory[isbn]
        else:
            print(f"Book with ISBN {isbn} is not found in the inventory.")
            return None

    def list_all_books(self):
        print("Inventory of the Bookstore:")
        for isbn, book in self.inventory.items():
            print(f"ISBN: {isbn}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Price: ${book.price}")
            print(f"Quantity: {book.quantity}")
            print("------------------------------")

    @transaction_logging
    def process_sale(self, customer, isbn, quantity, date):
        book = self.find_book_by_isbn(isbn)
        if book and book.sell_stock(quantity):
            transaction = Transaction(book, customer, quantity, date)
            customer.purchased_books.append(transaction)
            print(f"Sale processed: {quantity} copies of '{book.title}' to {customer.name}")
        else:
            print("Sale could not be processed.")
