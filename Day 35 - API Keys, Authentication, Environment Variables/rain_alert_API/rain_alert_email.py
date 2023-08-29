import requests
import smtplib

ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "YOUR-API-KEY"
LAT = 51.509865
LONG = -0.118092

MY_EMAIL = "YOUR-EMAIL"
APP_PASSWORD = "YOUR-APP-PASSWORD"
RECIPIENT_EMAIL = "RECIPIENT_EMAIL"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

umbrella_needed = False

for hour_data in weather_slice:
    weather_id = hour_data["weather"][0]["id"]
    if int(weather_id) < 700:
        umbrella_needed = True

if umbrella_needed:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=APP_PASSWORD
        )

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject:Rain Rain Rain\n\n It's going to be rain today, Don't forget your Umbrella."
        )
