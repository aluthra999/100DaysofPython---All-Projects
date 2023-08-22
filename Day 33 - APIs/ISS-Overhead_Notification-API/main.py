import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "YOUR_EMAIL@gmail.com"
APP_PASSWORD = "YOUR_APP_PASSWORD"

MY_LAT = 46.268400  # Your latitude
MY_LONG = -63.110260  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night_time() and is_night_time():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(
                user=MY_EMAIL,
                password=APP_PASSWORD
            )
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="RECIPIENT@EMAIL.COM",
                msg=f"Subject:Look up in Sky 🛰️\n\nLook Up ISS is passing above you any second now!"
            )
