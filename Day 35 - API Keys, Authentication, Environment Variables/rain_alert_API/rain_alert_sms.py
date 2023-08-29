import requests
from twilio.rest import Client

ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "YOUR-API-KEY"

account_sid = "YOUR-ACCOUNT-ID"
auth_token = "YOUR AUTH TOKEN"
SENDER_PHONE = "+11234567890"
RECEIVER_PHONE = "+10987654321"

LAT = 51.509865
LONG = -0.118092

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
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(from_=SENDER_PHONE, body="It's going to be rain today 🌧️, Don't forget your ☂️", to=RECEIVER_PHONE)

    print(message.status)
