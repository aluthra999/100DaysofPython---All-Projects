from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

INSTA_ACCOUNT = "your username"
INSTA_PASSWORD = "your password"

ACCOUNT_URL = "https://www.instagram.com/chefsteps/"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(), options=options)

    def login(self):
        self.driver.get(ACCOUNT_URL)
        sleep(5)
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div['
                                 '2]/div/div/div[3]/div/div[2]/div[1]/a/button').click()
        sleep(3)
        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        username.send_keys(INSTA_ACCOUNT)
        sleep(5)
        password.send_keys(INSTA_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(5)

    def find_followers(self):
        # Dismiss notification for new insta account : if not skip this
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div["
                                 "2]/section/main/div/div/div/div/button").click()
        sleep(3)

        # find followers
        followers_to_follow = self.driver.find_element(By.XPATH,
                                                       "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div["
                                                       "1]/div[2]/section/main/div/header/section/ul/li[2]/a/div")
        followers_to_follow.click()
        sleep(2)

    def follow(self):
        # Number of followers
        number_of_followers = self.driver.find_element(By.XPATH,
                                                       "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div["
                                                       "1]/div[2]/section/main/div/header/section/ul/li["
                                                       "2]/a/div/span/span")
        number = int(number_of_followers.text.split(' ')[0].strip()) * 1000

        # Follow all the followers
        for i in range(1, number):
            try:
                follow = self.driver.find_element(By.XPATH,
                                                  f"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div["
                                                  f"2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div["
                                                  f"3]/button")
                follow.click()
                sleep(2)
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,
                                                         "/html/body/div[2]/div/div/div/div[2]/div/div/div["
                                                         "2]/div/div/div[1]/div/div[ "
                                                         "2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
                cancel_button.click()
                sleep(1)


insta_follower = InstaFollower()

insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
