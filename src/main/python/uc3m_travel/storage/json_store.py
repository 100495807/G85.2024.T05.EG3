import json
from datetime import datetime
from uc3m_travel.hotel_management_exception import HotelManagementException
from uc3m_travel.hotel_management_config import JSON_FILES_PATH


class JsonStore():
    """Clase JsonStore"""
    def __init__(self):
        pass

    def write_json_file(self, data_list, file_store):
        try:
            with open(file_store, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as error:
            raise HotelManagementException("Wrong file  or file path") from error

    def load_json_file(self, file_store):
        try:
            with open(file_store, "r", encoding="utf-8", newline="") as file:
                data_list = json.load(file)
        except FileNotFoundError:
            data_list = []
        except json.JSONDecodeError as error:
            raise HotelManagementException("JSON Decode Error - Wrong JSON Format") from error
        return data_list

    def save_reservation(self, my_reservation):
        # escribo el fichero Json con todos los datos
        file_store = JSON_FILES_PATH + "store_reservation.json"
        # leo los datos del fichero si existe , y si no existe creo una lista vacia
        # se extrae el metodo para leer los archivos
        data_list = self.load_json_file(file_store)
        # compruebo que esta reserva no esta en la lista
        for item in data_list:
            if my_reservation.localizer == item["_HotelReservation__localizer"]:
                raise HotelManagementException("Reservation already exists")
            if my_reservation.id_card == item["_HotelReservation__id_card"]:
                raise HotelManagementException("This ID card has another reservation")
        # añado los datos de mi reserva a la lista , a lo que hubiera
        data_list.append(my_reservation.__dict__)
        # escribo la lista en el fichero
        # se extrae el metodo para escribir en los archivos
        self.write_json_file(data_list, file_store)


    def check_reservation(self, my_localizer):
        """check"""
        # buscar en almacen
        file_store = JSON_FILES_PATH + "store_reservation.json"
        # leo los datos del fichero , si no existe deber dar error porque el almacen de reservaa
        # debe existir para hacer el checkin
        store_list = self.load_json_file(file_store)
        reservation_credit_card = ""
        reservation_date_arrival = ""
        reservation_date_timestamp = ""
        reservation_days = ""
        reservation_id_card = ""
        reservation_name = ""
        reservation_phone = ""
        reservation_room_type = ""
        # compruebo si esa reserva esta en el almacen
        found = False
        for item in store_list:
            if my_localizer == item["_HotelReservation__localizer"]:
                reservation_days = item["_HotelReservation__num_days"]
                reservation_room_type = item["_HotelReservation__room_type"]
                reservation_date_timestamp = item["_HotelReservation__reservation_date"]
                reservation_credit_card = item["_HotelReservation__credit_card_number"]
                reservation_date_arrival = item["_HotelReservation__arrival"]
                reservation_name = item["_HotelReservation__name_surname"]
                reservation_phone = item["_HotelReservation__phone_number"]
                reservation_id_card = item["_HotelReservation__id_card"]
                found = True
        return found, reservation_credit_card, reservation_date_arrival, reservation_date_timestamp, reservation_days, reservation_id_card, reservation_name, reservation_phone, reservation_room_type

    def write_checkin(self, my_checkin):
        # Escribir el fichero JSON con todos los datos
        file_store = JSON_FILES_PATH + "store_check_in.json"
        # Leer los datos del fichero si existe, y si no, crear una lista vacía
        room_key_list = self.load_json_file(file_store)
        # Comprobar que no se haya hecho otro check-in antes
        for item in room_key_list:
            if my_checkin["room_key"] == item.get("_HotelStay__room_key"):
                raise HotelManagementException("Check-in already performed")
        # Añadir los datos de mi check-in a la lista
        room_key_list.append(my_checkin)
        print("Writing check-in data:", my_checkin)  # Depuración
        self.write_json_file(room_key_list, file_store)

    def check_checkin(self, room_key):
        file_store = JSON_FILES_PATH + "store_check_in.json"
        room_key_list = self.load_json_file(file_store)

        if not isinstance(room_key_list, list):
            raise HotelManagementException("Error: Invalid data format in check-in store")

        found = False
        departure_date_timestamp = None
        for item in room_key_list:
            if item["_HotelStay__room_key"] == room_key:
                departure_date_timestamp = item["_HotelStay__departure"]
                found = True
                break

        if not found:
            raise HotelManagementException("Error: room key not found")

        return departure_date_timestamp

    def write_checkout(self, room_key):
        file_store_checkout = JSON_FILES_PATH + "store_check_out.json"
        room_key_list = self.load_json_file(file_store_checkout)
        for checkout in room_key_list:
            if checkout["room_key"] == room_key:
                raise HotelManagementException("Guest is "
                                               "already out")
        room_checkout = {"room_key": room_key, "checkout_time": datetime.timestamp(datetime.utcnow())}
        room_key_list.append(room_checkout)
        self.write_json_file(room_key_list, file_store_checkout)


    def check_arrival(self, file_input):
        input_list = self.load_json_file(file_input)
        # comprobar valores del fichero
        try:
            my_localizer = input_list["Localizer"]
            my_id_card = input_list["IdCard"]
        except KeyError as error:
            raise HotelManagementException("Error - Invalid Key in JSON") from error
        return my_id_card, my_localizer