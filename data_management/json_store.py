"""Clase JsonStore con las funciones relacionadas al archivo json"""
import json
from data_management.exception_management import ProgramException


class JsonStore:
    # FilePath Julio: "D:/Julio/Uc3m/Curso 3/Cuatrimestre 1/Criptografia/Practica1/data_management/data_json/user_data.json"
    # FilePath Álvaro: "C:/Users/alvar/PycharmProjects/Practica1_Criptografia/data_management/data_json/user_data.json"
    _FILE_PATH = "D:/Julio/Uc3m/Curso3/Criptografia/Practica1/data_management/data_json/user_data.json"
    _ID_FIELD = ""
    _data_list = []

    def __init__(self):
        pass

    # Función que carga el contenido del json en la lista de datos
    def load(self):
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError as exception_raised:
            raise ProgramException("JSON Decode Error - Wrong JSON Format") from exception_raised

    # Función que guarda la lista de datos en el json
    def save(self):
        try:
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as exception_raised:
            raise ProgramException("Wrong file or file path") from exception_raised

    # Función que añade un elemento al final de la lista y la guarda
    def add_item(self, item):
        self.load()
        self._data_list.append(item)
        self.save()

    # Función que actualiza un elemento el la lista con las mismas claves pero diferentes valores
    def update_item(self, new_elem):
        self.load()
        new_data_list = []
        for elem in self._data_list:
            if elem.keys() != new_elem.keys():
                new_data_list.append(elem)
            else:
                new_data_list.append(new_elem)
        self._data_list = new_data_list
        self.save()

    # Función que encuentra el valor en el json
    def find_item(self, key_value):
        self.load()
        for item in self._data_list:
            if item.get(key_value) is not None:
                return item.get(key_value)
        return None

    # Función que vacía el archivo json
    def empty_json_file(self):
        self._data_list = []
        self.save()
