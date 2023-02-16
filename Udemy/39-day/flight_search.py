import requests
import api_keys
from pprint import pprint
from datetime import datetime, timedelta

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.iataCode = None
        self.API_KEY = api_keys.API_KEY
        self.API_END = api_keys.API_END
        self.flights = []

    def get_iata_code(self, city):
        if city != '':
            headers = {"apikey" : self.API_KEY}
            params = {"term" : city, "location_types" : "city"}
            response = requests.get(url=f"{self.API_END}locations/query", headers=headers, params=params)
            if response.status_code == 200:
                iata_code = response.json()["locations"][0]["code"]
                print(f"The IATA code for {city} is {iata_code}")
                return iata_code
            else:
                print(f"Error: {response.status_code} - {response.text}")
            # self.iataCode = "TESTING"
            # return self.iataCode

    def search_flight(self, data:list):

        tomorrow = datetime.now() + timedelta(hours=24)

        six_months = tomorrow + timedelta(days=180)

        headers = {"apikey" : self.API_KEY}

        for _ in data:
            count = 0
            params = {
                "fly_from" : "LON",
                "fly_to" : data[count]['iataCode'],
                "date_from" : tomorrow.strftime("%d%m%Y"),
                "date_to" : six_months.strftime("%d%m%Y"),
                "nights_in_dst_from" : 7,
                "nights_in_dst_to" : 28,
                "flight_type" : "round",
                "curr" : "GBP"
            }

            count += 1

            response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=headers, params=params)
            response.raise_for_status()
            flights = response.json()
            self.flights.append(flights)

        return self.flights
            
        
            

