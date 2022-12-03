"""CLase Register con todas las funciones que realizan el registro"""

import os
import base64
from data_management.json_store import JsonStore
from data_management.cypher import Security
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import random


class Register:

    def __init__(self, user, accesskey, age, phone, id):
        self.__iban = self.generate_iban()
        self.__user = user
        self.__accesskey = accesskey
        self.__age = age
        self.__phone = phone
        self.__id = id
        self.__money = "0"
        self.__salt = os.urandom(16)

    # Función que genera un IBAN aleatorio
    @staticmethod
    def generate_iban():
        numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        iban_gen = "ES"
        for i in range(22):
            iban_gen = iban_gen + random.choice(numeros)
        return iban_gen

    # Función que deriva la contraseña con un salt y lo guarda en el json
    def derivation_value(self, key, value):
        json = JsonStore()
        mydict = {}
        kdf = Scrypt(salt=self.__salt, length=32, n=2**14, r=8, p=1)
        derivated_key = kdf.derive(value.encode())
        encoded = base64.b64encode(derivated_key)
        mydict[key] = encoded.decode("ascii")
        json.add_item(mydict)

    # Función que guarda el salt para derivar la contraseña
    def save_salt(self):
        json = JsonStore()
        mydict = {}
        encoded = base64.b64encode(self.__salt)
        mydict["salt"] = encoded.decode("ascii")
        json.add_item(mydict)

    # Función que sirve para encriptar y guardar los datos del registro del usuario
    def cypher_values(self):
        security = Security(self.__accesskey)
        key = "iban"
        iv = os.urandom(16)
        security.save_in_user_data(key, self.__iban, iv)        # Cifrado y almacenamiento de IBAN
        key = "usuario"
        iv = os.urandom(16)
        security.save_in_user_data(key, self.__user, iv)        # Cifrado y almacenamiento de usuario
        key = "contrasena"
        self.derivation_value(key, self.__accesskey)    # Derivación y almacenamiento de contraseña con salt
        key = "fecha_nacimiento"
        iv = os.urandom(16)
        security.save_in_user_data(key, self.__age, iv)         # Cifrado y almacenamiento de fecha de nacimiento
        key = "telefono"
        iv = os.urandom(16)
        security.save_in_user_data(key, self.__phone, iv)       # Cifrado y almacenamiento de número de teléfono
        key = "id"
        iv = os.urandom(16)
        security.save_in_user_data(key, self.__id, iv)          # Cifrado y almacenamiento de documento de identificación
        key = "saldo"
        iv = os.urandom(16)
        security.save_in_user_data(key, self.__money, iv)       # Cifrado y almacenamiento de dinero de la cuenta
        self.save_salt()                                # Almacenamiento de salt de contraseña
