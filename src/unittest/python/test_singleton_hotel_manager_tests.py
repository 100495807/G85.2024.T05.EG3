" Module for the test opf singleton"
import unittest
from uc3m_travel.hotel_manager import HotelManager
from uc3m_travel.storage.arrival_store import ArrivalStore
from uc3m_travel.storage.checkin_store import CheckInStore
from uc3m_travel.storage.checkout_store import CheckOutStore
from uc3m_travel.storage.reservation_store import ReservationStore
from uc3m_travel.attributes.attribute_id_card import IdCard


# pylint: disable=missing-class-docstring
class MyTestcase(unittest.TestCase):

    # pylint: disable=too-many-locals
    # pylint: disable=missing-function-docstring
    def test_singleton_hotel_manager_tests(self):
        hotel_manager_1 = HotelManager()
        hotel_manager_2 = HotelManager()
        hotel_manager_3 = HotelManager()

        self.assertEqual(hotel_manager_1, hotel_manager_2)
        self.assertEqual(hotel_manager_2, hotel_manager_3)
        self.assertEqual(hotel_manager_3, hotel_manager_1)

        arrival_store_1 = ArrivalStore()
        arrival_store_2 = ArrivalStore()
        arrival_store_3 = ArrivalStore()

        self.assertEqual(arrival_store_1, arrival_store_2)
        self.assertEqual(arrival_store_2, arrival_store_3)
        self.assertEqual(arrival_store_3, arrival_store_1)

        checkin_store1 = CheckInStore()
        checkin_store2 = CheckInStore()
        checkin_store3 = CheckInStore()

        self.assertEqual(checkin_store1, checkin_store2)
        self.assertEqual(checkin_store2, checkin_store3)
        self.assertEqual(checkin_store3, checkin_store1)

        checkout_store1 = CheckOutStore()
        checkout_store2 = CheckOutStore()
        checkout_store3 = CheckOutStore()

        self.assertEqual(checkout_store1, checkout_store2)
        self.assertEqual(checkout_store2, checkout_store3)
        self.assertEqual(checkout_store3, checkout_store1)

        reservation_store1 = ReservationStore()
        reservation_store2 = ReservationStore()
        reservation_store3 = ReservationStore()

        self.assertEqual(reservation_store1, reservation_store2)
        self.assertEqual(reservation_store2, reservation_store3)
        self.assertEqual(reservation_store3, reservation_store1)

        dni_1 = IdCard("12345678Z")
        dni_2 = IdCard("12345678Z")

        self.assertNotEqual(dni_1, dni_2)

    if __name__ == '__main__':
        unittest.main()
