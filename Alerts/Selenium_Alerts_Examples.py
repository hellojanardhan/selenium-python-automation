# JavaScript Alerts (Browser popups)

# Simple Alert
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://example.com/js-alert")

# Trigger alert
driver.find_element(By.Id, "alertButton").click()

# switch to alert
alert = driver.switch_to_alert

# Read alert text
print("Alert message",alert.text)

# Accept the alert
alert.accept()

# Confirmation Alert

driver.find_element(By.ID, "confirmationButton").click()

confirm_alert = driver.switch_to_alert
print("Confirm message", confirm_alert.text)

# click confirm
confirm_alert.dismiss()

# Prompt Alert

driver.find_element(By.ID , "promptButton").click()

prompt_alert = driver.switch_to_alert

print(f"Prompt message" , prompt_alert.text)

prompt_alert.send_keys("Hello selenium")
promot_alert.accept()

# Wait for alert to appear
alert = WebDriver.wait(driver, 10).until(EC.alert_is_present())
alert_text = alert.text
print("Dynamic alert text ",alert_text)
alert.accept()

# HTML Alerts (Bootstrap / Material / Toasts)

#1. Simple Bootstrap Alert
from selenium.webdriver.common.by import By

driver.get("https://example.com/bootstrap-alerts")

# Locate the HTML element
html_alert = driver.find_element(By.ID, "myAlert")
print("HTML alert", html_alert.text)

# close alert (If close button exists)
html_alert.find_element(By.ID ,"close").click()

#2. Toast Notification (disappearing alert)

driver.get("https://example.com/toast-alert")

# wait until the toast is visible
toast = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "toastMsg")))

print("Toast Message", toast.text)

# HTML Alert with Button Action
driver.get("https://example.com/html-alert-buttons")

# Click action inside HTML alert
html_alert = driver.find_element(By.ID, "actionAlert")
print("Alert message:", html_alert.text)

html_alert.find_element(By.XPATH, ".//button[text()='Confirm']").click()