import smtplib

yahoo_email = "pruebaprogramacion99@yahoo.com"
PASSWORD = "abcd1234()6789"
gmail_email = "pruebaprogramacion5773@gmail.com"
password_g = "abcd1234()"
password_app_g = "jlcbzdoajvkrpsrq"

with smtplib.SMTP("smtp.gmail.com") as connection:

# Start tls will secure our conection and encrypt the email during its journey
    connection.starttls()
    connection.login(user=gmail_email, password=password_app_g)
    connection.sendmail(from_addr=gmail_email, to_addrs=yahoo_email, msg="Subject:Hello\n\nThis is the body of my email")
# connection.close()