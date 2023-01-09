import pandas

data_csv = pandas.read_csv("Udemy/25-day/squirrel_count.csv")

data = data_csv.to_dict()

fur_color = data["Primary Fur Color"]

cinnamon_count = 0

black_count = 0

gray_count = 0

for count in fur_color:
    if fur_color[count] == "Cinnamon":
        cinnamon_count += 1
    elif fur_color[count] == "Gray":
        gray_count += 1
    elif fur_color[count] == "Black":
        black_count += 1

print(cinnamon_count)
print(gray_count)
print(black_count)

data_table = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_count, cinnamon_count, black_count]
}

census_data = pandas.DataFrame(data_table)
print(census_data)
squirrel_census_data = census_data.to_csv("Udemy/25-day/squirrel_census_data.csv")


