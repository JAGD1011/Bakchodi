from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://tutedude.com/#")
#numbers = []
try:
    loginbu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "hide-login"))
)
    loginbu.click()
    time.sleep(1)
    
    username = driver.find_element_by_id('input-EmailLogin')

    password = driver.find_element_by_id('input-PasswordLogin')
    
    
    
    #un = input("Enter your kerberos ID: ")
    username.send_keys('militantmini1@gmail.com')

    #pw = input("Enter your kerberos password: ")
    password.send_keys('Arsh@152107')


    button = driver.find_element_by_xpath('//button[normalize-space()="Login"]')            #selenium se button doondhna
    button.click()

except:
    driver.quit()

