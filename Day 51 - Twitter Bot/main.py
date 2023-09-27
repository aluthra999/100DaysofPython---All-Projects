import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

TWITTER_EMAIL = "example@gmail.com"
TWITTER_PASSWORD = "xyz"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.down = 0
        self.up = 0

    def get_internet_Speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(4)
        accept_cookie = self.driver.find_element(By.CLASS_NAME, value="onetrust-banner-options")
        accept_cookie.click()
        sleep(5)
        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()
        sleep(50)
        self.down = float(self.driver.find_element(By.CLASS_NAME, value="download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, value="upload-speed").text)
        print(self.down, self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        sleep(10)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(TWITTER_EMAIL)
        sleep(1)
        email_input.send_keys(Keys.ENTER)
        sleep(5)
        try:
            pass_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/"
                                                     "div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            # Your Username here in case Twitter asks for username before asking password
            username.send_keys("example")
            username.send_keys(Keys.ENTER)
            sleep(5)
            pass_input = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div"
                                                       "/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/"
                                                       "div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)

        sleep(5)

        input_ = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        input_.send_keys(f"My Current Internet Speed is {self.down} Download and {self.up} Upload")
        sleep(3)
        tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/"
                                                   "div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]"
                                                   "/div/div/div[2]/div[3]/div/span/span")
        tweet.click()
        time.sleep(5)
        print("Tweet Done")
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_Speed()
bot.tweet_at_provider()
