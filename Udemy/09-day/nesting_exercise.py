travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country,visits,cities):
    travel_log.append({"country" : country, "visits" : visits, "cities" : cities})

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Looping all the way to get to the values of the dictionary inside the travel_log list:
for dictionary in travel_log:
    print(dictionary)
    for key in dictionary:
        print(key)
        print(dictionary[key])