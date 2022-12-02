
import base64
from data_management.json_store import JsonStore
from data_management.json_store_signature import SignatureStore
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

    def check_money_withdraw(self):
        if self.__oper_money <= 0:
            print("Valor introducido incorrecto. Debe ser un número positivo mayor que 0 BBBBBBBBBBBBBBB.\n")
            return False
        elif self.__oper_money > int(self.__money):
            print("Valor introducido excede el saldo disponible.")
            print("Dinero disponible en tu cuenta:", self.__money)
            print()
            return False
        else:
            return True

    def check_money_deposit(self):
        if self.__oper_money <= 0:
            print("Valor introducido incorrecto. Debe ser un número positivo mayor que 0 CCCCCCCCCCCCCCCCCC.\n")
            return False
        elif self.__oper_money > 2000:
            print("Cantidad excedida del máximo por operación (Máx:2000).\n")
            return False
        else:
            return True

    def get_message(self, oper, operation):
        iban_message = "Cuenta: " + self.get_iban() + "\n"
        operation_message = "Operación: " + operation + "\n"
        amount_message = "Cantidad de operación: " + str(self.__oper_money) + "\n"
        current_money_mesage = "Saldo antes de operación: " + self.__money + "\n"
        if oper == "+":
            final_money = int(self.__money) + self.__oper_money
        else:
            final_money = int(self.__money) - self.__oper_money
        final_money_message = "Saldo tras operación: " + str(final_money) + "\n"
        message = iban_message + operation_message + current_money_mesage + amount_message + final_money_message
        return message, final_money

    def get_signature(self, message):
        key = Key(self.__accesskey)
        signature = key.signing(message.encode())
        print("Se ha guardado una firma recibo de la operación.\n")
        #print("La firma de la operación es: \n" + signature.decode())
        return signature

    def save_signature(self, operation, oper, signature):
        json = SignatureStore()
        mydict = {}
        key = "Firma de " + operation + " " + oper + str(self.__oper_money)
        encoded_signature = base64.b64encode(signature)
        mydict[key] = encoded_signature.decode("ascii")
        json.add_item(mydict)

    def save_new_money(self, new_money):
        security = Security(self.__accesskey)
        key = "saldo"
        iv = security.decoded_value("iv_saldo")
        mydict = security.encode_value(iv, key, new_money)
        json = JsonStore()
        json.update_item(mydict)

    def signature_verification(self, message, signature):
        key = Key(self.__accesskey)
        verified = False
        while not verified:
            option = input("Para verificar la firma teclee 'verify', en caso contrario teclee 'exit': ").lower()
            print()
            if option == "verify":
                try:
                    verification = key.verify(signature, message.encode())
                    print("Verificación de firma correcta. La firma está realizada por MyVirtualBank.\n")
                except Exception:
                    print("Verificación errónea. La firma no está realizada por MyVirtualBank.\n")
                verified = True
            elif option == "exit":
                verified = True
            else:
                print("Opción incorrecta.\n")
                verified = False

    def withdraw_money(self):
        operation = "extraer dinero"
        oper = "-"
        message, new_money = self.get_message(oper, operation)
        print(message)
        print("Operación realizada correctamente.")
        signature = self.get_signature(message)
        self.save_signature(operation, oper, signature)
        self.save_new_money(str(new_money))
        self.signature_verification(message, signature)

    def deposit_money(self):
        operation = "ingresar dinero"
        oper = "+"
        message, new_money = self.get_message(oper, operation)
        print(message)
        print("Operación realizada correctamente.")
        signature = self.get_signature(message)
        self.save_signature(operation, oper, signature)
        self.save_new_money(str(new_money))
        self.signature_verification(message, signature)
