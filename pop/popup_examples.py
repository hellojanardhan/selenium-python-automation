from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.testmuai.com/selenium-playground/window-popup-modal-demo/")

wait = WebDriverWait(driver, 10)

main_window = driver.current_window_handle
main_title = driver.title

# ✅ SAFE CLICK (re-finds element every retry)
def click_element(d):
    elem = d.find_element(By.XPATH, "//a[@title='Follow @Lambdatesting on Twitter']")
    elem.click()
    return True

wait.until(click_element)

# wait for new window
wait.until(lambda d: len(d.window_handles) > 1)

for window in driver.window_handles:
    driver.switch_to.window(window)
    if "twitter" in driver.current_url.lower():
        break

print("Child title:", driver.title)

driver.close()

driver.switch_to.window(main_window)

print("Main title:", driver.title)

assert driver.title == main_title

driver.quit()