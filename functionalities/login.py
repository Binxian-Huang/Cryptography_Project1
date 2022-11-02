import base64
from data_management.json_store import JsonStore
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes


class Login:

    def __init__(self, user, accesskey):
        self.__user = user
        self.__accesskey = accesskey
        self.__key = self.decoded_values("key")
        self.__user_iv = self.decoded_values("iv_usuario")

    def decoded_values(self, key):
        value = self.find_in_json(key)
        return base64.b64decode(value)

    def find_in_json(self, key):
        json = JsonStore()
        value = json.find_item(key)
        return value

    def validate_user(self):
        cipher = Cipher(algorithms.AES256(self.__key), modes.CBC(self.__user_iv))
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(128).unpadder()
        padded_user_value = self.decoded_values("usuario")
        value = decryptor.update(padded_user_value) + decryptor.finalize()
        user_value = unpadder.update(value) + unpadder.finalize()
        #value = decryptor.update(user_value) + decryptor.finalize()
        if self.__user == user_value.decode():
            return True
        else:
            return False

    def validate_accesskey(self):
        bytes = self.__accesskey.encode()
        hash_value = hashes.Hash(hashes.SHA256())
        hash_value.update(bytes)
        encoded = base64.b64encode(hash_value.finalize())
        hash_accesskey = encoded.decode("ascii")
        saved_accesskey = self.find_in_json("contrasena")
        if hash_accesskey == saved_accesskey:
            return True
        else:
            return False

    def validate_values(self):
        validated_user = self.validate_user()
        validated_accesskey = self.validate_accesskey()
        if validated_user and validated_accesskey:
            return True
        else:
            return False
