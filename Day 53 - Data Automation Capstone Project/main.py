from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests

# Set up the Selenium WebDriver (make sure you have a webdriver installed)
driver = webdriver.Chrome()

zillow_link = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds" \
              "%22%3A%7B%22west%22%3A-122.64275587988281%2C%22east%22%3A-122.22390212011719%2C%22south%22%3A37." \
              "64410412680146%2C%22north%22%3A37.906246406831336%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3A" \
              "false%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1" \
              "%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%" \
              "22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%" \
              "22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%" \
              "22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

google_form_url = 'https://forms.gle/r6wHW6P76CUXx4hK8'

# Send an HTTP GET request to the URL
response = requests.get(google_form_url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Extract listing data
listing_links = [a['href'] for a in soup.select(".list-card-link")]
listing_prices = [price.text for price in soup.select(".list-card-price")]
listing_addresses = [address.text for address in soup.select(".list-card-addr")]

# Ensure all lists have the same length
min_length = min(len(listing_links), len(listing_prices), len(listing_addresses))

# Print the first 5 listings as a test
for i in range(min_length):
    print(f"Listing {i+1} - Price: {listing_prices[i]}, Address: {listing_addresses[i]}, Link: {listing_links[i]}")

# Loop through each listing and submit data to the Google Form
for i in range(len(listing_links)):
    driver.get(google_form_url)

    # Fill in the form fields
    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                '/div/div[1]/div/div[1]/input')
    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/'
                                                  'div[2]/div/div[1]/div/div[1]/input')
    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/'
                                               'div[2]/div/div[1]/div/div[1]/input')

    price_field.send_keys(listing_prices[i])
    address_field.send_keys(listing_addresses[i])
    link_field.send_keys(listing_links[i])

    # Submit the form
    link_field.send_keys(Keys.RETURN)

    # Wait for a few seconds before moving to the next listing (to avoid rate limiting)
    time.sleep(3)

# Close the WebDriver
driver.quit()
