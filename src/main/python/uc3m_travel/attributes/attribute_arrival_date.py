from uc3m_travel.attributes.attribute import Attribute

class ArrivalDate(Attribute):
    """Definition of attribute Arrival Date"""

    def __init__(self, attr_value):
        """Definition of attribute Arrival Date init"""
        super().__init__()
        self._validation_pattern = r"^(([0-2]\d|-3[0-1])\/(0\d|1[0-2])\/\d{4})$"
        self._error_message = "Invalid date format"
        self._attr_value = self._validate(attr_value)