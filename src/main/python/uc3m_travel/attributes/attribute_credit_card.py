"""
Este módulo es la base para el attribute credit card
"""

from uc3m_travel.attributes.attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException

class CreditCard(Attribute):
    """Definition of attribute Credit Card"""
    # pylint: disable=super-init-not-called, too-few-public-methods
    def __init__(self, attr_value):
        """Definition of attribute Credit Card init"""
        self._validation_pattern = r"^[0-9]{16}$"
        self._error_message = "Invalid credit card format"
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value):
        super()._validate(attr_value)
        # Convert the credit card number to a list of integers
        digits = [int(char) for char in attr_value]
        # Perform the Luhn algorithm checksum calculation
        checksum = 0
        for i, digit in enumerate(digits):
            if i % 2 == 0:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        # Check if the checksum is divisible by 10
        if checksum % 10 != 0:
            raise HotelManagementException("Invalid credit card number (not luhn)")

        # Return the validated credit card number
        return attr_value
