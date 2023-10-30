#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
#from flight_data import FlightData
from part04.flight_search import FlightSearch
from part04.notification_manager import NotificationManager
# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from part04.data_manager import DataManager
import datetime as dt

# Instantiate the FlightData class
#flight_data = FlightData()
# Instantiate the NotificationManager class
notification_manager = NotificationManager()
data_manager = DataManager()
flight_search = FlightSearch()

def run():
  
  sheet_data = data_manager.get_destination_data()
  print(f"\n{sheet_data}")

  #  5. In main.py check if sheet_data contains any values for the "iataCode" key.
  #  If not, then the IATA Codes column is empty in the Google Sheet.
  #  In this case, pass each city name in sheet_data one-by-one
  #  to the FlightSearch class to get the corresponding IATA code
  #  for that city using the Flight Search API.
  #  You should use the code you get back to update the sheet_data dictionary.
  if sheet_data[0]["iataCode"] == "":
      #step 3 - Get the IATA Codes sing the Kiwi Partners API
      for row in sheet_data:
          row["iataCode"] = flight_search.get_destination_code(row["city"])
      #print(f"sheet_data:\n {sheet_data}")
      data_manager.destination_data = sheet_data
      data_manager.update_destination_codes()
  
  tomorrow = dt.datetime.now() + dt.timedelta(days=1)
  six_months_from_today = dt.datetime.now() + dt.timedelta(days=(6 * 30))
  
  # 6. Pass the sheet_data dictionary to the FlightSearch class to get the flight data for the next six months.
  #  You should use the code you get back to update the sheet_data dictionary.
  for destination in sheet_data:
    flight = flight_search.check_flights(
      "LIS",
      destination["iataCode"],
      from_time=tomorrow,
      to_time=six_months_from_today
    )
      