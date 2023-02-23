import requests
import api_keys
from pprint import pprint
from datetime import datetime, timedelta
from flight_data import FlightData

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        """This class is responsible for talking to the Flight Search API"""
        self.city = city
        self.iataCode = None
        self.API_KEY = api_keys.API_KEY
        self.API_END = api_keys.API_END
        self.flights = []

    def get_iata_code(self, city):
        """Gets the IATA Code of the city given by parameter via the Flight Search API and returns it as a string"""
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

    def search_flight(self, destination_city):
        """Requires a destination city IATA Code to work. 
        It searchs the lowest price flight available from tomorrow to six month and it checks for 7 to 28 nights in destination and the flight back.
        It's calculated in GBP currency"""

        tomorrow = datetime.now() + timedelta(hours=24)

        six_months = tomorrow + timedelta(days=180)

        headers = {"apikey" : self.API_KEY}

        params = {
                "fly_from" : "LON",
                "fly_to" : destination_city,
                "date_from" : tomorrow.strftime("%d/%m/%Y"),
                "date_to" : six_months.strftime("%d/%m/%Y"),
                "nights_in_dst_from" : 7,
                "nights_in_dst_to" : 28,
                "flight_type" : "round",
                "one_for_city" : 1,
                "max_stopovers" : 0,
                "curr" : "GBP",
            }


        response = requests.get(url="https://api.tequila.kiwi.com/v2/search", headers=headers, params=params)
        response.raise_for_status()
        try:
            data = response.json()['data'][0]
        except IndexError:

            params["max_stopovers"] = 1
            response = requests.get(
                url="https://api.tequila.kiwi.com/v2/search",
                headers=headers,
                params=params,
            )

            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination_city}")
            else:
                pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                return flight_data

        else:

            flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split("T")[0],
                return_date=data['route'][1]['local_departure'].split("T")[0]
            )

            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
        
            

