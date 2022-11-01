"""Modulo principal"""
import data_management.validate_data
from functionalities.register import Register

def validate_register():

    register_user = ""
    validated = False
    while not validated:
        register_user = input("Introduzca un nombre de usuario: ")
        validated = data_management.validate_data.validate_user(register_user)

    register_accesskey = ""
    validated = False
    while not validated:
        register_accesskey = input("Introduca una clave de acceso: ")
        validated = data_management.validate_data.validate_accesskey(register_accesskey)

    register_age = ""
    validated = False
    while not validated:
        register_age = input("Introduzca fecha de nacimiento(dd/mm/yyyy): ")
        validated = data_management.validate_data.validate_age(register_age)

    register_phone = ""
    validated = False
    while not validated:
        register_phone = input("Introduzca un número de teléfono: ")
        validated = data_management.validate_data.validate_phone(register_phone)

    register_id = ""
    validated = False
    while not validated:
        register_id = input("Introduca un documento de identificación(dni/nie): ")
        validated = data_management.validate_data.validate_id(register_id)

    return register_user, register_accesskey, register_age, register_phone, register_id

def my_program():
    print("Hola bienvenido a la aplicación MyVirtualBank.")
    print("Para usar la aplicación debe ser miembro de nuestro banco.")
    login = False
    while not login:
        member = input("¿Tiene una cuenta creada?(y/n): ")
        if member == "y":
            user = input("Introduzca el usuario: ")
            password = input("Introduzca la contraseña: ")
            login = True
        elif member == "n":
            register = input("¿Quiere crear una cuenta?(y/n): ")
            if register == "y":
                data_validated = validate_register()
                data_register = Register(data_validated[0], data_validated[1], data_validated[2], data_validated[3], data_validated[4])
                data_register.cypher_user()
                data_register.cypher_age()
                data_register.cypher_phone()
                data_register.cypher_id()
                data_register.save_key()
                login = True
            elif register != "n":
                print("Valor introducido incorrecto.")
        else:
            print("Valor introducido incorrecto.")
