from crypto import verify_pub_key, kp, dp, hash
#kp sender, dp recv
class transaction:
    def __init__(self, amount, pubkey_recv, pubkey_sender, signature=None):
        self.amount = amount
        self.pubkey_receiver = pubkey_recv
        self.signature = signature
        self.pubkey_sender = pubkey_sender

    def verify(self, signature=None):
        if not self.signature:
            self.signature = signature
        return verify_pub_key(self.pubkey_sender, self, self.signature)

    def sign(self, kp):
        x = self
        self.signature = kp.sign(x)
        return self.signature

    def __str__(self):
        return str(self.amount) + str(self.pubkey_receiver) + str(self.signature)

class money_created:
    def __init__(self, pubkey_recv, amount):
        self.pubkey_receiver = pubkey_recv
        self.amount = amount

    def verify(self):
        return True

def test():
    t = transaction(15, dp.pubkey(), kp.pubkey())
    x = t.sign(kp)
    p = transaction(15, dp.pubkey(), kp.pubkey(), signature=x)
test()
