from uc3m_travel.attributes.attribute import Attribute
from uc3m_travel.hotel_management_exception import HotelManagementException

class NumDays(Attribute):
    """Definition of attribute Number of Days"""

    def __init__(self, attr_value):
        """Definition of attribute Number of Days init"""
        attr_value = str(attr_value)
        self._validation_pattern = r"^\d+$"
        self._error_message = "Invalid num_days datatype"
        self._attr_value = self._validate(attr_value)

    def _validate(self, attr_value):
        """Validate the number of days"""
        super()._validate(attr_value)  # Use the parent validation first
        attr_value = int(attr_value)
        # Validar el rango
        if not (1 <= attr_value <= 10):
            raise HotelManagementException("Numdays should be in the range 1-10")

        # Return the validated number of days
        return attr_value