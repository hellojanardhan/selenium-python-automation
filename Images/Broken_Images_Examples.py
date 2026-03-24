# 1️⃣ Using HTTP Request (requests library)

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.testmuai.com/selenium-playground/broken-image/")

images=WebDriverWait(driver , 10).until(
    EC.visibility_of_all_elements_located((By.XPATH, "//img[@src=\"abcd.jpg\"]"))
)
print(images)

for image in images:
    src = image.get_attribute("src")
    print(src)
    try:
        response  = requests.get(src)
        if response.status_code == 200:
            print(f"Image OK: {src}")
        else:
            print(f"Broken Image is found(staus {response.status_code}): {src}")

    except requests.exceptions.RequestException:
        print(f"Invalid Image URL: {src}")

driver.quit()

"""
✅ Explanation:

requests.head() sends a lightweight HTTP request to check if the image exists.

Status code 200 → OK, others (404, 500) → broken image.
"""

# 2️⃣ Using JavaScript DOM Properties
# Broken_Images_Modified.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 1️⃣ Launch browser
driver = webdriver.Firefox()  # or webdriver.Chrome()
driver.get("https://www.testmuai.com/selenium-playground/broken-image/")

# 2️⃣ Wait until at least one image is present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "img"))
)

# 3️⃣ Use JavaScript to detect broken images
broken_images = driver.execute_script("""
let broken = [];
let imgs = document.images;
for (let i=0; i<imgs.length; i++) {
    if (!imgs[i].complete || imgs[i].naturalWidth === 0) {
        broken.push(imgs[i].src);
    }
}
return broken;
""")

# 4️⃣ Print results
if broken_images:
    print("Broken images found:")
    for src in broken_images:
        print(src)
else:
    print("No broken images found")

# 5️⃣ Close browser
driver.quit()

