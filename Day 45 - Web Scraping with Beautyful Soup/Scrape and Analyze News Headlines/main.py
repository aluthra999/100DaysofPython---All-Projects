"""
Description:

Create a Python program that scrapes news headlines from a news website and provides you with some insights or analysis
based on the headlines.
"""
import requests
from bs4 import BeautifulSoup
from mail import Mail


# TODO 1.Choose a News Website: Select a news website from which you want to scrape headlines.
techcrunch_link = "https://techcrunch.com/"

# TODO 2.Scrape Headlines:
#  Use BeautifulSoup and Python's requests library to scrape the headlines from the chosen website.
#  Extract relevant information such as the headline text, publication date, and link to the full article.
response = requests.get(url=techcrunch_link)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
headline = soup.find(name="h2", class_="fi-main-block__title")
headline_link = soup.find(name="a", class_="post-block__title__link")
print(headline.text)
print(f"{headline_link.get('href')}")

mail = Mail
write_mail = mail(headline.text, headline_link.get('href'))
