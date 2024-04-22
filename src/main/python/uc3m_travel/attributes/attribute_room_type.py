from uc3m_travel.attributes.attribute import Attribute

class RoomType(Attribute):
    """Definition of attribute Room Type"""

    def __init__(self, attr_value):
        """Definition of attribute Room Type init"""
        super().__init__()
        self._validation_pattern = r"^(SINGLE|DOUBLE|SUITE)$"
        self._error_message = "Invalid roomtype value"
        self._attr_value = self._validate(attr_value)