# import csv

# with open("Udemy/25-day/weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
    
#     temperatures = []
    
#     for row in data:
#         # try:
#         #     temperatures.append(int(row[1]))
#         # except:
#         #     temperatures.append(row[1])
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data = pandas.read_csv("Udemy/25-day/weather_data.csv")

# print(data)
# print(data["temp"])

print(type(data)) # Data Frame (whole table)
print(type(data["temp"])) # Series (one column)

dict_data = data.to_dict()
print(dict_data)

temp_list = data["temp"].to_list()
print(temp_list)

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)

avg_temp = data["temp"].mean()

max_temp = data["temp"].max()
print(max_temp)

# Get data in colums
print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

# Get data in value 
monday = data[data.day == "Monday"]
monday_temp = monday.temp
print(monday_temp)
farenheit_temp = (monday.temp * 1.8) + 32
print(farenheit_temp)

# Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}
new_table = pandas.DataFrame(data_dict)
print(new_table)
new_table.to_csv("Udemy/25-day/new_table.csv")