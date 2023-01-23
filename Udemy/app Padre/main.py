import requests
# from api_key import API_KEY, AUTH_TOKEN

# api_key = API_KEY

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

info = f"""
Buen día pa!
Información General:
Día: {data['day']['1']['name']}
Temp. Mín: {data['day']['1']['tempmin']}°C
Temp. Máx: {data['day']['1']['tempmax']}°C
Alba: {data['day']['1']['sun']['in']} hs
Crepúsculo: {data['day']['1']['sun']['out']} hs
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

print(data['day']['1']['hour'][0]['wind']['speed'])

print(info)
