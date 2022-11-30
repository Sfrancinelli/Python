print("Welcome to the Band Name Generator!")
city_name = input("What's name of the city you grew up in?\n")
pet_name = input("What's the name of your pet?\n")
band_name = "Your band name could be " + city_name + " " + pet_name
print(band_name)

palabras = ["ANANA", "KIWI", "MANZANA"]

for valor in palabras:
    for char in valor:
        print(char)