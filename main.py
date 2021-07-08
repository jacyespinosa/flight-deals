from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
sheety_data = data.get_data()

flight = FlightSearch()

"""
Checking if sheety_data contains any values for the "iataCode" key. If not, then the IATA Codes column is empty in the 
Google Sheet. In this case, instead of passing each city name in sheety_data one-by-one to the FlightSearch class, 
the FlightSearch class will respond with "TESTING" instead of a real IATA code. 
"""
if sheety_data[0]['iataCode'] == '':
    for item in sheety_data:
        item['iataCode'] = flight.get_destination_code(item['city'])

data.update_rows()