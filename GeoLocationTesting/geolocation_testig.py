from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()

options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 1
})

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# 🌍 Set London location
driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
    "latitude": 51.468183,
    "longitude": -0.128145,
    "accuracy": 100
})

driver.get("https://whatmylocation.com/")

time.sleep(5)

# 📌 Capture full page text
text = driver.find_element(By.TAG_NAME, "body").text

print("----- OUTPUT -----")
print(text)

# ✅ Validation using coordinates (BEST METHOD)
if "51.468183" in text and "-0.128145" in text:
    print("✅ Test Passed: Location correctly set to London coordinates")
else:
    print("❌ Test Failed: Coordinates not matched")

driver.quit()