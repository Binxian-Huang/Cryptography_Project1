import os
from data_management.json_store import JsonStore
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding


class Register:

    def __init__(self, user, accesskey, age, phone, id):
        self.__user = user
        self.__accesskey = accesskey
        self.__age = age
        self.__phone = phone
        self.__id = id
        self.__key = os.urandom(32)

    def cypher_user(self):
        key = "usuario"
        self.cypher_values(key, self.__user)

    def cypher_age(self):
        key = "fecha_nacimiento"
        self.cypher_values(key, self.__age)

    def cypher_phone(self):
        key = "telefono"
        self.cypher_values(key, self.__phone)

    def cypher_id(self):
        key = "usuario"
        self.cypher_values(key, self.__id)

    def cypher_values(self, key, value):
        json = JsonStore()
        mydict = {}
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES256(self.__key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        #padder = padding.PKCS7(128).padder()
        #padded_data = padder.update(value) + padder.finalize()
        result = encryptor.update(value) + encryptor.finalize()
        mydict[key] = result
        mydict["iv"] = iv
        json.add_item(mydict)

    def save_key(self):
        json = JsonStore
        mydict = {}
        mydict["key"] = self.__key
        json.add_item(mydict)
