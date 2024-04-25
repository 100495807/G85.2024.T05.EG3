"""
Este módulo es la base para el attribute nombre
"""

from uc3m_travel.attributes.attribute import Attribute


class Name(Attribute):
    """Definition of attribute Name"""
    # pylint: disable=super-init-not-called, too-few-public-methods
    def __init__(self, attr_value):
        """Definition of attribute Name init"""
        super().__init__()
        self._validation_pattern = r"^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$"
        self._error_message = "Invalid name format"
        self._attr_value = self._validate(attr_value)
