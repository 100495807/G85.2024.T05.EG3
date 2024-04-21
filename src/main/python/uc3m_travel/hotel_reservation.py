"""Hotel reservation class"""
import hashlib
from uc3m_travel.hotel_management_exception import HotelManagementException
import re
from datetime import datetime

class HotelReservation:
    """Class for representing hotel reservations"""
    #pylint: disable=too-many-arguments, too-many-instance-attributes
    def __init__(self,
                 id_card:str,
                 credit_card_number:str,
                 name_surname:str,
                 phone_number:str,
                 room_type:str,
                 arrival:str,
                 num_days:int):
        """constructor of reservation objects"""
        self.__credit_card_number = credit_card_number
        self.__id_card = id_card
        justnow = datetime.utcnow()
        self.__arrival = arrival
        self.__reservation_date = datetime.timestamp(justnow)
        self.__name_surname = name_surname
        self.__phone_number = phone_number
        self.__room_type = room_type
        self.__num_days = num_days
        self.__localizer =  hashlib.md5(str(self).encode()).hexdigest()

    def __str__(self):
        """return a json string with the elements required to calculate the localizer"""
        #VERY IMPORTANT: JSON KEYS CANNOT BE RENAMED
        json_info = {"id_card": self.__id_card,
                     "name_surname": self.__name_surname,
                     "credit_card": self.__credit_card_number,
                     "phone_number:": self.__phone_number,
                     "reservation_date": self.__reservation_date,
                     "arrival_date": self.__arrival,
                     "num_days": self.__num_days,
                     "room_type": self.__room_type,
                     }
        return "HotelReservation:" + json_info.__str__()
    @property
    def credit_card(self):
        """property for getting and setting the credit_card number"""
        return self.__credit_card_number
    @credit_card.setter
    def credit_card(self, value):
        self.__credit_card_number = value

    @property
    def id_card(self):
        """property for getting and setting the id_card"""
        return self.__id_card
    @id_card.setter
    def id_card(self, value):
        self.__id_card = value


    @property
    def localizer(self):
        """Returns the md5 signature"""
        return self.__localizer

    @staticmethod
    def check_dni(dni):
        """Validate the DNI syntax and letter"""
        options = {"0": "T", "1": "R", "2": "W", "3": "A", "4": "G", "5": "M",
                   "6": "Y", "7": "F", "8": "P", "9": "D", "10": "X", "11": "B",
                   "12": "N", "13": "J", "14": "Z", "15": "S", "16": "Q", "17": "V",
                   "18": "H", "19": "L", "20": "C", "21": "K", "22": "E"}

        result = r'^[0-9]{8}[A-Z]{1}$'
        my_registration = re.compile(result)
        if not my_registration.fullmatch(dni):
            raise HotelManagementException("Invalid IdCard format")

        numbers_dni = int(dni[0:8])
        letra_dni = str(numbers_dni % 23)
        if dni[8] != options[letra_dni]:
            raise HotelManagementException("Invalid IdCard letter")

        return dni

    @staticmethod
    def validate_room_type(room_type):
        """validates the room type value using regex"""
        my_registration = re.compile(r"(SINGLE|DOUBLE|SUITE)")
        result = my_registration.fullmatch(room_type)
        if not result:
            raise HotelManagementException("Invalid roomtype value")
        return room_type

    @staticmethod
    def validate_name(name):
        """validate the name and surname using a regex"""
        result = r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$"
        my_registration = re.compile(result)
        regex_matches = my_registration.fullmatch(name)
        if not regex_matches:
            raise HotelManagementException("Invalid name format")
        return name

    @staticmethod
    def validatecreditcard(credit_card):
        """Validates the credit card number using the Luhn algorithm"""
        # Compile a regular expression pattern to match a 16-digit number
        my_registration = re.compile(r"^[0-9]{16}")

        # Check if the credit card number matches the pattern
        if not my_registration.fullmatch(credit_card):
            raise HotelManagementException("Invalid credit card format")

        # Convert the credit card number to a list of integers
        digits = [int(char) for char in credit_card]

        # Perform the Luhn algorithm checksum calculation
        checksum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        # Check if the checksum is divisible by 10
        if not checksum % 10 == 0:
            raise HotelManagementException("Invalid credit card number (not luhn)")

        # Return the validated credit card number
        return credit_card

    @staticmethod
    def validate_arrival_date(arrival_date):
        """validates the arrival date format  using regex"""
        my_registration = re.compile(r"^(([0-2]\d|-3[0-1])\/(0\d|1[0-2])\/\d\d\d\d)$")
        result = my_registration.fullmatch(arrival_date)
        if not result:
            raise HotelManagementException("Invalid date format")
        return arrival_date

    @staticmethod
    def validate_numdays(num_days):
        """validates the number of days"""
        try:
            days = int(num_days)
        except ValueError as error:
            raise HotelManagementException("Invalid num_days datatype") from error
        if (days < 1 or days > 10):
            raise HotelManagementException("Numdays should be in the range 1-10")
        return num_days

    @staticmethod
    def validate_phonenumber(phone_number):
        """validates the phone number format  using regex"""
        my_registration = re.compile(r"^(\+)[0-9]{9}")
        result = my_registration.fullmatch(phone_number)
        if not result:
            raise HotelManagementException("Invalid phone number format")
        return phone_number

    @staticmethod
    def validate_localizer(localizer):
        """validates the localizer format using a regex"""
        result = r'^[a-fA-F0-9]{32}$'
        my_registration = re.compile(result)
        if not my_registration.fullmatch(localizer):
            raise HotelManagementException("Invalid localizer")
        return localizer