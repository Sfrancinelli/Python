import requests
from api_key import API_KEY, ACCOUNT_SID, AUTH_TOKEN
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")

auth_token = os.environ.get("AUTH_TOKEN")

print(api_key)

parameters = {
    "lat" : -34.641364,
    "lon" : -58.406247,
    "exclude" : "current,minutely,daily",
    "appid" : api_key,
    "units" : "metric",
}

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)

response.raise_for_status()

data = response.json()

# print(data['list'][0]['weather'])
# print(data['list'][1]['weather'])
# print(data['list'][0]['weather'][0]['id'])

count = 0

# My way of doing it
for _ in range(0,13):
    if data['list'][count]['weather'][0]['id'] <= 700:
        print("Bring an umbrella")
    count += 1

# Another way of doing it
will_rain = False

weather_slice = data['list'][:12]

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body="It's going to rain today. Remember to bring an umbrella",from_='+16018846323', to="+54 11 3704 2581")
    print("Bring an umbrella.")

    print(message.status)