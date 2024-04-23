from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_exception import HotelManagementException

class ArrivalStore(JsonStore):
    def __init__(self):
        super().__init__()

    def check_arrival(self, file_input):
        input_list = self.load_list_from_file(file_input)
        # comprobar valores del fichero
        try:
            my_localizer = input_list["Localizer"]
            my_id_card = input_list["IdCard"]
        except KeyError as error:
            raise HotelManagementException("Error - Invalid Key in JSON") from error
        return my_id_card, my_localizer