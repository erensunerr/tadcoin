from crypto import hash

class Block:
    def __init__(self):
        self.data = ""
        self.hash = ""
        self.nonce = 0
        self.data = ""
        self.prevHash = ""

    def add_data(self, data):
        self.data += data

    def import_block(self, data_string):
        x = data_string.split("|\n")
        self.hash = x[0]
        self.nonce = x[1]
        self.data = x[2]
        self.prevHash = x[3]

    def export_block(self):
        return "{0}|\n{1}|\n {2}|\n {3}".format(self.hash, self.nonce, self.data, self.prevHash)

    def __repr__(self):
        return "{0}|\n {1}|\n {2}".format(self.nonce, self.data, self.prevHash)

    def verify(self):
        return hash(str(self)) == self.hash

    def mine(self):
        def isGood(self):
            return hash(str(self))[0:4] == "0000"
        self.nonce = 0
        while not isGood(self):
            self.nonce+=1
        return True

    def read_data(self):
        return self.data
