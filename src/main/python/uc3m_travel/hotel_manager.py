"""Module for the hotel manager"""
from datetime import datetime
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_reservation import HotelReservation
from uc3m_travel.hotel_stay import HotelStay
from freezegun import freeze_time
from uc3m_travel.attributes.attribute_id_card import IdCard
from uc3m_travel.attributes.attribute_localizer import Localizer
from uc3m_travel.attributes.attribute_roomkey import RoomKey
from uc3m_travel.storage.json_store import JsonStore
import json
reservation_store = JsonStore()

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
        reservation_store.save_reservation(my_reservation)

        return my_reservation.localizer

    def guest_arrival(self, file_input: str) -> str:
        """manages the arrival of a guest with a reservation"""
        my_id_card, my_localizer = reservation_store.check_arrival(file_input)

        my_id_card = IdCard(my_id_card).value
        my_localizer = Localizer(my_localizer).value

        found, reservation_credit_card, reservation_date_arrival, reservation_date_timestamp, reservation_days, reservation_id_card, reservation_name, reservation_phone, reservation_room_type = reservation_store.check_reservation(
            my_localizer)

        if not found:
            raise HotelManagementException("Error: localizer not found")
        if my_id_card != reservation_id_card:
            raise HotelManagementException("Error: Localizer is not correct for this IdCard")
        # regenrar clave y ver si coincide
        reservation_date = datetime.fromtimestamp(reservation_date_timestamp)

        with freeze_time(reservation_date):
            new_reservation = HotelReservation(credit_card_number=reservation_credit_card,
                                               id_card=reservation_id_card,
                                               num_days=reservation_days,
                                               room_type=reservation_room_type,
                                               arrival=reservation_date_arrival,
                                               name_surname=reservation_name,
                                               phone_number=reservation_phone)
        if new_reservation.localizer != my_localizer:
            raise HotelManagementException("Error: reservation has been manipulated")

        # compruebo si hoy es la fecha de checkin
        reservation_format = "%d/%m/%Y"
        date_obj = datetime.strptime(reservation_date_arrival, reservation_format)
        if date_obj.date() != datetime.date(datetime.utcnow()):
            raise HotelManagementException("Error: today is not reservation date")

        # genero la room key para ello llamo a Hotel Stay
        my_checkin = HotelStay(idcard=my_id_card, localizer=my_localizer, numdays=int(reservation_days),
                               roomtype=reservation_room_type)

        # Ahora lo guardo en el almacen nuevo de checkin
        reservation_store.write_checkin(my_checkin.__dict__)

        return my_checkin.room_key

    def guest_checkout(self, room_key: str) -> bool:
        """manages the checkout of a guest"""
        room_key = RoomKey(room_key).value
        #check that the roomkey is stored in the checkins file
        departure_date_timestamp = reservation_store.check_checkin(room_key)

        today = datetime.utcnow().date()
        if datetime.fromtimestamp(departure_date_timestamp).date() != today:
            raise HotelManagementException("Error: today is not the departure day")

        reservation_store.write_checkout(room_key)

        return True
