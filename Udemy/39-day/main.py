from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
sheet_data = data_manager.get_data()
pprint(sheet_data)

print(sheet_data['prices'][0]['city'])

count = 0

for code in sheet_data['prices'][count]['iataCode']:
    if code == '':
        flight_search = FlightSearch(sheet_data['prices'][count]['city'])
        iata_code = flight_search.get_iata_code()
        pass
