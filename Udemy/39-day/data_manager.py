from pprint import pprint
import api_keys
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEET_ENDPOINT = api_keys.SHEET_ENDPOINT
        self.AUTH_STR = api_keys.AUTH
        self.HEADERS = {'Authorization' : self.AUTH_STR}

    def get_data(self):
        sheet_response = requests.get(url=self.SHEET_ENDPOINT, headers=self.HEADERS)
        sheet_response.raise_for_status()
        sheet_data = sheet_response.json()
        return sheet_data['prices']
    
    def edit_data(self, row, column, value):
        data = {
            "prices" : {
            column : value
            }
        }
        response = requests.put(url=f"{self.SHEET_ENDPOINT}/{row}", headers=self.HEADERS, json=data)
        response.raise_for_status()
        print(f"Row {row} updated successfully!")

if __name__ == "__main__":
    data_manager = DataManager()
    data_manager.get_data()