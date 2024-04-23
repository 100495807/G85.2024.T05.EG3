from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.hotel_management_exception import HotelManagementException
from datetime import datetime

class CheckOutStore(JsonStore):
    _file_name = JSON_FILES_PATH + "store_check_out.json"
    def __init__(self):
        super().__init__()

    def add_item(self, item):
        """add_item para reservation_store"""
        check_out_found = self.find_item("room_key", item)
        if check_out_found:
            raise HotelManagementException("Guest is already out")
        room_checkout = {"room_key": item, "checkout_time": datetime.timestamp(datetime.utcnow())}
        super().add_item(room_checkout)