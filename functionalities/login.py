
from data_management.cypher import Security


class Login:

    def __init__(self, user, accesskey):
        self.__user = user
        self.__accesskey = accesskey
        self.__salt = self.get_salt()

    # Función que accede al salt
    def get_salt(self):
        return self.get_value("salt")

    # Función que busca el elemento con clave "key" en el archivo json
    def get_value(self, key):
        security = Security(self.__accesskey)
        value = security.decoded_value(key)
        return value

    # Función que comprueba que el usuario introducido coincide con el guardado
    def validate_user(self):
        security = Security(self.__accesskey)
        iv_key = "iv_usuario"
        key = "usuario"
        user_value = security.decode_value(iv_key, key)
        if self.__user == user_value.decode():
            return True
        else:
            return False

    # Función que comprueba que la contraseña introducida y aplicado al salt coincide con la guardada
    def validate_accesskey(self):
        security = Security(self.__accesskey)
        return security.validate_accesskey()

    # Función que comprueba que ambos valores usuario y contraseña coinciden
    def validate_values(self):
        validated_accesskey = self.validate_accesskey()
        if validated_accesskey:
            return self.validate_user()
        else:
            return False
