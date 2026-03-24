from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.testmuai.com/selenium-playground/hover-demo/")

wait = WebDriverWait(driver, 10)

# locate element
button = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//div[text()='Hover Me'])[1]"))
)

# before hover
before_hover = button.value_of_css_property("background-color")
print("Before hover:", before_hover)

# hover action
ActionChains(driver).move_to_element(button).perform()

# IMPORTANT: re-locate after hover
button_after = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//div[text()='Hover Me'])[1]"))
)

after_hover = button_after.value_of_css_property("background-color")
print("After hover:", after_hover)

driver.quit()


# Example-2

driver = webdriver.Chrome()
driver.get("https://www.testmuai.com/selenium-playground/hover-demo/")

wait = WebDriverWait(driver, 10)

# locate element
button = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//div[text()='Hover Me'])[2]"))
)

# before hover
before_hover = button.value_of_css_property("background-color")
print("Before hover:", before_hover)

# hover action
ActionChains(driver).move_to_element(button).perform()

# IMPORTANT: re-locate after hover
button_after = wait.until(
    EC.visibility_of_element_located((By.XPATH, "(//div[text()='Hover Me'])[2]"))
)

after_hover = button_after.value_of_css_property("background-color")
print("After hover:", after_hover)

driver.quit()

# CSS Hover Effects on Button

# Example -1

driver = webdriver.Chrome()
driver.get("https://www.testmuai.com/selenium-playground/hover-demo/")

wait = WebDriverWait(driver, 10)

# Step 1: Locate main hover element
link_hover = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='Link Hover']"))
)

# Step 2: Perform hover
ActionChains(driver).move_to_element(link_hover).perform()
print("Hovered on Link Hover")

driver.quit()


# Example-2
driver = webdriver.Chrome()
driver.get("https://www.testmuai.com/selenium-playground/hover-demo/")

wait = WebDriverWait(driver, 10)

# Step 1: Locate main hover element
link_hover = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class=\"flex ml-15\"][2]//div[text()='Hover Me']"))
)

# before_hover
before_hover = driver.find_element(By.XPATH , "//div[@class=\"flex ml-15\"][2]//div[text()='Hover Me']")
print(f"Before hover {before_hover.value_of_css_property('background-color')}")


actions = ActionChains(driver)
actions.move_to_element(link_hover).perform()


after_hover_link = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class=\"flex ml-15\"][2]//div[text()='Hover Me']"))
)

#after_hover
after_hover = driver.find_element(By.XPATH , "//div[@class=\"flex ml-15\"][2]//div[text()='Hover Me']")
print(f"After hover {after_hover.value_of_css_property('background-color')}")

driver.quit()


