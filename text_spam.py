from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

time.sleep(5)

driver.get("https://web.whatsapp.com")

print ('Instructions: \n1.After the whatsapp web gets opened, put it on split screen \n2. select the chat where you want to spam \n3. enter the text and no.of messages. \n4. Please make sure not to disturb the web window once it gets opened. \n')

text = input('Text bol:')


n = int(input ('kitne: '))

print ('ho gaya kaam, ab jaa.')

try:
    username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.p3_M1"))
        )

    for x in range (0,n):
        print ('Count :' + x)

        username.send_keys( text + '\n')
        time.sleep(0.1)

except:
    driver.quit()