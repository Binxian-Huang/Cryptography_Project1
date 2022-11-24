import os
import base64
from data_management.json_store import JsonStore
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes

class Register:

    def __init__(self, user, accesskey, age, phone, id, money):
        self.__user = user
        self.__accesskey = accesskey
        self.__age = age
        self.__phone = phone
        self.__id = id
        self.__money= money
        self.__key = os.urandom(32)
   #Devolver datos para la opcion de mostrar Información
    def show_inf_user(self):
        return self.__user
    def show_inf_age(self):
        return self.__age
    def show_inf_phone(self):
        return self.__phone
    def show_inf_id(self):
        return self.__id
    def return_money(self):
        return self.__money
    #Cifrado del campo "usuario"
    def cypher_user(self):
        key = "usuario"
        self.cypher_values(key, self.__user)
    #Hash de la contraseña del usuario
    def hash_accesskey(self):
        key = "contrasena"
        self.hash_values(key, self.__accesskey)
    #Cifrado de la fecha de nacimiento
    def cypher_age(self):
        key = "fecha_nacimiento"
        self.cypher_values(key, self.__age)
    #Cifrado del número de teléfono
    def cypher_phone(self):
        key = "telefono"
        self.cypher_values(key, self.__phone)
    #Cifrado del documento de identificación
    def cypher_id(self):
        key = "usuario"
        self.cypher_values(key, self.__id)
    #Cifrado del dinero de la cuenta
    def cypher_money(self):
        self.cypher_values(key, self.__money)

    #Funcion principal para cifrar los campos del usuario
    def cypher_values(self, key, value):
        json = JsonStore()
        mydict = {}
        iv = os.urandom(16)
        bytes = value.encode()
        cipher = Cipher(algorithms.AES256(self.__key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(bytes) + padder.finalize()
        result = encryptor.update(padded_data) + encryptor.finalize()
        encoded_result = base64.b64encode(result)
        encoded_iv = base64.b64encode(iv)
        mydict[key] = encoded_result.decode("ascii")
        mydict["iv_"+key] = encoded_iv.decode("ascii")
        json.add_item(mydict)

    #Función principal para aplicar hash a los campos del usuario
    def hash_values(self, key, value):
        json = JsonStore()
        mydict = {}
        bytes = value.encode()
        hash_value = hashes.Hash(hashes.SHA256())
        hash_value.update(bytes)
        encoded = base64.b64encode(hash_value.finalize())
        mydict[key] = encoded.decode("ascii")
        json.add_item(mydict)

    def save_key(self):
        json = JsonStore()
        mydict = {}
        encoded = base64.b64encode(self.__key)
        mydict["key"] = encoded.decode("ascii")
        json.add_item(mydict)
