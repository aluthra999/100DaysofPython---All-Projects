import requests
from datetime import date
from datetime import timedelta
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

today = date.today()
yesterday = today - timedelta(days=1)
# Day before Yesterday (dby)
dby = today - timedelta(days=2)

# Alpha Vantage API - Stock Price

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "YOUR-API-KEY"

stocks_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stocks_response = requests.get(STOCK_ENDPOINT, params=stocks_parameters)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()

# NEWS ARTICLES API

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "YOUR-API-KEY"

news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
news_articles = []

# TWILIO API

account_sid = "YOUR-ACCOUNT-ID"
auth_token = "YOUR-API-KEY"

# Your Twilio phone number
FROM_PHONE = "+11234567890"

# Recipient phone number
TO_PHONE = "+10987654321"

# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries.
#  e.g. [new_value for (key, value) in dictionary.items()]
yesterday_closing_price = float(stocks_data["Time Series (Daily)"][str(yesterday)]['4. close'])
# print(f"Closing price on {yesterday} was: ${yesterday_closing_price}")

# TODO 2. - Get the day before yesterday's closing stock price
dby_closing_price = float(stocks_data["Time Series (Daily)"][str(dby)]['4. close'])
# print(f"Closing price on {dby} was: ${dby_closing_price}")

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = yesterday_closing_price - dby_closing_price
# print(difference)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.

percentage_difference = ((yesterday_closing_price - dby_closing_price) / dby_closing_price) * 100
# print(round(percentage_difference, 1))

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(percentage_difference) >= 0:
    # print("Message should Go!")
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    # TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint:
    #  https://stackoverflow.com/questions/509211/understanding-slice-notation
    news_articles = news_data["articles"][:1]

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    article_list = [
        f"{STOCK_NAME}: {up_down}{round(percentage_difference, 2)}%\nHeadline: {article['title']}\n" \
        f"Brief: {article['description']}"
        for article in news_articles]
    print(article_list)

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # TODO 9. - Send each article as a separate message via Twilio.
    for article_text in article_list:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_=FROM_PHONE,
            body=article_text,
            to=TO_PHONE
        )

        print(message.status)

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of 
the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of
 the coronavirus market crash.
"""
