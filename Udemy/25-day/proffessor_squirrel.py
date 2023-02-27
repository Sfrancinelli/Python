import pandas

# It could be done differently. Here it goes the proffesor take:

data = pandas.read_csv("Udemy/25-day/squirrel_count.csv")

gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])

red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_squirrels = data[data["Primary Fur Color"] == "Black"]
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)
