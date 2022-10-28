age = input("What is your current age?")

time_left = 90 - int(age)

months = time_left * 12

weeks = time_left * 52

days = time_left * 365

print ("You have " + str(days) + " days, " + str(weeks) + " weeks, and " + str(months) + " months left.")