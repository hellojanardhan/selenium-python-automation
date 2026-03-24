from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.testmuai.com/selenium-playground/shadow-dom/")

wait = WebDriverWait(driver, 10)

# Direct JS (no WebElement → no stale issue)
shadow_root = wait.until(
    lambda d: d.execute_script(
        "return document.querySelector('shadow-signup-form')?.shadowRoot"
    )
)

# Now find element inside shadow DOM
username = shadow_root.find_element(By.CSS_SELECTOR, "input[name='username']")
username.send_keys("John")

driver.quit()