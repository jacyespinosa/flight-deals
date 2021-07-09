from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
sheety_data = data.get_data()

flight = FlightSearch()

"""
Checking if sheety_data contains any values for the "iataCode" key. If not, then the IATA Codes column is empty in the 
Google Sheet. Pass each city name in sheet_data one-by-one to the FlightSearch class to get the corresponding IATA code
 for that city using the Flight Search API. Must use the code you get back to update the sheet_data dictionary.. 
"""
if sheety_data[0]['iataCode'] == '':
    for item in sheety_data:
        item['iataCode'] = flight.get_destination_code(item['city'])

data.update_rows()