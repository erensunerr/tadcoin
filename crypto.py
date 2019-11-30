import hashlib
from ecdsa import SigningKey, VerifyingKey, SECP256k1
def hash(x):
  return hashlib.sha256(str(x).encode()).hexdigest()


class key_pair:
    def __init__(self):
        pass
    def open(self, location):
        pass
    def save(self, location):
        pass
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
