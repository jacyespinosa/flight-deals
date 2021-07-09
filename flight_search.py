import requests

KIWI_API = "INSERT KIWI API"
KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search?"

header = {
    "apikey": KIWI_API
}


class FlightSearch:

    def get_iataCode(self, city):
        query = {"term": f"{city}", "location_types": "airport", }
        response = requests.get(url=KIWI_ENDPOINT, params=query, headers=header)
        result = response.json()['locations']
        return result[0]['code']