from uc3m_travel.attributes.attribute import Attribute

class Localizer(Attribute):
    """Definition of attribute Localizer"""

    def __init__(self, attr_value):
        """Definition of attribute Localizer init"""
        super().__init__()
        self._validation_pattern = r'^[a-fA-F0-9]{32}$'
        self._error_message = "Invalid localizer"
        self._attr_value = self._validate(attr_value)
