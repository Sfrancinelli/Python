from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from notification_manager import NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
sheet_data = data_manager.get_data()
# pprint(sheet_data)

# print(sheet_data[0]['city'])



count = 0

for _ in sheet_data:
    if sheet_data[count]['iataCode'] == '':
        city = sheet_data[count]['city']
        flight_search = FlightSearch(city)
        iata_code = flight_search.get_iata_code(city)
        # print(city)
        # print(iata_code)
        sheet_data[count]['iataCode'] = iata_code
        # print(city)
        # print(sheet_data[count]['iataCode'])
    count += 1

# pprint(sheet_data[0]['city'])
# pprint(sheet_data)

# This line is commented so it doesn't trigger more API Calls (limit is 200 per month)
# For the final code, the line below must be uncommented
# data_manager.edit_data()

flight_search = FlightSearch(sheet_data[0]['city'])

for destination in sheet_data:
    flights = flight_search.search_flight(destination['iataCode'])
    notification = NotificationManager()
    if flights.price < destination['lowestPrice']:
        notification.send_notification(price=flights.price, origin_city=flights.origin_city, origin_airport= flights.origin_airport, destination_city=flights.destination_city, destination_airport=flights.destination_airport, out_date=flights.out_date, return_date=flights.return_date)
    print("---------------------------------")



