import base64
from data_management.json_store import JsonStore
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

class Login:

    def __init__(self, user, accesskey):
        self.__user = user
        self.__accesskey = accesskey
        self.__salt = self.decoded_values("salt")
        self.__user_iv = self.decoded_values("iv_usuario")

    def decoded_values(self, key):
        value = self.find_in_json(key)
        return base64.b64decode(value)

    def find_in_json(self, key):
        json = JsonStore()
        value = json.find_item(key)
        return value

    def validate_user(self):
        key = self.get_key()
        cipher = Cipher(algorithms.AES256(key), modes.CBC(self.__user_iv))
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        padded_user_value = self.decoded_values("usuario")
        value = decryptor.update(padded_user_value) + decryptor.finalize()
        user_value = unpadder.update(value) + unpadder.finalize()
        if self.__user == user_value.decode():
            return True
        else:
            return False

    def validate_accesskey(self):
        kdf = Scrypt(salt=self.__salt, length=32, n=2 ** 14, r=8, p=1)
        derivated_accesskey = self.decoded_values("contrasena")
        try:
            kdf.verify(self.__accesskey.encode(), derivated_accesskey)
            return True
        except:
            return False

    def get_key(self):
        key_padder = padding.PKCS7(256).padder()
        key = key_padder.update(self.__accesskey.encode()) + key_padder.finalize()
        return key

    def validate_values(self):
        validated_accesskey = self.validate_accesskey()
        if validated_accesskey:
             return self.validate_user()
        else:
            return False
