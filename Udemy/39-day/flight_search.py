import requests
import api_keys
from pprint import pprint

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.iataCode = None
        self.API_KEY = api_keys.API_KEY
        self.API_END = api_keys.API_END

    def get_iata_code(self, city):
        if city != '':
            headers = {"apikey" : self.API_KEY}
            params = {"term" : city, "location_types" : "city"}
            response = requests.get(url=f"{self.API_END}locations/query", headers=headers, params=params)
            if response.status_code == 200:
                iata_code = response.json()["locations"][0]["code"]
                print(f"The IATA code for {city} is {iata_code}")
            else:
                print(f"Error: {response.status_code} - {response.text}")
            # self.iataCode = "TESTING"
            # return self.iataCode
