from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.testmuai.com/selenium-playground/drag-and-drop-demo/")

wait = WebDriverWait(driver, 10)

# Wait for elements
wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Draggable 1']")))
wait.until(EC.presence_of_element_located((By.ID, "mydropzone")))

# Always locate fresh elements
source = driver.find_element(By.XPATH, "//span[text()='Draggable 1']")
target = driver.find_element(By.ID, "mydropzone")

# 🔥 JavaScript Drag & Drop (Best Solution)
driver.execute_script("""
function dragAndDrop(source, target) {
    const dataTransfer = new DataTransfer();

    source.dispatchEvent(new DragEvent('dragstart', { dataTransfer }));
    target.dispatchEvent(new DragEvent('dragover', { dataTransfer }));
    target.dispatchEvent(new DragEvent('drop', { dataTransfer }));
    source.dispatchEvent(new DragEvent('dragend', { dataTransfer }));
}

dragAndDrop(arguments[0], arguments[1]);
""", source, target)

time.sleep(10)
print("✅ Drag and Drop performed successfully using JS")

driver.quit()



# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.testmuai.com/selenium-playground/drag-and-drop-demo/")

wait = WebDriverWait(driver, 10)

# Wait for elements (use presence, not clickable)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Draggable 1']")))
wait.until(EC.presence_of_element_located((By.ID, "mydropzone")))

# Re-locate elements (important)
source = driver.find_element(By.XPATH, "//span[text()='Draggable 1']")
target = driver.find_element(By.ID, "mydropzone")

# Perform drag and drop
actions = ActionChains(driver)
actions.click_and_hold(source).move_to_element(target).release().perform()

print("✅ Drag and Drop performed successfully")

driver.quit()