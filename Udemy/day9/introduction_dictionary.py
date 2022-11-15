programming_dictionary = {"Bug":"An error in a program that prevents the program fron running as expected.",
"Function":"A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over again.",}

# Retrieving items from dictionary.
print(programming_dictionary["Loop"])

# Adding new items to dictionary.
programming_dictionary["Dictionary"] = "Dictionaries are used to store data values in key:value pairs."

print(programming_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# Wipe an existing dictionary.
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting.
capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
}

# Nesting a List in a Dictionary.
travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a Dictionary in a Dictionary.
travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5}
}

# Nesting a Dictionary in a List.
travel_log = [
    {
        "country" : "France", 
        "cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12
    },
    {
        "country" : "Germany",
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5
    }
]

print(travel_log)