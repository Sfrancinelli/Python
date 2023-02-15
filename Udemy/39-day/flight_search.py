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
            pass
            # self.iataCode = "TESTING"
            # return self.iataCode
