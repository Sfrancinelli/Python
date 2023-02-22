import api_keys
import requests
from pprint import pprint

USERS_ENDPOINT = api_keys.USERS_ENDPOINT

AUTH = api_keys.AUTH
headers = {'Authorization' : AUTH}

sheet_response = requests.get(url=USERS_ENDPOINT, headers=headers)
sheet_response.raise_for_status()
sheet_data = sheet_response.json()
pprint(sheet_data['users'][0])