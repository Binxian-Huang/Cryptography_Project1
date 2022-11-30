
from data_management.cypher import Security


class Money:

    def __init__(self, money, accesskey):
        self.__accesskey = accesskey
        self.__oper_money = money
        self.__money = self.get_account_money()

    def check_money(self):
        if self.__oper_money <= 0:
            print("Valor introducido incorrecto. Debe ser un número positivo mayor que 0.\n")
            return False
        elif self.__oper_money > int(self.__money.decode()):
            print("Valor introducido excede el saldo disponible.")
            print("Dinero disponible en tu cuenta:", self.__money.decode())
            print()
            return False
        else:
            return True

    def get_account_money(self):
        security = Security(self.__accesskey)
        iv_key = "iv_saldo"
        key = "saldo"
        saldo = security.decode_value(iv_key, key)
        return saldo
