# import libraries
from datetime import datetime
from tkinter import *
from geopy.geocoders import Nominatim
import requests

MY_LAT = ""
MY_LONG = ""

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}


def get_lat_long(address):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(address)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None


def calc():
    address = address_entry.get()  # Get the address from the entry widget
    lat_long = get_lat_long(address)  # Get latitude and longitude for the provided address

    if lat_long:
        global MY_LAT, MY_LONG
        MY_LAT, MY_LONG = lat_long  # Update global variables with the new lat and long

        parameters["lat"] = MY_LAT
        parameters["lng"] = MY_LONG

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()

        sunrise_label_text.config(text=data["results"]["sunrise"])
        sunset_label_text.config(text=data["results"]["sunset"])
    else:
        sunrise_label_text.config(text="Address not found")
        sunset_label_text.config(text="Address not found")


window = Tk()
window.title("Sunrise - Sunset")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=350)

# Address Section
address_label = Label(text="Address: ")
address_label.grid(row=1, column=1)

address_entry = Entry(width=30)
address_entry.grid(row=1, column=2)

# Date (Set to today by default)
today_date_finder = datetime.now().date()

today_date_label = Label(text="Date:")
today_date_label.grid(row=2, column=1)

today_date = Label(text=f"{today_date_finder}")
today_date.grid(row=2, column=2)

# Sunrise Info
sunrise_label = Label(text="Sunrise will be at: ")
sunrise_label.grid(row=3, column=1)

sunrise_label_text = Label(text="")
sunrise_label_text.grid(row=3, column=2)

# Sunset Info
sunset_label = Label(text="Sunset will be at: ")
sunset_label.grid(row=4, column=1)

sunset_label_text = Label(text="")
sunset_label_text.grid(row=4, column=2)

# Button
calculate_button = Button(text="Find the time", command=calc, width=30)
calculate_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
