"""Module for the hotel manager"""
from datetime import datetime
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from uc3m_travel.attributes.attribute_id_card import IdCard
from uc3m_travel.attributes.attribute_localizer import Localizer
from uc3m_travel.attributes.attribute_roomkey import RoomKey
from uc3m_travel.storage.reservation_store import ReservationStore
from uc3m_travel.storage.checkin_store import CheckInStore
from uc3m_travel.storage.checkout_store import CheckOutStore
from uc3m_travel.storage.arrival_store import ArrivalStore

class HotelManager:
    """Class with all the methods for managing reservations and stays"""

    def __init__(self):
        pass

    # pylint: disable=too-many-arguments
    def room_reservation(self,
                         credit_card: str,
                         name_surname: str,
                         id_card: str,
                         phone_number: str,
                         room_type: str,
                         arrival_date: str,
                         num_days: int) -> str:
        """manges the hotel reservation: creates a reservation and saves it into a json file"""
        my_reservation = HotelReservation(id_card=id_card,
                                          credit_card_number=credit_card,
                                          name_surname=name_surname,
                                          phone_number=phone_number,
                                          room_type=room_type,
                                          arrival=arrival_date,
                                          num_days=num_days)

        ReservationStore().add_item(my_reservation)

        return my_reservation.localizer


    def guest_arrival(self, file_input: str) -> str:
        """manages the arrival of a guest with a reservation"""
        my_checkin = HotelStay.create_guest_arrival_from_file(file_input)

        CheckInStore().add_item(my_checkin.__dict__)

        return my_checkin.room_key



    def guest_checkout(self, room_key: str) -> bool:
        """manages the checkout of a guest"""
        room_key = RoomKey(room_key).value
        departure_date_timestamp = CheckInStore().check_checkin(room_key)
        today = datetime.utcnow().date()
        if datetime.fromtimestamp(departure_date_timestamp).date() != today:
            raise HotelManagementException("Error: today is not the departure day")
        CheckOutStore().add_item(room_key)
        return True
