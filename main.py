"""Modulo principal"""

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
            register_user = input("Introduzca un nombre de usuario: ")
            register_password = input("Introduca una contraseña: ")
            register_age = input("Introduzca fecha de nacimiento(dd/mm/yyyy): ")
            register_phone = input("Introduzca un número de teléfono: ")
            register_id = input("Introduca un documento de identificación(dni/nie: ")
            login = True
        elif register != "n":
            print("Valor introducido incorrecto.")
    else:
        print("Valor introducido incorrecto.")
