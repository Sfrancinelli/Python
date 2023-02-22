from flight_data import FlightData
from twilio.rest import Client
import api_keys

class NotificationManager:

    def __init__(self):
        """This class is responsible for sending notifications with the deal flight details."""
        self.ACCOUNT_SID = api_keys.ACCOUNT_SID
        self.AUTH_TOKEN = api_keys.AUTH_TOKEN

    def send_notification(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        client = Client(self.ACCOUNT_SID, self.AUTH_TOKEN,)
        message = client.messages.create(body=f"Low price alert! Only £{price} to fly from {origin_city}-{origin_airport} to {destination_city}-{destination_airport}, from {out_date} to {return_date}.",
                                         from_='+16018846323', 
                                         to="+54 11 3704 2581")

        print(message.status)