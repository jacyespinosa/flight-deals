import requests

SHEETY_ENDPOINT = "INSERT YOUR API HERE"

"""
I USED GOOGLE SHEET TO ADD MY DATA SPECIFICALLY THE CITIES THAT I AM INTERESTED IN TRAVELLING. THEN I CREATED
 A NEW PROJECT ON SHEETY API (COPIED THE GOOGLE SHEET). THEN I REQUESTED TO GET ALL THE DATA FROM GOOGLE SHEET USING
 SHEETY API.
"""
class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination = data["prices"]
        return self.destination

    '''
    Make a PUT request and use the row id from sheet_data to update the Google Sheet with the IATA codes. 
    '''
    def update_rows(self):
        for city in self.destination:
            updated_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=updated_data)

