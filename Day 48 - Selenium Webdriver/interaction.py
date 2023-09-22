from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_count.click()

login = driver.find_element(By.LINK_TEXT, "Log in")
login.click()

username = driver.find_element(By.XPATH, '//*[@id="wpName1"]')
username.send_keys('test')
username.send_keys(Keys.TAB)

password = driver.find_element(By.XPATH, '//*[@id="wpPassword1"]')
password.send_keys("TestPassword1!")

login_button = driver.find_element(By.XPATH, '//*[@id="wpLoginAttempt"]')
login_button.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("India")
# search.send_keys(Keys.ENTER)

# driver.quit()
