from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
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
        item['iataCode'] = flight.get_iataCode(item['city'])

data.update_rows()

for city in sheety_data:
    deals = flight.get_deals(fly_city_from="SFO", fly_city_to=city["iataCode"], date_from=date_from, date_to=date_to)

    if deals is None:
        print(f"There is no direct flights or 1 stop over flights available from SFO to {city['city']}.")
        continue

    '''
    Check if any of the flights found are cheaper than the Lowest Price listed in the Google Sheet. If so, then use the 
    Twilio API to send an SMS with enough information to book the flight. You should use the NotificationManager for 
    this job.
    '''
    if deals.price < city['lowestPrice']:
        notify = NotificationManager()

        message = f"Subject:LOW FLIGHTS ALERT!\n\nLOW PRICE ALERT: Only ${deals.price} from " \
                  f"{deals.departure_city}-{deals.departure_airport_code} to" \
                  f"{deals.arrival_city}-{deals.arrival_airport_code} on {deals.fly_date} to {deals.return_date}.\n\n" \
                  f"https://www.google.com/travel/flights/search?hl=en#flt=" \
                  f"{deals.departure_airport_code}.{deals.arrival_airport_code}.{deals.fly_date}*" \
                  f"{deals.arrival_airport_code}.{deals.departure_airport_code}.{deals.return_date}\n\n"

        if deals.stopovers == 1:
            message += f"There is 1 stopover, via {deals.via_city}"
            notify.send_email(message)
        else:
            notify.send_email(message)