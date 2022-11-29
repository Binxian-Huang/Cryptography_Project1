"""Modulo principal"""

import data_management.validate_data
from functionalities.register import Register
from functionalities.login import Login
from data_management.json_store import JsonStore
from functionalities.operation_money import OPMoney
from functionalities.show_info import ShowInfo

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
    data_register.cypher_values()
    print("Usuario registrado correctamente.\n")

def login_user():
    print("Para iniciar sesión introduzca usuario y contraseña.\n")
    access = False
    while not access:
        user = input("Introduzca el usuario: ")
        accesskey = input("Introduzca la contraseña: ")
        login = Login(user, accesskey)
        result = login.validate_values()
        if result:
            print("Inicio de sesión correcto.\n")
            access = True
        else:
            print("Usuario o contraseña incorrecto.\n")

def my_program():
    print("Hola bienvenido a la aplicación MyVirtualBank.")
    print("Para usar la aplicación debe ser miembro de nuestro banco.\n")
    login = False #Variable para controlar el login
    while not login:
        member = input("¿Tiene una cuenta creada?(y/n): ").lower()
        if member == "y":#Iniciar sesión
             login_user()
             login = True
        elif member == "n":#Registro del usuario
            register = input("¿Quiere crear una cuenta?(y/n): ").lower()
            if register == "y":
                json = JsonStore()
                json.empty_json_file()
                print()
                register_user()
                login = True #Nos hemos registrado, variable "login" cambia
            elif register == "n": #No queremos crear ninguna cuenta. Se cierra el programa
                print("Fin de programa.")
                exit()
            else:
                print("Valor introducido incorrecto.\n")
        else:
            print("Valor introducido incorrecto.\n")

    #login = True
    print("Bienvenido a MyVirtualBank.")
    print("A continuación, le mostramos las posibles operaciones a realizar: \n")
    exit_program = False #Variable para controlar cuando salir del sistema
    while not exit_program:
        messages_oper()
        oper = input("¿Qué desea realizar?: ").lower()
        if oper == "information": #Usuario elige mostrar información de la cuenta
            print("Para acceder a la información personal se necesita verificación de la identidad.")
            verified = False
            while not verified:
                access = input("Introduzca la contraseña: ")
                information = ShowInfo(access)
                if information.validate_accesskey() == True:
                    print("Identidad verificada.")
                    information.show_info()
                    verified = True
                else:
                    print("Contraseña incorrecta.")
        elif oper == "withdraw": #Usuario elige depositar/extraer dinero
            pass

        elif oper == "deposit":
            pass

        elif oper == "exit": #Usuario quiere salir del programa
            exit_program = True #Salimos del bucle
        else:
            #Ninguna de las operaciones anteriores, mensaje para el usuario
            print("Operación inválida.\n")
    print("Fin de programa. ¡Hasta la próxima!\n")
    exit()

#Mensajes del programa
def messages_oper(): #Mostrar información de las funcionalidades
    print("-Para mostrar información de la cuenta, introduzca 'information'.\n")
    print("-Para extraer dinero de tu cuenta, introduzca 'withdraw'.\n")
    print("-Para depositar dinero en tu cuenta, introduzca 'deposit'.\n")
    print("-Para salir del programa, introduzca 'exit'.\n")

