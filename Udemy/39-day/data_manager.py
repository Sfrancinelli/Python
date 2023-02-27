from pprint import pprint
import api_keys
import requests

class DataManager:
    """This class is responsible for talking to the Google Sheet"""
    def __init__(self):
        self.SHEET_ENDPOINT = api_keys.SHEET_ENDPOINT
        self.AUTH_STR = api_keys.AUTH
        self.HEADERS = {'Authorization' : self.AUTH_STR}
        self.destination_data = {}

    def get_data(self):
        """This function gets the information of the Google Sheet and returns it on a list"""
        sheet_response = requests.get(url=self.SHEET_ENDPOINT, headers=self.HEADERS)
        sheet_response.raise_for_status()
        sheet_data = sheet_response.json()
        self.destination_data = sheet_data['prices']
        return self.destination_data
    
    def edit_data(self):
        """This function gets the updated IATA Codes from the destination data list and passes it to the Google Sheet via PUT request"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"https://api.sheety.co/ae3f72ea4b144b074aefb4c47de6eff8/flightDeals/prices/{city['id']}", headers=self.HEADERS, json=new_data)
            response.raise_for_status()
            print(f"Row {city['id']} updated successfully!")

if __name__ == "__main__":
    data_manager = DataManager()
    data_manager.get_data()