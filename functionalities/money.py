
from data_management.cypher import Security
from data_management.manage_key import Key

class Money:

    def __init__(self, money, accesskey):
        self.__accesskey = accesskey
        self.__oper_money = money
        self.__money = self.get_account_money()

    def get_element_json(self, iv_key, key):
        security = Security(self.__accesskey)
        value = security.decode_value(iv_key, key)
        return value

    def get_account_money(self):
        iv_key = "iv_saldo"
        key = "saldo"
        saldo = self.get_element_json(iv_key, key)
        return saldo.decode()

    def get_iban(self):
        iv_key = "iv_iban"
        key = "iban"
        iban = self.get_element_json(iv_key, key)
        return iban.decode()

    def check_money(self):
        if self.__oper_money <= 0:
            print("Valor introducido incorrecto. Debe ser un número positivo mayor que 0.\n")
            return False
        elif self.__oper_money > 2000:
            print("Cantidad excedida del máximo por operación (Máx:2000).")
            return False
        elif self.__oper_money > int(self.__money):
            print("Valor introducido excede el saldo disponible.")
            print("Dinero disponible en tu cuenta:", self.__money)
            print()
            return False
        else:
            return True

    def get_message(self, oper, operation):
        iban_message = "Cuenta: " + self.get_iban() + "\n"
        operation_message = "Operación: " + operation + "\n"
        amount_message = "Cantidad de operación: " + str(self.__oper_money) + "\n"
        if oper == "+":
            final_money = int(self.__money) + self.__oper_money
        else:
            final_money = int(self.__money) - self.__oper_money
        final_money_message = "Saldo tras operación: " + str(final_money) + "\n"
        message = iban_message + operation_message + amount_message + final_money_message
        return message

    def signature_verification(self, message):
        key = Key(self.__accesskey)
        signature = key.signing(message)
        print("La firma de la operación es: " + signature)
        verify = False
        while not verify:
            option = input("Para verificar la firma teclee 'verify': ")
            if option == "verify":
                verification = key.verify(signature, message)
            else:
                print("Opción incorrecta.\n")

    def withdraw_money(self):
        operation = "extraer dinero"
        oper = "+"
        message = self.get_message(oper, operation)
        print(message)
        print("Operación realizada correctamente.\n")
        self.signature_verification(message)

    def deposit_money(self):
        operation = "ingresar dinero"
        oper = "-"
        message = self.get_message(oper, operation)
        print(message)
        print("Operación realizada correctamente.\n")
        self.signature_verification(message)
