import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1

def hash(x):
  return hashlib.sha256(str(x).encode()).hexdigest()


class key_pair:
    def __init__(self):
        self.sk = None
        self.vk = None

    def open(self, location):
        file = open(location, "rb")
        sk = file.read()
        file.close()
        self.sk = SigningKey.from_pem(sk)
        self.vk = self.sk.verifying_key


    def save(self, location):
        file = open(location, "wb+")
        x = self.sk.to_pem()
        file.write(x)
        file.close()

    def generate(self):
        self.sk = SigningKey.generate(curve=SECP256k1) # uses NIST192p
        self.vk = self.sk.verifying_key

    def sign(self, message):
        return self.sk.sign(bytes(str(message), 'utf-8'))

    def pubkey(self):
        return self.vk.to_pem()

def verify_pub_key(pubkey, message, signature):
    pubkey_c = VerifyingKey.from_pem(pubkey)
    return pubkey_c.verify(signature, bytes(str(message), 'utf-8'))

kp = key_pair()
kp.open("k.ak")
dp = key_pair()
dp.open("x.ak")
