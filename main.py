"""import tkinter as tk

window = tk.Tk()
window.title("Hello world")
window.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()

Program Requirements
Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.

The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.

Toggle these options when setting up with the API providers

Sheety API
Avoid making too many unnecessary requests with the Sheety API while testing your code. The free tier for the Sheety API only allows 200 requests per month.
"""
import part02.main as p

p.run()