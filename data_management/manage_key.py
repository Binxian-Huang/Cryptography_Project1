
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from data_management.cypher import Security
from data_management.exception_management import ProgramException


class Key:

    def __init__(self, accesskey):
        self.__accesskey = accesskey

    def generate_save_key(self):
        security = Security(self.__accesskey)
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.BestAvailableEncryption(security.get_key()))
        with open("D:/Julio/Uc3m/Curso3/Criptografia/Practica1/data_management/private_key.pem", "w+b") as file:
            file.write(pem)

    def load_key(self):
        security = Security(self.__accesskey)
        key_password = security.get_key()
        try:
            with open("D:/Julio/Uc3m/Curso3/Criptografia/Practica1/data_management/private_key.pem", "rb") as file:
                private_key = serialization.load_pem_private_key(file.read(), password=key_password)
                return private_key
        except FileNotFoundError as exception_raised:
            raise ProgramException("Wrong file or file path") from exception_raised

    def signing(self, message):
        private_key = self.load_key()
        signature = private_key.sign(message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return signature

    def verify(self, signature, message):
        private_key = self.load_key()
        public_key = private_key.public_key()
        public_key.verify(signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
