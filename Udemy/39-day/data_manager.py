from pprint import pprint
import api_keys
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEET_ENDPOINT = api_keys.SHEET_ENDPOINT
        self.AUTH_STR = api_keys.AUTH

    def get_data(self):
        headers = {'Authorization' : self.AUTH_STR}
        sheet_response = requests.get(url=self.SHEET_ENDPOINT, headers=headers)
        sheet_response.raise_for_status()
        sheet_data = sheet_response.json()
        return sheet_data['prices']

if __name__ == "__main__":
    data_manager = DataManager()
    data_manager.get_data()