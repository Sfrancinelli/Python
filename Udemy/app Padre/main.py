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
Día: {data['day']['1']['name']}
Temp. Mín: {data['day']['1']['tempmin']}
Temp. Máx: {data['day']['1']['tempmax']}
Alba: {data['day']['1']['sun']['in']}
Crepúsculo: {data['day']['1']['sun']['out']}
Vientos: 
    Velocidad:{data['day']['1']['wind']['speed']}km/h
Lluvia: {data['day']['1']['rain']}, si es 0, no llueve. Si es 1, llueve.
Humedad: {data['day']['1']['humidity']}%
Nubes: {data['day']['1']['clouds']}
Indice UV: {data['day']['1']['uv_index']}
"""


print(info)
