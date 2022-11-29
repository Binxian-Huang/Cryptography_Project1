class OPMoney:

    def __init__(self, money):
        self.__money = money
    #Pensar con qué sustituir los "return 0"
    def introducir_dinero(self, money):
        arg=OPMoney.no_int(money)
        if arg is False: #Argumento pasado no es un int
            return 0
        if money > 10000: #Número de euros máximo
            return 0
        nuevo_arg = self.__money + money
        #Nuevo_arg meterlo en clase Usuario
        print("Introducir dinero")
        print("¡Operación realizada con éxito!\n")


    def extraer_dinero(self, money):
    #El argumento es el dinero que el usuario quiere extraer
        arg = OPMoney.no_int(money)
        if arg is False: #Argumento pasado no es un int
            return 0
        if money > self.__money:
            return 0 #Error: Extraer más dinero del que se tiene
        nuevo_arg = self.__money - money
        #nuevo_arg meterlo en clase del usuario
        print("Extraer dinero")
        print("¡Operación realizada con éxito!\n")

    #Comprobar que el argumento pasado es un entero
    def no_int(money):
        if money is not int:
            return False
        return True


