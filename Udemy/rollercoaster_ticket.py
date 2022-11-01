print("Welcome to the rollercoaster ticket calculator!\nWe have a set of rules and prices:\nIf you are less than 120cm tall you can't ride :(\nTicket prices:\nUnder 12 years old: $5\nFrom 12 to 18 years old: $7\nOver 18 years old: $12\nAdd a photo for only $3!")
height = int(input("What's your height in cm?\n"))
age = int(input("How old are you?\n"))
bill = 0

if height > 120:
  if age < 12:
    bill += 5
    photo = input("Would you like a photo? Yes or no ")
  elif age < 18:
    bill += 7
    photo = input("Would you like a photo? Yes or no ")
  elif age >= 18:
    bill += 12
    photo = input("Would you like a photo? Yes or no ")
  if photo.upper() == "YES":
    bill += 3
    print(f"Your total bill is ${bill}. Enjoy the ride!")
  else:
    bill = bill
    print(f"Your total bill is ${bill}. Enjoy the ride!")
else:
  print("You can't ride until you grow up :c")
