from data_manager import DataManager
from flight_search import FlightSearch
import datetime

today = datetime.datetime.today()
next_6_months = datetime.datetime.now() + datetime.timedelta(days = 6*30)
min_return_date = datetime.datetime.now() + datetime.timedelta(days = 7)
max_return_date = datetime.datetime.now() + datetime.timedelta(days = 28)

date_from = today.strftime("%d/%m/%Y")
date_to = next_6_months.strftime("%d/%m/%Y")
return_from = min_return_date.strftime("%d/%m/%Y")
return_to = max_return_date.strftime("%d/%m/%Y")


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

for city in sheety_data:
    deals = flight.get_deals(fly_city_from="SFO", fly_city_to=city["iataCode"], date_from=date_from, date_to=date_to)