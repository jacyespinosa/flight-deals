import requests
from flight_data import FlightData
import datetime


KIWI_API = "INSERT KIWI API"
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search?"

header = {
    "apikey": KIWI_API
}

today = datetime.datetime.today()
next_6_months = datetime.datetime.now() + datetime.timedelta(days=6 * 30)
min_return_date = datetime.datetime.now() + datetime.timedelta(days=7)
max_return_date = datetime.datetime.now() + datetime.timedelta(days=28)

date_from = today.strftime("%d/%m/%Y")
date_to = next_6_months.strftime("%d/%m/%Y")
return_from = min_return_date.strftime("%d/%m/%Y")
return_to = max_return_date.strftime("%d/%m/%Y")


class FlightSearch:

    def get_iataCode(self, city):
        query = {"term": f"{city}", "location_types": "airport", }
        response = requests.get(url=KIWI_ENDPOINT, params=query, headers=header)
        result = response.json()['locations']
        return result[0]['code']


    def get_deals(self, fly_city_from, fly_city_to, date_from, date_to):
        query = {
            "fly_from": fly_city_from,
            "fly_to": fly_city_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }


        '''
        Catching Exceptions when there are no flights to certain destinations in the timeframe that you're searching in.
        '''
        response = requests.get(url=KIWI_SEARCH_ENDPOINT, params=query, headers=header)
        try:
            result = response.json()['data'][0]
        except IndexError:
            try:
                query["max_stopovers"] = 1
                response = requests.get(url=KIWI_SEARCH_ENDPOINT, params=query, headers=header)
                result = response.json()['data'][0]

                flight_info = FlightData(
                    price=result["price"],
                    departure_airport_code=result["route"][0]["flyFrom"],
                    departure_city=result["route"][0]["cityFrom"],
                    arrival_airport_code=result["route"][1]["flyTo"],
                    arrival_city=result["route"][1]["cityTo"],
                    fly_date=result["route"][0]["local_departure"].split("T")[0],
                    return_date=result["route"][2   ]["local_arrival"].split("T")[0],
                    stopovers=1,
                    via_city=result["route"][0]["cityTo"]
                )

                return flight_info
            except IndexError:
                return None

        else:
            flight_info = FlightData(
                price=result["price"],
                departure_airport_code=result["route"][0]["flyFrom"],
                departure_city=result["route"][0]["cityFrom"],
                arrival_airport_code=result["route"][0]["flyTo"],
                arrival_city=result["route"][0]["cityTo"],
                fly_date=result["route"][0]["local_departure"].split("T")[0],
                return_date=result["route"][1]["local_arrival"].split("T")[0],
            )

            return flight_info