import api_keys
import requests
from pprint import pprint

USERS_ENDPOINT = api_keys.USERS_ENDPOINT

AUTH = api_keys.AUTH
HEADERS = {'Authorization' : AUTH}

# sheet_response = requests.get(url=USERS_ENDPOINT, headers=HEADERS)
# sheet_response.raise_for_status()
# sheet_data = sheet_response.json()
# pprint(sheet_data['users'][0])

# First Name Column = sheet_data['users'][0]['firstName']
# Last Name Column = sheet_data['users'][0]['lastName']
# Email Column = sheet_data['users'][0]['email']

print("Welcome to Sebastian's Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What's your first name?\n")
last_name = input("What's your last name?\n")
email = input("What's your email?\n")
email_confirmation = input("Please type your email again.\n")

if email == email_confirmation:
    print("You're in the club!")
    new_data = {
        "user": {
            "firstName" : first_name,
            "lastName" : last_name,
            "email" : email
        }
    }
    response = requests.post(url=USERS_ENDPOINT, headers=HEADERS, json=new_data)
    response.raise_for_status()
    print(f"Sheet updated successfully!")