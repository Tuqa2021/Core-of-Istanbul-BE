class Transaction:
    def __init__(self, transaction_id, book, customer, quantity, date):
        self.transaction_id = transaction_id
        self.book = book
        self.customer = customer
        self.quantity = quantity
        self.date = date
