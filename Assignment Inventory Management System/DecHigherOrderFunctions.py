import Transaction
def requires_admin(func):
    def wrapper(self, *args, **kwargs):
        if self.is_admin:
            return func(self, *args, **kwargs)
        else:
            print("Permission denied. This action requires admin privileges.")
    return wrapper

def transaction_logging(func):
    def wrapper(self, customer, isbn, quantity, date):
        book = self.find_book_by_isbn(isbn)
        if book and book.sell_stock(quantity):
            transaction = Transaction(book, customer, quantity, date)
            customer.purchased_books.append(transaction)
            print(f"Sale processed: {quantity} copies of '{book.title}' to {customer.name}")
            print(f"Transaction details: ID: {transaction.transaction_id}, Date: {date}")
        else:
            print("Sale could not be processed.")
    return wrapper

def operate_on_books(bookstore, operation_function):
    for isbn, book in bookstore.inventory.items():
        operation_function(bookstore, book)

def discount_all_books(bookstore, book, discount_percentage):
    book.price *= (1 - discount_percentage / 100)

def restock_books(bookstore, book, min_stock_level, restock_amount):
    if book.quantity < min_stock_level:
        book.add_stock(restock_amount)