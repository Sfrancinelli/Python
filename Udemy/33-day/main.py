import requests
from datetime import datetime

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# print(data["iss_position"])

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)

parameters = {
    "lat" : -34.641364,
    "lng" : -58.406247,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

time_now = datetime.now()

print(time_now.hour)
# print(sunrise, sunset)

# Get the hour alone from the response time. Splitting out the datetime.
splitted_sunrise = sunrise.split("T")[1].split(":")[0]
splitted_sunset = sunset.split("T")[1].split(":")[0]

print(splitted_sunrise, splitted_sunset)


