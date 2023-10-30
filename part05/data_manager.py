import requests
import os
from pprint import pprint
#STEP 2
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/041bc237af12575deefd9d8f485daa6f/flightDeals/prices"
SHEETY_API_KEY = os.environ["SHEETY_API_KEY"]
SHEETY_APP_ID = os.environ["SHEETY_APP_ID"]

HEADERS = {
  "Authorization": f"Bearer {SHEETY_API_KEY}",
  "Content-Type": "application/json"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

  
    def get_destination_data(self):
      # 2. Use the Sheety API to GET all the data in that sheet and print it out.
          response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADERS)
          data = response.json()
          self.destination_data = data["prices"]
          # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
          #pprint(data["prices"])
          return self.destination_data

      # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
      # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
          for city in self.destination_data:
              new_data = {
                  "price": {
                      "iataCode": city["iataCode"]
                  }
              }
              response = requests.put(
                  url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                  json=new_data,
                headers=HEADERS
              )
              pprint(response.text)
