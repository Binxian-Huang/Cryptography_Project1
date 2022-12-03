"""Subclase SignatureStore de la clase JsonStore para las frimas con las mismas funciones pero que guarda las firmas en un archivo json diferente"""

from data_management.json_store import JsonStore


class SignatureStore(JsonStore):
    _FILE_PATH = "D:/Julio/Uc3m/Curso3/Criptografia/Practica1/data_management/data_json/user_operation_signature.json"
    _ID_FIELD = ""
    _data_list = []

    def load(self):
        super().load()

    def save(self):
        super().save()

    def add_item(self, item):
        super().add_item(item)

    def find_item(self, key_value):
        super().find_item(key_value)

    def empty_json_file(self):
        super().empty_json_file()
