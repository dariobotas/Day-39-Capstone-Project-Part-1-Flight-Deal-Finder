class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
      self.price = price
      self.departure_airport = origin_airport
      self.departure_city = origin_city
      self.departure_date = out_date
      self.arrival_airport = destination_airport
      self.arrival_city = destination_city
      self.arrival_date = return_date

  