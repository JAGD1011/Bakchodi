from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
time.sleep(4)

driver.get("https://web.whatsapp.com")

input ('kitne bande: ')

try:

    for x in range(0,10):

        emoji_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "_23sAs _3V3JJ l9Mer _2Bl6V _1owZM"))
        )
        emoji_button.click()

        time.sleep(0.1)

        emoji = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "b35 emojik wa"))
        )
        emoji.click()

        time.sleep(0.1)

        textbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.p3_M1"))
        )
        textbox.send_keys( '\n')

        time.sleep(0.2)

    

except:
    driver.quit()