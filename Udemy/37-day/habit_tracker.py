from user_creation import pixela_endpoint, mi_endpoint, USER, TOKEN
import requests
from datetime import datetime

GRAPH_ID = "graph1"

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_adding_end = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Walking Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

time_now = datetime.now()
print(time_now.strftime("%Y%m%d"))

yesterday = datetime(year=2023, month=1, day=25)

graph_values = {
    "date" : yesterday.strftime("%Y%m%d"),
    "quantity" : "17.4"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

response = requests.post(url=graph_adding_end, json=graph_values, headers=headers)

print(response.text)


