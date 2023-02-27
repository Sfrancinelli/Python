from flight_data import FlightData
from twilio.rest import Client
import api_keys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import api_keys
import requests

class NotificationManager:

    def __init__(self):
        """This class is responsible for sending notifications with the deal flight details."""
        self.ACCOUNT_SID = api_keys.ACCOUNT_SID
        self.AUTH_TOKEN = api_keys.AUTH_TOKEN
        self.EMAIL_SENDER = api_keys.EMAIL_SENDER
        self.EMAIL_PASSWORD = api_keys.EMAIL_PASSWORD
        self.USERS_ENDPOINT = api_keys.USERS_ENDPOINT
        self.AUTH = api_keys.AUTH
        self.HEADERS = {'Authorization' : self.AUTH}

    def send_notification(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, stop_overs=0, via_city=""):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN,)
        
        if stop_overs == 0 and via_city == "":
            message = client.messages.create(body=f"Low price alert! Only £{price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport}, from {out_date} to {return_date}.",
                                            from_='+16018846323', 
                                            to="+54 11 3704 2581")

            print(message.status)

        else:
            message = client.messages.create(body=f"Low price alert! Only £{price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport}, from {out_date} to {return_date}.\nFlight has {stop_overs} stop over, via {via_city}",
                                            from_='+16018846323', 
                                            to="+54 11 3704 2581")
            
    def send_email(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, flight_link):

        EMAIL_SENDER = self.EMAIL_SENDER
        email_receiver = ''
        EMAIL_SUBJECT = 'New Low Price Flight Founded!'
        email_message = f"Low price alert! Only £{price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport}, from {out_date} to {return_date}."
        EMAIL_PASSWORD = self.EMAIL_PASSWORD

        with smtplib.SMTP("smtp.gmail.com") as connection:

            sheet_response = requests.get(url=self.USERS_ENDPOINT, headers=self.HEADERS)
            sheet_response.raise_for_status()
            sheet_data = sheet_response.json()

            for user in sheet_data['users']:
                
                print(user['email'])
                email_receiver = user['email']

                connection.starttls()
                connection.login(user=EMAIL_SENDER, password=EMAIL_PASSWORD)
                connection.sendmail(from_addr=EMAIL_SENDER,
                to_addrs=email_receiver, msg=f"Subject:{EMAIL_SUBJECT}\n\n{email_message}\n{flight_link}.".encode('utf-8'))
