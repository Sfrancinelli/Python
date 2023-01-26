from user_creation import pixela_endpoint, mi_endpoint, USER, TOKEN
import requests

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

graph_values = {
    "date" : "20230126",
    "quantity" : "10"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

response = requests.post(url=graph_adding_end, json=graph_values, headers=headers)

print(response.text)


