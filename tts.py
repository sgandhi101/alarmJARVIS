from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import requests

def speak(text):
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

    driver = webdriver.Chrome(executable_path=DRIVER_BIN, options=chrome_options)

    driver.get("https://www.ibm.com/demos/live/tts-demo/self-service/home")
    driver.find_element_by_id('text-area').clear()
    driver.find_element_by_id('text-area').send_keys(text)

    driver.find_element_by_id('dialect').click()
    sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div').click()

    driver.find_element_by_id('voice').click()
    sleep(0.5)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[3]/div/div/div/div[3]/div').click()

    driver.find_element_by_id('downshift-3-toggle-button').send_keys(Keys.ARROW_UP, Keys.ENTER)

    driver.find_element_by_id('btn').click()
    sleep(9.5)
    requests.post("https://maker.ifttt.com/trigger/light_on/with/key/gsKcdHNyARXIQw9Mzh3ZTdMN_z5SK69A-btqMxQvHE8")
    # Following line of code is only for Mac OS
    os.system(
        'afplay -v 0.18 soundtrack.mp3')  # This is NOT a linear scaling but relative to a logarithmic output

    sleep(60)
    os.system('killall chromedriver')
