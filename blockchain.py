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

    def search_address(self, address):
        for block in self.chain:
