import requests
from datetime import datetime
import smtplib

MY_LAT = -34.641364 # Your latitude
MY_LONG = -58.406247 # Your longitude

def get_iss_pos():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return (iss_latitude, iss_longitude)

iss_data = get_iss_pos()

iss_lat = iss_data[0]
iss_lng = iss_data[1]

def compare_pos():
    global MY_LAT, MY_LONG, iss_lat, iss_lng

    if MY_LAT == iss_lat or MY_LAT < iss_lat + 5 and MY_LAT > iss_lat - 5:
        if MY_LONG == iss_lng or MY_LONG < iss_lng + 5 and MY_LONG > iss_lng - 5:
            return True
        else:
            return False
    else:
        return False

position = compare_pos()

print(position)

# Your position is within +5 or -5 degrees of the ISS position.

print(iss_lat, iss_lng)

def get_sun():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    return data

sun_data = (get_sun())

sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = datetime.now()

if time_now.hour > 22 and position:
    gmail_email = "pruebaprogramacion5773@gmail.com"
    password_app_g = "jlcbzdoajvkrpsrq"
    yahoo_email = "pruebaprogramacion99@yahoo.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=gmail_email, password=password_app_g)
        connection.sendmail(from_addr=gmail_email,
        to_addrs=gmail_email, msg="Subject:Look for the stars!\n\nThe ISS satelite is passing right now above your head! Look up and watch it!")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



