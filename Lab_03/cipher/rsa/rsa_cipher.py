from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os

class RSACipher:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.private_key_path = "private.pem"
        self.public_key_path = "public.pem"

    def generate_keys(self):
        key = RSA.generate(self.key_size)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open(self.private_key_path, "wb") as priv_file:
            priv_file.write(private_key)

        with open(self.public_key_path, "wb") as pub_file:
            pub_file.write(public_key)

    def load_keys(self):
        if not os.path.exists(self.private_key_path) or not os.path.exists(self.public_key_path):
            raise FileNotFoundError("Keys not found. Please generate keys first.")

        with open(self.private_key_path, "rb") as priv_file:
            private_key = RSA.import_key(priv_file.read())

        with open(self.public_key_path, "rb") as pub_file:
            public_key = RSA.import_key(pub_file.read())

        return private_key, public_key
    
    def load_key(self):
        private_key, public_key = self.load_keys()
        return private_key, public_key  # Trả về giống load_keys()

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        encrypted_message = cipher.encrypt(message.encode())
        return encrypted_message

    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        decrypted_message = cipher.decrypt(ciphertext)
        return decrypted_message.decode()

    def sign(self, message, private_key):
        h = SHA256.new(message.encode())
        signature = pkcs1_15.new(private_key).sign(h)
        return signature

    def verify(self, message, signature, public_key):
        h = SHA256.new(message.encode())
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False
