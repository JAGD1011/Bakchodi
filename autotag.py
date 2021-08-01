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
    username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.p3_M1"))
        )

    for x in range (0,6):

        username.send_keys( '@' )

        time.sleep(1)

        for y in range (0,x):
            username.send_keys(Keys.ARROW_DOWN)

        username.send_keys( '\n' )

        time.sleep(1)

        username.send_keys( '\n' )

        time.sleep(1)

    

except:
    driver.quit()