import hashlib
import json
from datetime import datetime
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_management_config import JSON_FILES_PATH


class JsonStore():
    """Clase JsonStore"""
    _file_name = ""

    def __init__(self):
        self._data_list = []
        self.load_list_from_file()

    @property
    def hash(self):
        self.load_list_from_file()
        return hashlib.md5(str(self._data_list).encode()).hexdigest()

    def save_list_to_file(self):
        try:
            with open(self._file_name, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as error:
            raise HotelManagementException("Wrong file  or file path") from error

    def load_list_from_file(self, file_name=None):
        try:
            if file_name:
                with open(file_name, "r", encoding="utf-8", newline="") as file:
                    self._data_list = json.load(file)
                    return self._data_list
            else:
                with open(self._file_name, "r", encoding="utf-8", newline="") as file:
                    self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError as error:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from error

    def add_item(self, item):
        """Agregar un nuevo elemento a la lista almacenada en el archivo JSON."""
        self.load_list_from_file()
        self._data_list.append(item)
        self.save_list_to_file()

    def find_item(self, key, value):
        """Buscar un elemento en la lista almacenada en el archivo JSON."""
        self.load_list_from_file()
        for item in self._data_list:
            if item[key] == value:
                return item
        return None
