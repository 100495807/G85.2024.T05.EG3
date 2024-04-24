import hashlib
from datetime import datetime
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.attributes.attribute_id_card import IdCard
from uc3m_travel.storage.arrival_store import ArrivalStore
from uc3m_travel.attributes.attribute_localizer import Localizer
from uc3m_travel.hotel_reservation import HotelReservation

class HotelStay:
    """Class for representing hotel stays"""
    def __init__(self,
                 idcard: str,
                 localizer: str,
                 numdays: int,
                 roomtype: str):
        """constructor for HotelStay objects"""
        self.__algorithm = "SHA-256"
        self.__type = roomtype
        self.__idcard = idcard
        self.__localizer = localizer
        justnow = datetime.utcnow()
        self.__arrival = datetime.timestamp(justnow)
        # timestamp is represented in seconds.miliseconds
        # to add the number of days we must express num_days in seconds
        self.__departure = self.__arrival + (numdays * 24 * 60 * 60)
        self.__room_key = hashlib.sha256(self.__signature_string().encode()).hexdigest()

    def __signature_string(self):
        """Composes the string to be used for generating the key for the room"""
        return "{alg:" + self.__algorithm + ",typ:" + self.__type + ",localizer:" + \
            self.__localizer + ",arrival:" + str(self.__arrival) + \
            ",departure:" + str(self.__departure) + "}"

    @property
    def id_card(self):
        """Property that represents the product_id of the patient"""
        return self.__idcard

    @id_card.setter
    def id_card(self, value):
        self.__idcard = value

    @property
    def localizer(self):
        """Property that represents the order_id"""
        return self.__localizer

    @localizer.setter
    def localizer(self, value):
        self.__localizer = value

    @property
    def arrival(self):
        """Property that represents the phone number of the client"""
        return self.__arrival

    @property
    def room_key(self):
        """Returns the sha256 signature of the date"""
        return self.__room_key

    @property
    def departure(self):
        """Returns the issued at value"""
        return self.__departure

    @departure.setter
    def departure(self, value):
        """returns the value of the departure date"""
        self.__departure = value

    @classmethod
    def create_guest_arrival_from_file(cls, file_input):
        my_id_card, my_localizer = ArrivalStore().check_arrival(file_input)
        my_id_card = IdCard(my_id_card).value
        my_localizer = Localizer(my_localizer).value
        new_reservation = HotelReservation.create_reservation_from_arrival(my_id_card, my_localizer)
        # compruebo si hoy es la fecha de checkin
        reservation_format = "%d/%m/%Y"
        date_obj = datetime.strptime(new_reservation.arrival, reservation_format)
        if date_obj.date() != datetime.date(datetime.utcnow()):
            raise HotelManagementException("Error: today is not reservation date")
        # genero la room key para ello llamo a Hotel Stay
        my_checkin = HotelStay(idcard=my_id_card, numdays=int(new_reservation.num_days),
                               localizer=my_localizer, roomtype=new_reservation.room_type)
        return my_checkin