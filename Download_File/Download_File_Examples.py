import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1️⃣ Set download directory
download_path = os.path.join(os.getcwd(), "downloads")
os.makedirs(download_path, exist_ok=True)

# 2️⃣ Chrome options (🔥 important fix added)
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True   # ✅ Force PDF download
}
options.add_experimental_option("prefs", prefs)

# 3️⃣ Launch browser
driver = webdriver.Chrome(options=options)
driver.get("https://www.testmuai.com/selenium-playground/download-file-demo/")

# 4️⃣ Click Download button (🔥 stable JS click)
for i in range(5):
    try:
        driver.execute_script("""
            var xpath = "//button[text()='Download File']";
            var result = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
            var element = result.singleNodeValue;
            if (element) { element.click(); }
        """)
        print("✅ Clicked Download Button")
        break
    except:
        time.sleep(1)

# 5️⃣ Wait for download
time.sleep(5)

# 6️⃣ Verify download
files = os.listdir(download_path)

if files:
    print("✅ File downloaded successfully:", files)
else:
    print("❌ File download failed")

driver.quit()