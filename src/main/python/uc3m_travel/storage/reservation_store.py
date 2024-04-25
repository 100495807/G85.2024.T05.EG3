from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.hotel_management_exception import HotelManagementException


class ReservationStore:

    class __ReservationStore(JsonStore):
        _file_name = JSON_FILES_PATH + "store_reservation.json"

        def __init__(self):
            """init de JsonStore para cargar datos"""
            super().__init__()

        def add_item(self, item):
            """add_item para reservation_store"""
            reservation_found = self.find_item("_HotelReservation__localizer", item.localizer)
            id_card_found = self.find_item("_HotelReservation__id_card", item.id_card)
            if reservation_found:
                raise HotelManagementException("Reservation already exists")
            if id_card_found:
                raise HotelManagementException("This ID card has another reservation")
            super().add_item(item.__dict__)

        def check_reservation(self, my_localizer):
            """check"""
            localizer_found = self.find_item("_HotelReservation__localizer", my_localizer)
            if localizer_found:
                return localizer_found
            else:
                raise HotelManagementException("Error: localizer not found")

    __instance = None

    def __new__(cls):
        if not ReservationStore.__instance:
            ReservationStore.__instance = ReservationStore.__ReservationStore()
        # Add file path class attribute from inner class:
        return ReservationStore.__instance
