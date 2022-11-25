import os
import base64
from data_management.json_store import JsonStore
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

class Register:

    def __init__(self, user, accesskey, age, phone, id, money, iban):
        self.__user = user
        self.__accesskey = accesskey
        self.__age = age
        self.__phone = phone
        self.__id = id
        self.__money = money
        self.__iban = iban
        self.__salt = os.urandom(16)
        self.__key = self.get_key()

    def generateIban(self):#IBAN aleatorio
        numeros=["0","1","2","3","4","5","6","7","8","9"]
        iban_gen="ES"
        for i in range(22):
            iban_gen = iban_gen + random.choice(numeros)
        return iban_gen

   #Devolver datos para la opcion de mostrar Información
    def show_inf_user(self):
        return self.__user
    def show_inf_age(self):
        return self.__age
    def show_inf_phone(self):
        return self.__phone
    def show_inf_id(self):
        return self.__id
    def show_money(self):
        return self.__money
    def show_iban(self):
        return self.__iban

    #Cifrado del campo "usuario"
    def cypher_user(self):
        key = "usuario"
        self.cypher_values(key, self.__user)
    #Hash de la contraseña del usuario
    def derivation_accesskey(self):
        key = "contrasena"
        self.derivation_value(key, self.__accesskey)
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
        key = "money"
        self.cypher_values(key, self.__money)

    #Funcion principal para cifrar los campos del usuario
    def cypher_values(self, key, value):
        json = JsonStore()
        mydict = {}
        iv = os.urandom(16)
        bytes = value.encode()
        cipher = Cipher(algorithms.AES256(self.__key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        data_padder = padding.PKCS7(128).padder()
        padded_data = data_padder.update(bytes) + data_padder.finalize()
        result = encryptor.update(padded_data) + encryptor.finalize()
        encoded_result = base64.b64encode(result)
        encoded_iv = base64.b64encode(iv)
        mydict[key] = encoded_result.decode("ascii")
        mydict["iv_"+key] = encoded_iv.decode("ascii")
        json.add_item(mydict)


    def get_key(self):
        key_padder = padding.PKCS7(256).padder()
        key = key_padder.update(self.__accesskey.encode()) + key_padder.finalize()
        return key

    def derivation_value(self, key, value):
        json = JsonStore()
        mydict = {}
        kdf = Scrypt(salt=self.__salt, length=32, n=2**14, r=8, p=1)
        derivated_key = kdf.derive(value.encode())
        encoded = base64.b64encode(derivated_key)
        mydict[key] = encoded.decode("ascii")
        json.add_item(mydict)

    def save_salt(self):
        json = JsonStore()
        mydict = {}
        encoded = base64.b64encode(self.__salt)
        mydict["salt"] = encoded.decode("ascii")
        json.add_item(mydict)
