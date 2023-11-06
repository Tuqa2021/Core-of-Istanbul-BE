import Transaction
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchased_books = []

    def purchase_book(self, book, quantity, date):
        if book.sell_stock(quantity):
            transaction = Transaction(book, self, quantity, date)
            self.purchased_books.append(transaction)

    def display_purchase_history(self):
        if not self.purchased_books:
            print(f"{self.name}'s purchase history is empty.")
        else:
            print(f"{self.name}'s Purchase History:")
            for transaction in self.purchased_books:
                print(f"Transaction ID: {transaction.transaction_id}")
                print(f"Book: {transaction.book.title}")
                print(f"Quantity: {transaction.quantity}")
                print(f"Date: {transaction.date}")
                print("------------------------------")

