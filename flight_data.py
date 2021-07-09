'''
FlightData class represents the flight data. e.g. price, departure_airport_code, departure_city_code and etc.
'''


class FlightData:
  def __init__(self, price, departure_airport_code, departure_city, arrival_airport_code, arrival_city, fly_date, return_date,
               stopovers=0, via_city=""):
    self.price = price
    self.departure_airport_code = departure_airport_code
    self.departure_city = departure_city
    self.arrival_airport_code = arrival_airport_code
    self.arrival_city = arrival_city
    self.fly_date = fly_date
    self.return_date = return_date
    self.stopovers = stopovers
    self.via_city = via_city