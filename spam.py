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
    #username.send_keys("a")
    for x in range (0,600):

        time.sleep(0.1)
        print (x)
        #time.sleep(0.2)
        #username.send_keys('@Gargee' + '\n'  + '@pi' + '\n' + '@ra' + '\n' + '@abhir' + '\n' + '@ib' + '\n' + '@me' + '\n' + '@ramd' + '\n' + '@bha' + '\n' + '@bhos' + '\n' + '@hars' + '\n' + '@him' + '\n' + '@ish' + '\n' + '@jyotika' + '\n' + '@jyotishna' + '\n' + '@pra' + '\n' + '@sanya' + '\n' + '@tims' + '\n' + '@wiki' + '\n' + 'automatic tags by Aviral and Arsh' "\n")
        #username.send_keys('.' '\n' + ',' + '\n')
        username.send_keys('Happy bday ')
        time.sleep(0.1)
        username.send_keys('Aarya')
        #for y in range (0,23):
        #username.send_keys(Keys.ARROW_DOWN)
        #time.sleep(0.1)
        username.send_keys('\n')
        time.sleep(0.1)
        # username.send_keys(Keys.RETURN)
        #time.sleep(0.4)
        username.send_keys('\n')
        
    #username.send_keys('\n')

except:
    driver.quit()