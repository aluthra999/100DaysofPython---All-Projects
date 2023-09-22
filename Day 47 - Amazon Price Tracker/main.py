from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.amazon.ca/CanaKit-Raspberry-Pi-Extreme-Kit/dp/B08DGZ67BP/ref=sr_1_5?crid=DSEVY2721XLB&keywords=" \
      "raspberry%2Bpi%2B4&qid=1695390732&sprefix=rasp%2Caps%2C106&sr=8-5&ufe=app_do%3Aamzn1.fos.d0e27fc4-6417-4b26-" \
      "97cb-f959a9930752&th=1"

SENDER_EMAIL = ""
RECEIVER_EMAIL = ""
APP_PASSWORD = ""

response = requests.get(
    url=URL,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31",
        "Accept-Language": "en-US,en;q=0.9"
    }
)

soup = BeautifulSoup(response.content, "lxml")

# Check if the element with id "productTitle" exists before extracting the title
title_element = soup.find(id="productTitle")
if title_element:
    title = title_element.get_text().strip()
    print(title)
else:
    print("Title element not found on the webpage.")

BUY_PRICE = 200

# Check if the element with class "a-offscreen" exists before extracting the price
price_element = soup.find(class_="a-offscreen")
if price_element:
    price = price_element.get_text()
    price_without_currency = price.split("$")[1]
    price_as_float = float(price_without_currency)
    print(price_as_float)

    if price_as_float < BUY_PRICE:
        message = f"{title} is now {price}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login(SENDER_EMAIL, APP_PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
            )

else:
    print("Price element not found on the webpage.")
