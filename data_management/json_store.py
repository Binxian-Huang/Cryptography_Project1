"""Class for managing storage in JSON files"""
import json
from data_management.exception_management import ProgramException


class JsonStore:
    """Class for managing storage in JSON files"""
    # FilePath Julio: "D:/Julio/Uc3m/Curso 3/Cuatrimestre 1/Criptografia/Practica1/data_management/data_json/user_data.json"
    # FilePath Álvaro: "C:/Users/alvar/PycharmProjects/Practica1_Criptografia/data_management/data_json/user_data.json"
    _FILE_PATH = "D:/Julio/Uc3m/Curso3/Criptografia/Practica1/data_management/data_json/user_data.json"
    _ID_FIELD = ""
    _data_list = []

    def __init__(self):
        pass

    def load(self):
        """Loading data into the datalist"""
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            # file is not found, so init my data_list
            self._data_list = []
        except json.JSONDecodeError as exception_raised:
            raise ProgramException("JSON Decode Error - Wrong JSON Format") from exception_raised

    def save(self):
        """Saves the datalist in the JSON file"""
        try:
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as exception_raised:
            raise ProgramException("Wrong file or file path") from exception_raised

    def add_item(self, item):
        """Adds a new item to the datalist and updates the JSON file"""
        self.load()
        self._data_list.append(item)
        self.save()

    def update_item(self, new_elem):
        self.load()
        new_data_list = []
        for elem in self._data_list:
            if elem.keys() != new_elem.keys():
                #res = {k: new_elem.get(k, v) for k, v in elem.items()}
                new_data_list.append(elem)
            else:
                new_data_list.append(new_elem)
        self.save()


    def find_item(self, key_value):
        """Finds the first item with the key_value in the datalist"""
        self.load()
        for item in self._data_list:
            if item.get(key_value) is not None:
                return item.get(key_value)
        return None

    def empty_json_file(self):
        """removes all data from the json file"""
        self._data_list = []
        self.save()
