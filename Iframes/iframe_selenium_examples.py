from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.testmuai.com/selenium-playground/iframe-demo/")

time.sleep(3)  
iframe = driver.find_element(By.ID, "iFrame1")
driver.switch_to.frame(iframe)

body = driver.find_element(By.TAG_NAME, "body")

body.click()
body.send_keys(Keys.CONTROL + "a")
body.send_keys(Keys.DELETE)

body.send_keys("This text is entered inside the iframe successfully")

time.sleep(2)

driver.switch_to.default_content()

driver.quit()