class Mempool:
    def __init__(self):
        self.transactions = []
        
    def add_transaction(self, transaction):
        self.transactions += [transaction]

    def get_transactions(self):
        return self.transactions

    def flush(self):
        self.transactions = []
