from uc3m_travel.storage.json_store import JsonStore
from uc3m_travel.hotel_management_config import JSON_FILES_PATH
from uc3m_travel.hotel_management_exception import HotelManagementException
class ReservationStore(JsonStore):
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
        found = False
        localizer_found = self.find_item("_HotelReservation__localizer", my_localizer)
        if localizer_found:
            found = True
            reservation_days = localizer_found["_HotelReservation__num_days"]
            reservation_room_type = localizer_found["_HotelReservation__room_type"]
            reservation_date_timestamp = localizer_found["_HotelReservation__reservation_date"]
            reservation_credit_card = localizer_found["_HotelReservation__credit_card_number"]
            reservation_date_arrival = localizer_found["_HotelReservation__arrival"]
            reservation_name = localizer_found["_HotelReservation__name_surname"]
            reservation_phone = localizer_found["_HotelReservation__phone_number"]
            reservation_id_card = localizer_found["_HotelReservation__id_card"]
            return found, reservation_credit_card, reservation_date_arrival, reservation_date_timestamp, reservation_days, reservation_id_card, reservation_name, reservation_phone, reservation_room_type
        else:
            return (found, None, None, None, None, None, None, None, None)