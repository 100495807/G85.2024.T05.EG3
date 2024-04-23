from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.hotel_management_exception import HotelManagementException

class CheckInStore(JsonStore):
    _file_name = JSON_FILES_PATH + "store_check_in.json"
    def __init__(self):
        super().__init__()

    def add_item(self, item):
        check_in_found = self.find_item("_HotelStay__room_key", item.get("roomkey"))
        if check_in_found:
            raise HotelManagementException("Check-in already performed")
        super().add_item(item)

    def check_checkin(self, room_key):
        room_key_found = self.find_item("_HotelStay__room_key", room_key)
        if not room_key_found:
            raise HotelManagementException("Error: room key not found")
        departure_date_timestamp = room_key_found["_HotelStay__departure"]
        return departure_date_timestamp
