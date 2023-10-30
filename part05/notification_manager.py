from twilio.rest import Client
import os


TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
      self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message, from_number, to_number):
      message = self.client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
      )
      #prints if successfully sent.
      print(message.sid)
      print(message.status)