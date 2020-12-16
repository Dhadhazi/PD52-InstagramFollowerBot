from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_driver_path = ""

ACCOUNT_TO_FOLLOW_FOLLOWERS = ""
USERNAME = ""
PASSWORD = ""

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.instagram.com/")


def login():
    accept_cookies_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
    time.sleep(2)
    if (accept_cookies_button):
        accept_cookies_button.click()
    time.sleep(2)

    username_input = driver.find_element_by_name("username")
    username_input.send_keys(USERNAME)
    password_input = driver.find_element_by_name("password")
    password_input.send_keys(PASSWORD)
    time.sleep(2)

    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
    login_button.click()


def find_followers():
    driver.get(f"https://www.instagram.com/{ACCOUNT_TO_FOLLOW_FOLLOWERS}/")
    time.sleep(2)
    followers_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    followers_button.click()
    time.sleep(2)

    modal = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')

    for i in range(10):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(2)


def follow():
    all_buttons = driver.find_elements_by_css_selector("li button")
    for button in all_buttons:
        try:
            button.click()
            time.sleep(1)
        except ElementClickInterceptedException:
            cancel_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
            cancel_button.click()


login()
time.sleep(2)
find_followers()
follow()