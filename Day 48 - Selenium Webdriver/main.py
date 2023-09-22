from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# TODO 1 Get product price from Amazon
# driver.get("https://www.amazon.ca/iRasptek-Raspberry-8GB-RAM-Starter/dp/B0BVYW5PFK/ref=sr_1_3_sspa?crid=286ODM27SRIQZ"
#            "&keywords=raspberry%2Bpi%2B4&qid=1695394973&sprefix=ras%2Caps%2C81&sr="
#            "8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
#
# price_dollor = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"Price is ${price_dollor.text}.{price_cents.text}")

# TODO 2 Automated Search
driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
# for time in event_times:
#     print(time.text)

event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# for name in event_name:
#     print(name.text)
    
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_name[n].text,
    }

print(events)
# close() will close a tab
# driver.close()
# While quit will close all tabs
driver.quit()
