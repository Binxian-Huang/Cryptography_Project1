from .register import Register
import random

class ShowInfo:
    def show_info():
        print("Monstrando información del usuario:\n")
        print("Nombre: ",Register.show_inf_user())
        print("Documento de identidad: ",Register.show_inf_id())
        print("Fecha de nacimiento",Register.show_inf_age())
        print("Número de teléfono: ",Register.show_inf_phone())
        print("Dinero de la cuenta",Register.show_money())
        print("IBAN cuenta MyVirtualBank",Register.show_iban())




