class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        try:
            last = self.chain[-1]
        except:
            last = None
        if not block.prevHash:
            if last:
                block.prevHash = self.chain[-1].hash
            block.mine()
        print(block, block.verify())
        if block.verify():
            self.chain += block
        return True

    def search_pubkey(self, pubkey):
        x = 0
        for block in self.chain:
            for transaction in block.transactions:
                transaction.verify()
                if transaction.pubkey_receiver == pubkey:
                    x += transaction.value
                if transaction.pubkey_sender == pubkey:
                    x -= transaction.value
        return x
