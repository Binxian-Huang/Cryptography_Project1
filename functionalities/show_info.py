
from functionalities.cypher import Security
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

class ShowInfo:
    def __init__(self, accesskey):
        self.__accesskey = accesskey
        self.__iban = self.show_value("iban").decode()
        self.__user = self.show_value("usuario").decode()
        self.__age = self.show_value("fecha_nacimiento").decode()
        self.__phone = self.show_value("telefono").decode()
        self.__id = self.show_value("id").decode()
        self.__money = self.show_value("saldo").decode()

    def validate_accesskey(self):
        security = Security(self.__accesskey)
        salt = security.decoded_value("salt")
        kdf = Scrypt(salt, length=32, n=2 ** 14, r=8, p=1)
        derivated_accesskey = security.decoded_value("contrasena")
        try:
            kdf.verify(self.__accesskey.encode(), derivated_accesskey)
            return True
        except:
            return False

    def get_value(self, iv_value, value):
        security = Security(self.__accesskey)
        return security.decode_value(iv_value, value)

    def show_value(self, value):
        iv_value = "iv_" + value
        return self.get_value(iv_value, value)

    def show_info(self):
        print("Monstrando información del usuario:\n")
        print("IBAN cuenta MyVirtualBank:", self.__iban)
        print("Nombre de usuario:", self.__user)
        print("Fecha de nacimiento:", self.__age)
        print("Número de teléfono:", self.__phone)
        print("Documento de identidad:", self.__id)
        print("Tu dinero:", self.__money)
        print()