from .register import Register
import random

class ShowInfo:
    def __init__(self, username, age, phone, id , money, Iban):
        self.__username = Register.show_inf_user()
        self.__age = Register.show_inf_age()
        self.__phone = Register.show_inf_phone()
        self.__id = Register.show_inf_id()
        self.__money = Register.show_money()
        self.__Iban = Register.show_iban()


    def show_info(self):
        print("Monstrando información del usuario:\n")
        print("Nombre: ",self.__username)
        print("Documento de identidad: ",self.__id)
        print("Fecha de nacimiento",self.__age)
        print("Número de teléfono: ",self.__phone)
        print("Dinero de la cuenta",self.__money)
        print("IBAN cuenta MyVirtualBank",self.__Iban)




