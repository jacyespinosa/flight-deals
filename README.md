# flight-deals
GOING SOMEWHERE? WANT TO SAVE MONEY? TIRED OF CHECKING AIRLINE/TRAVEL AGENCY WEBSITES?
GET NOTIFIED WHENEVER THERE IS A FLIGHT DEAL!


APIs Required
-Google Sheet Data Management - https://sheety.co/

-Kiwi Partners Flight Search API (Free Signup, Requires Credit Card Details) - https://partners.kiwi.com/

-Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

-Twilio SMS API - https://www.twilio.com/docs/sms


- Create a new Google Sheet with the desired destination cities and target price (lowest price). I used Sheety API in order to GET 
  all the data from my Google Sheet.
<img width="351" alt="image" src="https://user-images.githubusercontent.com/80412098/125152667-fe71ff00-e102-11eb-8309-63a22681aac4.png">

- FlightSearch Class and Sheety API are used to populate a copy of the Google Sheet with International Air Transport Association (IATA) codes for each city using    the Tequila Flight Search API Documentation. 
<img width="343" alt="image" src="https://user-images.githubusercontent.com/80412098/125152457-82c38280-e101-11eb-9f49-5293ea21c27e.png">

- By using the FlightSearch API, I can check the cheapest flights for all the cities listed in the Google Sheet using the Tequila Flight Search API Documentation. 
<img width="362" alt="Screen Shot 2021-07-09 at 10 02 08 PM" src="https://user-images.githubusercontent.com/80412098/125152439-658eb400-e101-11eb-9711-663c15b5bd3c.png">

- If the price is lower than the lowest price listed in the Google Sheet, then using Twilio API, I send an SMS with the help of the NotificationManager Class.
<img width="931" alt="image" src="https://user-images.githubusercontent.com/80412098/125152697-27928f80-e103-11eb-819b-1c16e229c1f3.png">

- The NotificationManager will send an SMS that includes the departure airport IATA code, destination airport IATA code, departure city, destination city,
  flight price and flight dates. e.g.
  <img width="839" alt="image" src="https://user-images.githubusercontent.com/80412098/125152587-48a6b080-e102-11eb-8de8-4b7300fdc7b9.png">

