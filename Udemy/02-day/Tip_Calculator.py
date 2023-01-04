print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
split = int(input("How many people to split the bill? "))

total_split =(total / split)

tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

percentage = tip * total_split /100

total_plus_tip = round(total_split + percentage , 2)

payment = print("Each person should pay: $" + str(total_plus_tip))