from crypto import hash, kp
import datetime, math, queue
class Block:
    # Includes: index, timestamp in unix time, transactions, nonce and previous_hash
    def __init__(self, index=0, timestamp=datetime.datetime.now(), root=None):
        self.index = index
        self.timestamp = timestamp
        self.transactions = []
        self.nonce = 0
        self.prevHash = ""
        self.root = root

    def add_transaction(self, transaction):
        self.transactions += [transaction]
    def __str__(self):
        self.compute_merkle_root
        return f"{self.root}{self.index}{self.timestamp}{self.prevHash}{self.nonce}"

    def verify(self):
        return hash(str(self))[0:4] == "0000"

    def mine(self):
        self.root = self.compute_merkle_root()
        self.add_transaction(kp.pubkey())
        def isGood(self):
            return hash(str(self))[0:4] == "0000"
        self.nonce = 0
        while not isGood(self):
            self.nonce += 1
        return True

    def compute_merkle_root(self):
        n = len(self.transactions)
        depth = math.ceil(math.log2(n))
        s = self.transactions
        q = queue.SimpleQueue()
        for x in s:
            q.put(hash(x))

        for _ in range(depth):
            length = q.qsize()
            width = math.floor(length/2)+(length%2)
            for _ in range(width):
                if length == 1:
                    a = q.get()
                    q.put(a)
                    length -= 1
                else:
                    a = q.get()
                    b = q.get()
                    q.put(hash(str(a)+str(b)))
                    length -= 2

        return q.get()

def test():
    b = Block()
    for i in range(13):
        b.add_transaction(i)
    b.mine()
    print(hash(str(b)), b.nonce)

test()
