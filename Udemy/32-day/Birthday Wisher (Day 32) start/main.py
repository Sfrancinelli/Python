import smtplib
import datetime as dt
import random 

# yahoo_email = "pruebaprogramacion99@yahoo.com"
# PASSWORD = "abcd1234()6789"
# gmail_email = "pruebaprogramacion5773@gmail.com"
# password_g = "abcd1234()"
# password_app_g = "jlcbzdoajvkrpsrq"

# with smtplib.SMTP("smtp.gmail.com") as connection:

# # Start tls will secure our conection and encrypt the email during its journey
#     connection.starttls()
#     connection.login(user=gmail_email, password=password_app_g)
#     connection.sendmail(from_addr=gmail_email, to_addrs=yahoo_email, msg="Subject:Hello/n/nThis is the body of my email")
# # connection.close()

# now = dt.datetime.now()
# print(now)
# year = now.year
# print(year)
# month = now.month
# print(month)
# day_of_week = now.weekday()
# print(day_of_week) # Computers count from 0, so 0 is monday, 1 tuesday, etc..
# date_of_birth = dt.datetime(year= 2000, month= 12, day=10, hour=4)
# print(date_of_birth)

with open("Udemy/32-day/Birthday Wisher (Day 32) start/quotes.txt") as quotes:
    q_list = quotes.readlines()
    print(q_list)

    now = dt.datetime.now()
    today = now.weekday()

    gmail_email = "pruebaprogramacion5773@gmail.com"
    password_app_g = "jlcbzdoajvkrpsrq"
    yahoo_email = "pruebaprogramacion99@yahoo.com"

    if today == 1:
        random_quote = random.choice(q_list)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=gmail_email, password=password_app_g)
            connection.sendmail(from_addr=gmail_email, to_addrs=yahoo_email, msg=f"Subject:Motivation\n\n{random_quote}")
