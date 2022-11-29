
from functionalities.cypher import Security
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

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
        kdf = Scrypt(salt=self.__salt, length=32, n=2 ** 14, r=8, p=1)
        derivated_accesskey = self.get_value("contrasena")
        try:
            kdf.verify(self.__accesskey.encode(), derivated_accesskey)
            return True
        except:
            return False

    #~Función que comprueba que ambos valores usuario y contraseña coinciden
    def validate_values(self):
        validated_accesskey = self.validate_accesskey()
        if validated_accesskey:
             return self.validate_user()
        else:
            return False
