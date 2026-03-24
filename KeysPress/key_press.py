from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.testmuai.com/selenium-playground/key-press/")

wait = WebDriverWait(driver, 10)

# Use presence instead of clickable
input_ele = wait.until(EC.presence_of_element_located((By.ID, "my_field")))

# Re-locate before action (important trick)
input_ele = driver.find_element(By.ID, "my_field")

input_ele.click()
input_ele.send_keys(Keys.ENTER)

data = driver.find_element(By.XPATH ,"//p[@id='result']")
print(data.text)


assert "ENTER" in data.text