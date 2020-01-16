import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1
def hash(x):
  return hashlib.sha256(str(x).encode()).hexdigest()


class key_pair:
    def __init__(self):
        self.sk = None
        self.vk = None
    def open(self, location):
        file = open(location, "r")
        sk = file.read().split("\n")
        self.sk = SigningKey.from_der(sk.decode('ascii'))
        self.vk = self.sk.verifying_key
        file.close()

    def save(self, location):
        file = open(location, "wb+")
        file.write(f"{self.sk.to_der()}".encode('ascii'))
        file.close()
    def generate(self):
        self.sk = SigningKey.generate(curve=SECP256k1) # uses NIST192p
        self.vk = self.sk.verifying_key
    def sign(self, message):
        return self.sk.sign(message)
    def pubkey(self):
        return self.vk.to_string()

def verif_pub_key(pubkey, message, signature):
    pubkey_c = VerifyingKey.from_string(pubkey, curve=SECP256k1)
    return pubkey_c.verify(signature, message)

n = key_pair()
n.generate()
print(n.pubkey())
n.save("./k.ak")
a = key_pair()
a.open("./k.ak")
print(a.pubkey())
