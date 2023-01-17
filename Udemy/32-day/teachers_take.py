from datetime import datetime
import pandas
import random
import smtplib

gmail_email = "pruebaprogramacion5773@gmail.com"
password_app_g = "jlcbzdoajvkrpsrq"
yahoo_email = "pruebaprogramacion99@yahoo.com"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("Udemy/32-day/birthdays.csv")

# new_dict = {new_key : new_value for (index, data_row) in data.iterrows()}

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"Udemy/32-day/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(gmail_email, password_app_g)
        connection.sendmail(from_addr=gmail_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{contents}")