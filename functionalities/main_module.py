"""Modulo principal"""

import data_management.validate_data
from functionalities.register import Register
from functionalities.login import Login
from data_management.json_store import JsonStore

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

def register_user():
    data_validated = validate_register()
    data_register = Register(data_validated[0], data_validated[1], data_validated[2], data_validated[3],
                             data_validated[4])
    data_register.cypher_user()
    data_register.hash_accesskey()
    data_register.cypher_age()
    data_register.cypher_phone()
    data_register.cypher_id()
    data_register.save_key()
    print("Usuario registrado correctamente.")

def login_user():
    print("Para iniciar sesión introduzca usuario y contraseña.")
    user = input("Introduzca el usuario: ")
    accesskey = input("Introduzca la contraseña: ")
    login = Login(user, accesskey)
    result = login.validate_values()
    if result:
        print("Inicio de sesión correcto.")
    else:
        print("Usuario o contraseña incorrecto.")

def my_program():
    print("Hola bienvenido a la aplicación MyVirtualBank.")
    print("Para usar la aplicación debe ser miembro de nuestro banco.")
    login = False
    while not login:
        member = input("¿Tiene una cuenta creada?(y/n): ").lower()
        if member == "y":
            login_user()
            login = True
        elif member == "n":
            register = input("¿Quiere crear una cuenta?(y/n): ").lower()
            if register == "y":
                json = JsonStore()
                json.empty_json_file()
                register_user()
                login = True
            elif register == "n":
                print("Fin de programa.")
                exit()
            else:
                print("Valor introducido incorrecto.")
        else:
            print("Valor introducido incorrecto.")
