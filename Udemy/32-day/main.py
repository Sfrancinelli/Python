##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib
import datetime as dt
import random
import pandas

PLACEHOLDER = "[NAME]"

dataframe = pandas.read_csv("Udemy/32-day/birthdays.csv")

birthdays = dataframe.to_dict(orient="records")

print(birthdays)

now = dt.datetime.now()
month = now.month
print(month)
day = now.day
print(day)

gmail_email = "pruebaprogramacion5773@gmail.com"
password_app_g = "jlcbzdoajvkrpsrq"
yahoo_email = "pruebaprogramacion99@yahoo.com"

names = []

print(birthdays[0]["month"])
count = 0
for _ in birthdays:
    names.append(birthdays[count]["name"])
    if month == birthdays[count]["month"] and day == birthdays[count]["day"]:
        random_num = random.randint(1,3)
        with open(f"Udemy/32-day/letter_templates/letter_{random_num}.txt") as letter:
            text = letter.read()
            new_mail = text.replace(PLACEHOLDER, birthdays[count]["name"])
            new_letter = open(f"Udemy/32-day/letter_templates/letter_{birthdays[count]['name']}.txt", "w")
            new_letter.write(new_mail)
            new_letter = open(f"Udemy/32-day/letter_templates/letter_{birthdays[count]['name']}.txt", "r")
            mail = new_letter.read()
        print(text)
        print(mail)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=gmail_email, password=password_app_g)
            connection.sendmail(from_addr=gmail_email, to_addrs=birthdays[count]['email'], msg=f"Subject:Happy Birthday!\n\n{mail}")

    count += 1

