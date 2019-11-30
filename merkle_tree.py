from crypto import sha256

class MerkleNode:
    def __init__(self, value=None, c1=None, c2=None):
        if value:
            self.hash = sha256(value)
        elif c1 and c2:
            self.hash = sha256(c1 + c2)
            self.c1 = c1
            self.c2 = c2
        else:
            raise Exception("Please provide children or value")

class MerkleTree:
    def __init__(self, *vals):
        if vals:
            self.vals = vals
        else:
            raise Exception("No values provided")
        if len(self.vals) % 2 == 1:
            self.vals = self.vals + self.vals[-1]
        q = []
        for i in self.vals:
            q += MerkleNode(value=i)
        self.__generate(q)

    def __generate(self, vals):
        q = []
        for i in range(len(vals)//2):
            a, b = 2*i, 2*i+1
            parent = MerkleNode()
            c1 = MerkleNode(vals[a], vals[b])
            c2 = MerkleNode(vals[a])
        self.__generate(q)
