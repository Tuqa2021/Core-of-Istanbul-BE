import unittest
import Book
import Bookstore
import Customer
import Transaction
from DecHigherOrderFunctions import operate_on_books
from DecHigherOrderFunctions import discount_all_books
from DecHigherOrderFunctions import restock_books


class TestBookstore(unittest.TestCase):
    def test_add_book(self):
        bookstore = Bookstore(is_admin=True)
        book = Book("978-0451524935", "1984", "George Orwell", 9.99, 10)
        bookstore.add_book(book)
        self.assertIn("978-0451524935", bookstore.inventory)

    def test_remove_book(self):
        bookstore = Bookstore(is_admin=True)
        book = Book("978-0451524935", "1984", "George Orwell", 9.99, 10)
        bookstore.add_book(book)
        bookstore.remove_book("978-0451524935")
        self.assertNotIn("978-0451524935", bookstore.inventory)

    def test_find_book_by_isbn(self):
        bookstore = Bookstore(is_admin=True)
        book = Book("978-0451524935", "1984", "George Orwell", 9.99, 10)
        bookstore.add_book(book)
        found_book = bookstore.find_book_by_isbn("978-0451524935")
        self.assertEqual(found_book, book)

    def test_discount_all_books(self):
        bookstore = Bookstore(is_admin=True)
        book1 = Book("978-0451524935", "1984", "George Orwell", 9.99, 10)
        book2 = Book("978-0061120084", "To Kill a Mockingbird", "Harper Lee", 12.99, 5)
        bookstore.add_book(book1)
        bookstore.add_book(book2)
        operate_on_books(bookstore, lambda b, book: discount_all_books(b, book, 10))
        self.assertEqual(book1.price, 8.99)
        self.assertEqual(book2.price, 11.69)

class TestCustomer(unittest.TestCase):
    def test_purchase_book(self):
        customer = Customer("Alice", "alice@example.com")
        book = Book("978-0451524935", "1984", "George Orwell", 9.99, 10)
        customer.purchase_book(book, 2, "2023-11-05")
        self.assertEqual(len(customer.purchased_books), 1)

    def test_display_purchase_history(self):
        customer = Customer("Alice", "alice@example.com")
        book = Book("978-0451524935", "1984", "George Orwell", 9.99, 10)
        customer.purchase_book(book, 2, "2023-11-05")
        display_output = customer.display_purchase_history()
        self.assertIn("Alice's Purchase History", display_output)

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        book = Book("978-0451524935", "1984", "George Orwell", 9.99, 10)
        customer = Customer("Alice", "alice@example.com")
        transaction = Transaction(book, customer, 2, "2023-11-05")
        self.assertEqual(transaction.book, book)
        self.assertEqual(transaction.customer, customer)
        self.assertEqual(transaction.quantity, 2)

if __name__ == '__main__':
    unittest.main()
