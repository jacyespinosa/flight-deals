# flight-deals

- FlightSearch Class and Sheety API are used to populate a copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. 
- By using the FlightSearch API, I can check the cheapest flights for all the cities listed in the Google Sheet.

- If the price is lower than the lowest price listed in the Google Sheet, then using Twilio API, I send an SMS with the help of the NotificationManager Class.
- The NotificationManager will send an SMS that includes the departure airport IATA code, destination airport IATA code, departure city, destination city,
  flight price and flight dates. e.g.
