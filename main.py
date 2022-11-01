"""Modulo principal"""
from functionalities.main_module import my_program
from data_management.json_store import JsonStore
def main():
    json = JsonStore()
    json.empty_json_file()
    my_program()

if __name__ == "__main__":
    main()

