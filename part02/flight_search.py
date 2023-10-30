import requests
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]
AFFIL_ID = os.environ["AFFIL_ID"]
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

class FlightSearch:

  def get_destination_code(self, city_name):
     # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
    
    #step 3 - Get the IATA Codes sing the Kiwi Partners API
    # https://tequila-api.kiwi.com/v2/destinations?affili
    location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
    headers = {"apikey": TEQUILA_API_KEY,}
    query = {"term": city_name,"location_types": "city"}
    response = requests.get(location_endpoint, headers=headers, params=query)
    response.raise_for_status()
    result = response.json()["locations"]
    code = result[0]["code"]
    #step 2
    #code = "TESTING"
    return code
