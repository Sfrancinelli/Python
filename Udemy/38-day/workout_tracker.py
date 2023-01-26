# x-app-id and x-app-key are required and need to be send as headers params.
# x-remote-user-id shoud be set to 0 right now.
import api_keys
import requests
import datetime

GENDER ="MALE"
WEIGHT_KG = "75.5"
HEIGHT = "181.1"
AGE = "22"

APP_ID = api_keys.APP_ID
API_KEY = api_keys.API_KEY

excercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

excercise_input = input("Tell me wich excercise you did today?: ")

header = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

params = {
    'query' : excercise_input,
    "gender" : GENDER,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT,
    "age" : AGE,
}

response = requests.post(url=excercise_endpoint, json=
                         params, headers=header)
response.raise_for_status()
data = response.json()
print(data)

SPREADSHEET_ENDPOINT = api_keys.SHEET_ENDPOINT

time_now = datetime.datetime.now()
print(time_now.strftime("%d/%m/%Y")) # Ej: 26/01/2023

try: 
    print(data['excercises'][0])
except:
    print("could not print value 0")
try:
    print(data['exercises'][1])
except:
    print("could not print value 1")