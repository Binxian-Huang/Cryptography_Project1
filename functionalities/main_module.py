"""Modulo principal"""

import data_management.validate_data
from functionalities.register import Register
from functionalities.login import Login
from data_management.json_store import JsonStore
from functionalities.operation_money import OPMoney

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
                             data_validated[4], 0)
    data_register.cypher_user()
    data_register.hash_accesskey()
    data_register.cypher_age()
    data_register.cypher_phone()
    data_register.cypher_id()
    data_register.cypher_money()
    data_register.save_key()
    print("Usuario registrado correctamente.")

def login_user():
    print("Para iniciar sesión introduzca usuario y contraseña.\n")
    user = input("Introduzca el usuario: ")
    accesskey = input("Introduzca la contraseña: ")
    login = Login(user, accesskey)
    result = login.validate_values()
    if result:
        print("Inicio de sesión correcto.\n")
    else:
        print("Usuario o contraseña incorrecto.")

def my_program():
    print("Hola bienvenido a la aplicación MyVirtualBank.\n")
    print("Para usar la aplicación debe ser miembro de nuestro banco.\n")
    login = False #Variable para controlar el login
    while not login:
        member = input("¿Tiene una cuenta creada?(y/n): \n").lower()
        if member == "y":#Iniciar sesión
            login_user()
            login = True
        elif member == "n":#Registro del usuario
            register = input("¿Quiere crear una cuenta?(y/n): \n").lower()
            if register == "y":
                json = JsonStore()
                json.empty_json_file()
                register_user()
                login = True #Nos hemos registrado, variable "login" cambia
            elif register == "n": #No queremos crear ninguna cuenta. Se cierra el programa
                print("Fin de programa.")
                exit()
            else:
                print("Valor introducido incorrecto.")
        else:
            print("Valor introducido incorrecto.")
    #login = True
    print("Bienvenido a MyVirtualBank\n")
    print("A continuación, le mostramos las posibles operaciones a realizar:")
    exit_program = False #Variable para controlar cuando salir del sistema
    while not exit_program:
        messages_oper()
        oper = input("¿Qué desea realizar?:").lower()
        if oper=="1": #Mostrar información de la cuenta
            print("Función para mostrar la información")
        elif oper=="2": #Depositar o extraer dinero
            messages_money()
            op_mon=input("¿Que operación desea realizar?\n").lower()
            if op_mon=="e":
                money_ext=input("¿Cuánto dinero desea extraer?")
                OPMoney.extraer_dinero(money_ext)
            elif op_mon=="i":
                money_int = input("¿Cuánto dinero desea introducir?")
                OPMoney.introducir_dinero(money_int)
        elif oper=="exit":
            exit_program= True #Salimos del bucle
        else:
            #Ninguna de las operaciones anteriores, mensaje para el usuario
            messages_error_op()
    print("Fin de programa. ¡Hasta la próxima!")
    exit()

#Mensajes del programa

def messages_oper():
    print("-Para mostrar información de la cuenta, introduzca 1")
    print("-Para extraer/depositar dinero en tu cuenta, introduzca 2")
    print("-Para salir del programa, introduzca exit\n")

def messages_money():
    print("¿Desea extraer o introducir dinero?")
    print("Para extraer dinero, inntroduzca e")
    print("Para introducir dinero, inntroduzca i")

def messages_error_op():
    print("Operación invalida, recuerda:")
    print("-Para mostrar información de la cuenta, introduzca 1")
    print("-Para depositar dinero en tu cuenta, introduzca 2")
    print("-Para salir del programa, introduzca exit\n")