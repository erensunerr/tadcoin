class Blockchain:
    def __init__(self):
        self.chain = []
        #TODO: sync chain with others on the network

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
