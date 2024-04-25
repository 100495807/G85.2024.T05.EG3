"""Module that store the arrival"""


from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_exception import HotelManagementException


# pylint: disable=invalid-name, too-few-public-methods, useless-parent-delegation

class ArrivalStore:
    """Clase que almacena la info de la llegada"""
    class __ArrivalStore(JsonStore):
        def __init__(self):
            super().__init__()

        def check_arrival(self, file_input):
            """funcion para verificar la llegada"""
            input_list = self.load_list_from_file(file_input)
            # comprobar valores del fichero
            try:
                my_localizer = input_list["Localizer"]
                my_id_card = input_list["IdCard"]
            except KeyError as error:
                raise HotelManagementException("Error - Invalid Key in JSON") from error
            return my_id_card, my_localizer

    __instance = None

    def __new__(cls):
        if not ArrivalStore.__instance:
            ArrivalStore.__instance = ArrivalStore.__ArrivalStore()
        # Add file path class attribute from inner class:
        return ArrivalStore.__instance
