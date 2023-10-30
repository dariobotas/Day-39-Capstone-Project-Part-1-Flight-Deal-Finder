import requests
import os
from part04.flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
AFFIL_ID = os.environ["AFFIL_ID"]


class FlightSearch:

  def get_destination_code(self, city_name):
    # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.

    #step 3 - Get the IATA Codes sing the Kiwi Partners API
    # https://tequila-api.kiwi.com/v2/destinations?affili
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    headers = {
      "apikey": TEQUILA_API_KEY,
    }
    query = {"term": city_name, "location_types": "city"}
    response = requests.get(location_endpoint, headers=headers, params=query)
    response.raise_for_status()
    result = response.json()["locations"]
    code = result[0]["code"]
    #step 2
    #code = "TESTING"
    return code

  def check_flights(self, origin_city_code, destination_city_code, from_time,
                    to_time):
    #step 4
    # https://tequila-api.kiwi.com/v2/search?affiliate_id=AFFIL_ID&origin=ORI&destination=DEST&from_date=FROM&to_date=TO
    search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
    headers = {
      "apikey": TEQUILA_API_KEY,
    }
    query = {
      "fly_from": origin_city_code,
      "fly_to": destination_city_code,
      "date_from": from_time.strftime("%d/%m/%Y"),
      "date_to": to_time.strftime("%d/%m/%Y"),
      "nights_in_dst_from": 7,
      "nights_in_dst_to": 28,
      "flight_type": "round",
      "one_for_city": 1,
      "max_stopovers": 0,
      "curr": "EUR"
    }
    response = requests.get(search_endpoint, headers=headers, params=query)
    response.raise_for_status()

    #print(response.json())
    try:
      data = response.json()["data"][0]
      print(data["price"])
    except IndexError:
      print(f"No flights found between {origin_city_code} and {destination_city_code}.")
      return None
    else:
      flight_data = FlightData(
        price=data["price"],
        origin_city=data["route"][0]["cityFrom"],
        origin_airport=data["route"][0]["flyFrom"],
        destination_city=data["route"][0]["cityTo"],
        destination_airport=data["route"][0]["flyTo"],
        out_date=data["route"][0]["local_departure"].split("T")[0],
        return_date=data["route"][1]["local_departure"].split("T")[0]
      )
      print(f"{flight_data.arrival_city}: {flight_data.price}€")
      return flight_data
