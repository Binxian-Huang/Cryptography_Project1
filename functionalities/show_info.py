
from data_management.cypher import Security


class ShowInfo:
    def __init__(self, accesskey):
        self.__accesskey = accesskey
        self.__iban = self.show_value("iban").decode()
        self.__user = self.show_value("usuario").decode()
        self.__age = self.show_value("fecha_nacimiento").decode()
        self.__phone = self.show_value("telefono").decode()
        self.__id = self.show_value("id").decode()
        self.__money = self.show_value("saldo").decode()

    def get_value(self, iv_value, value):
        security = Security(self.__accesskey)
        return security.decode_value(iv_value, value)

    def show_value(self, value):
        iv_value = "iv_" + value
        return self.get_value(iv_value, value)

    def show_info(self):
        print("Mostrando información del usuario:")
        print("IBAN cuenta MyVirtualBank:", self.__iban)
        print("Nombre de usuario:", self.__user)
        print("Fecha de nacimiento:", self.__age)
        print("Número de teléfono:", self.__phone)
        print("Documento de identidad:", self.__id)
        print("Tu dinero:", self.__money)
        print()
