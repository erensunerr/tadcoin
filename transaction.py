from crypto import verify_pub_key,
class transaction:
    def from_data(self, recipient, sender, amount, pubkey, signature):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.pubkey = pubkey
        self.signature = signature

    def verify():
        verify_pub_key(self.pubkey, self.__repr__(), self.signature)

    def __repr__(self):
        if not self.signature:
            raise Exception("Sign the transaction.")
        return f"{self.sender}-{self.amount}-{self.recipient}-{self.signature}-{self.pubkey}"

    def from_repr(self, repr):
        x = repr.split('-')
        self.sender = x[0]
        self.amount = x[1]
        self.recipient = x[2]
        self.signature = x[3]
        self.pubkey = x[4]

    def sign(self, privateKey):
        
