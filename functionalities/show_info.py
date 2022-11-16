from .register import Register
import random

class ShowInfo:

    def __init__(self):
        self.__iban = self.generateIban() #Número IBAN de la cuenta
        self.__money = 0 #Dinero de la cuenta

    def generateIban(self):#IBAN aleatorio
        numeros=["0","1","2","3","4","5","6","7","8","9"]
        iban_gen="ES"
        for i in range(22):
            iban_gen = iban_gen + random.choice(numeros)
        return iban_gen
    #Mostrar la informacion de la clase Registro
    def show_register(self):
        #Nombre usuario, fecha de nacimiento, número de teléfono y DNI
        print("Nombre del usuario: ",Register.show_inf_user())
        print("Fecha de nacimiento: ",Register.show_inf_age())
        print("Número de teléfono: ",Register.show_inf_phone())
        print("Documento de identificación: ",Register.show_inf_id())

    #Mostrar IBAN de la cuenta
    def show_iban(self):
        print("IBAN de la cuenta: ", self.__iban)

    #Mostrar dinero de la cuenta
    def show_money(self):
        print("Dinero de la cuenta: ", self.__money)

    #Funcion principal qque llamará a todas las anteriores
    def show_information(self):
        #Función principal de la clase
        self.show_register()
        self.show_iban()
        self.show_money()



