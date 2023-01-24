import requests
import smtplib
import os
import datetime
# from api_key import API_KEY, AUTH_TOKEN

# api_key = API_KEY

gmail_email = os.environ['GMAIL_EMAIL']
password_app_g = os.environ['PASS_G']
destiny = os.environ['DESTINO_G']

print(gmail_email)
print(password_app_g)
print(destiny)

# parameters = {
#     "lat" : -56.693780,
#     "lon" : -36.506100,
#     "exclude" : "current,minutely,hourly,alerts",
#     "appid" : api_key,
#     "units" : "metric",
# }

# url = f'https://api.openweathermap.org/data/2.5/forecast'

# response = requests.get(url, params=parameters)

# response.raise_for_status()

# data = response.json()

# print(data['list'])

# # print(f"Tides: {data['tides']}")
# # print(f"Winds: {data['winds']}")
# # print(f"Temperature: {data['temperature']}")
# # print(f"Rain: {data['rain']}")
# # print(f"Humidity: {data['humidity']}")

url = "https://api.meteored.com.ar/index.php?api_lang=ar&localidad=322233&affiliate_id=1b74vmv8apgk&v=3.0"

response = requests.get(url)

response.raise_for_status()

data = response.json()

# print(data['day']['1'])

endpoint = "https://www.worldtides.info/api"
tides_key = os.environ['TIDES_KEY']
lat = -36.506100
lon = -56.693779

respuesta = requests.get(endpoint, params={
    "key" : tides_key,
    "lat" : lat,
    "lon" : lon,
    "heights" : True
})

tide_data = respuesta.json()

tides = tide_data['heights']

for tide in tides:
    height = tide['height']
    date = datetime.datetime.fromtimestamp(tide['date'])
    print(f"Tide height {height} at: {date}")

info = f"""
Buen dia pa!
Informacion General:
Dia: {data['day']['1']['name']}
Temp. Min: {data['day']['1']['tempmin']} grados
Temp. Max: {data['day']['1']['tempmax']} grados
Alba: {data['day']['1']['sun']['in']} hs
Crepusculo: {data['day']['1']['sun']['out']} hs
----------------------------------------------------
Intervalo 1:
    Hora: {data['day']['1']['hour'][0]['interval']}
Vientos:
    Velocidad: {data['day']['1']['hour'][0]['wind']['speed']}km/h
    Direccion: {data['day']['1']['hour'][0]['wind']['dir']}
Lluvia: {data['day']['1']['hour'][0]['rain']}. (Si es 0, no llueve. Si es 1, llueve.)
Humedad: {data['day']['1']['hour'][0]['humidity']}%
Nubes: {data['day']['1']['hour'][0]['clouds']}
Indice UV: {data['day']['1']['hour'][0]['uv_index']}
----------------------------------------------------
Intervalo 2:
    Hora: {data['day']['1']['hour'][1]['interval']}
Vientos:
    Velocidad: {data['day']['1']['hour'][1]['wind']['speed']}km/h
    Direccion: {data['day']['1']['hour'][1]['wind']['dir']}
Lluvia: {data['day']['1']['hour'][1]['rain']}. (Si es 0, no llueve. Si es 1, llueve.)
Humedad: {data['day']['1']['hour'][1]['humidity']}%
Nubes: {data['day']['1']['hour'][1]['clouds']}
Indice UV: {data['day']['1']['hour'][1]['uv_index']}
----------------------------------------------------
Intervalo 3:
    Hora: {data['day']['1']['hour'][2]['interval']}
Vientos:
    Velocidad: {data['day']['1']['hour'][2]['wind']['speed']}km/h
    Direccion: {data['day']['1']['hour'][2]['wind']['dir']}
Lluvia: {data['day']['1']['hour'][2]['rain']}. (Si es 0, no llueve. Si es 1, llueve.)
Humedad: {data['day']['1']['hour'][2]['humidity']}%
Nubes: {data['day']['1']['hour'][2]['clouds']}
Indice UV: {data['day']['1']['hour'][2]['uv_index']}
----------------------------------------------------
Intervalo 4:
    Hora: {data['day']['1']['hour'][3]['interval']}
Vientos:
    Velocidad: {data['day']['1']['hour'][3]['wind']['speed']}km/h
    Direccion: {data['day']['1']['hour'][3]['wind']['dir']}
Lluvia: {data['day']['1']['hour'][3]['rain']}. (Si es 0, no llueve. Si es 1, llueve.)
Humedad: {data['day']['1']['hour'][3]['humidity']}%
Nubes: {data['day']['1']['hour'][3]['clouds']}
Indice UV: {data['day']['1']['hour'][3]['uv_index']}
----------------------------------------------------
Intervalo 5:
    Hora: {data['day']['1']['hour'][4]['interval']}
Vientos:
    Velocidad: {data['day']['1']['hour'][4]['wind']['speed']}km/h
    Direccion: {data['day']['1']['hour'][4]['wind']['dir']}
Lluvia: {data['day']['1']['hour'][4]['rain']}. (Si es 0, no llueve. Si es 1, llueve.)
Humedad: {data['day']['1']['hour'][4]['humidity']}%
Nubes: {data['day']['1']['hour'][4]['clouds']}
Indice UV: {data['day']['1']['hour'][4]['uv_index']}
----------------------------------------------------
Intervalo 6:
    Hora: {data['day']['1']['hour'][5]['interval']}
Vientos:
    Velocidad: {data['day']['1']['hour'][5]['wind']['speed']}km/h
    Direccion: {data['day']['1']['hour'][5]['wind']['dir']}
Lluvia: {data['day']['1']['hour'][5]['rain']}. (Si es 0, no llueve. Si es 1, llueve.)
Humedad: {data['day']['1']['hour'][5]['humidity']}%
Nubes: {data['day']['1']['hour'][5]['clouds']}
Indice UV: {data['day']['1']['hour'][5]['uv_index']}
----------------------------------------------------
Intervalo 7:
    Hora: {data['day']['1']['hour'][6]['interval']}
Vientos:
    Velocidad: {data['day']['1']['hour'][6]['wind']['speed']}km/h
    Direccion: {data['day']['1']['hour'][6]['wind']['dir']}
Lluvia: {data['day']['1']['hour'][6]['rain']}. (Si es 0, no llueve. Si es 1, llueve.)
Humedad: {data['day']['1']['hour'][6]['humidity']}%
Nubes: {data['day']['1']['hour'][6]['clouds']}
Indice UV: {data['day']['1']['hour'][6]['uv_index']}
----------------------------------------------------
Intervalo 7:
    Hora: {data['day']['1']['hour'][7]['interval']}
Vientos:
    Velocidad: {data['day']['1']['hour'][7]['wind']['speed']}km/h
    Direccion: {data['day']['1']['hour'][7]['wind']['dir']}
Lluvia: {data['day']['1']['hour'][7]['rain']}. (Si es 0, no llueve. Si es 1, llueve.)
Humedad: {data['day']['1']['hour'][7]['humidity']}%
Nubes: {data['day']['1']['hour'][7]['clouds']}
Indice UV: {data['day']['1']['hour'][7]['uv_index']}
"""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=gmail_email, password=password_app_g)
#     connection.sendmail(from_addr=gmail_email,
#     to_addrs=destiny, msg=f"Subject:Clima\n\n{info}")

# print(data['day']['1']['hour'][0]['wind']['speed'])

# print(info)
