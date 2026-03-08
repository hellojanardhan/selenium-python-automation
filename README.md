# Selenium Python Automation

A comprehensive guide to **End-to-End Selenium automation with Python**, covering core concepts, locators, waits, Page Object Model (POM), best practices, and real-world applications.

## 📚 Table of Contents

1. [Introduction to Selenium](#introduction-to-selenium)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
4. [Core Concepts](#core-concepts)
5. [Locating Strategies](#locating-strategies)
6. [Wait Mechanisms](#wait-mechanisms)
7. [Advanced Interactions](#advanced-interactions)
8. [Page Object Model](#page-object-model)
9. [Error Handling](#error-handling)
10. [Best Practices](#best-practices)

---

## Introduction to Selenium

### What is Selenium?

Selenium is an **open-source browser automation tool** used to automate web applications. It allows you to:

- ✅ Open websites and navigate through pages
- ✅ Click buttons and interact with elements
- ✅ Enter text in forms and submit data
- ✅ Handle alerts and popups
- ✅ Simulate real user actions

### Key Features

- **Multi-Browser Support**: Chrome, Firefox, Microsoft Edge, Safari, Opera
- **Multi-Language Support**: Python, Java, C#, JavaScript
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Parallel Execution**: Run tests simultaneously for faster results
- **Open Source & Free**: No licensing costs
- **Large Community**: Extensive documentation and support
- **CI/CD Integration**: Seamless integration with Jenkins, GitHub Actions, etc.

### Why Use Selenium?

1. **Automate Repetitive Tasks**: Login, form submission, data extraction
2. **Functional Testing**: Verify features work correctly
3. **Regression Testing**: Ensure new changes don't break existing functionality
4. **Cross-Browser Testing**: Check application behavior across different browsers
5. **Cost-Effective**: Reduces manual testing effort and time
6. **Increased Test Coverage**: Run more test scenarios faster

---

## Project Structure

```
selenium-python-automation/
├── 01_Intro_to_Selenium
├── 02_Components_of_Selenium
├── 03_Intro_to_Selenium_WebDriver
├── 04_App_and_Uses_of_Selenium_WebDriver
├── 05_Features_Of_Selenium
├── 06_Limitations_Of_Selenium
├── 07_Selenium_Python_Installation
├── 08_navigation_get_method.py
├── 09_Interacting_With_Webpage
├── 10_Locating_Multiple_Elements
├── 11_Selenium_Locating_Strategies
├── 12_Explicit-Waits-In-Selenium
├── 13_Implicit_Waits_In_Selenium
├── 14_Selenium_ActionChains
├── 15_Handle_Alerts_In_Selenium
├── 16_Adding_Deleting_Cookies_Selenium
├── 17_Exceptions_In_Selenium.txt
├── 18_Assertions_In_Selenium
├── 19_PageObjectModel_In_Selenium
├── 20_WebDriver_Methods_In_Selenium
├── 21_Element_Methods_In_Selenium
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

#### Step 1: Install Python

1. Download from [python.org](https://www.python.org/)
2. **Important**: Check "Add Python to PATH" during installation
3. Verify installation:
   ```bash
   python --version
   # or
   py --version
   ```

#### Step 2: Install Selenium

```bash
pip install selenium
# or for multiple Python installations
py -m pip install selenium
```

Verify Selenium installation:
```bash
pip show selenium
```

#### Step 3: Install a Web Browser

Download one of the supported browsers:
- [Chrome](https://www.google.com/chrome/)
- [Firefox](https://www.mozilla.org/firefox/)
- [Microsoft Edge](https://www.microsoft.com/edge/)

#### Step 4: WebDriver Setup

**Note**: Selenium 4.6+ includes Selenium Manager which automatically manages drivers. No manual setup needed!

Simple example:
```python
from selenium import webdriver

# Automatically downloads Chrome driver
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
driver.quit()
```

---

## Core Concepts

### Components of Selenium

Selenium consists of 4 main components:

#### 1️⃣ Selenium IDE
- Browser extension for recording and playback
- Suitable for beginners and quick prototyping
- Limited for complex automation

#### 2️⃣ Selenium RC (Remote Control)
- Older component, now deprecated
- Required a separate server
- Replaced by WebDriver for better performance

#### 3️⃣ Selenium WebDriver ⭐
- **Main component** used in real-time projects
- Direct communication with browsers
- No server needed
- Fast and reliable

#### 4️⃣ Selenium Grid
- Run tests on multiple machines simultaneously
- Hub-Node architecture
- Enables parallel and cross-browser testing

### WebDriver Methods

#### Navigation Methods
```python
driver.get("https://www.example.com")      # Open URL
driver.back()                               # Go back
driver.forward()                            # Go forward
driver.refresh()                            # Refresh page
```

#### Window Management
```python
driver.maximize_window()                    # Maximize window
driver.minimize_window()                    # Minimize window
driver.fullscreen_window()                  # Fullscreen mode
driver.get_window_size()                    # Get size
driver.set_window_rect(x, y, width, height) # Set size and position
```

#### Browser Information
```python
driver.title                                # Get page title
driver.current_url                          # Get current URL
driver.page_source                          # Get page HTML
```

---

## Locating Strategies

### 7 Locator Strategies

Selenium provides 7 ways to locate elements:

#### 1️⃣ By ID (Fastest & Most Reliable)
```python
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "element_id")
```

#### 2️⃣ By Name
```python
element = driver.find_element(By.NAME, "element_name")
```

#### 3️⃣ By Class Name
```python
element = driver.find_element(By.CLASS_NAME, "class_name")
```

#### 4️⃣ By Tag Name
```python
elements = driver.find_elements(By.TAG_NAME, "button")  # All buttons
```

#### 5️⃣ By CSS Selector (Recommended)
```python
element = driver.find_element(By.CSS_SELECTOR, "div.title")
```

#### 6️⃣ By XPath
```python
element = driver.find_element(By.XPATH, "//input[@id='username']")
```

#### 7️⃣ By Link Text
```python
element = driver.find_element(By.LINK_TEXT, "Click Here")
element = driver.find_element(By.PARTIAL_LINK_TEXT, "Click")  # Partial match
```

### Finding Multiple Elements

```python
from selenium.webdriver.common.by import By

# Returns a list of elements
elements = driver.find_elements(By.TAG_NAME, "button")
print(len(elements))  # Number of buttons

# Iterate through elements
for element in elements:
    element.click()
```

---

## Wait Mechanisms

Modern web applications load content dynamically. Waits help Selenium wait for elements before interacting.

### Implicit Wait

Applies globally to all element searches:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(10)  # Wait up to 10 seconds

driver.get("https://www.example.com")
element = driver.find_element(By.ID, "myDynamicElement")
```

**Characteristics:**
- Global scope (applies to all elements)
- Set once during session
- Selenium waits for specified time before throwing exception

### Explicit Wait (Recommended)

More precise - waits for specific conditions:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.example.com")

# Wait up to 10 seconds for element to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "myButton"))
)
element.click()
```

### Common Expected Conditions

| Condition | Purpose |
|-----------|---------|
| `presence_of_element_located()` | Element exists in DOM |
| `visibility_of_element_located()` | Element is visible |
| `element_to_be_clickable()` | Element is clickable |
| `title_is()` | Page title matches |
| `title_contains()` | Page title contains text |
| `alert_is_present()` | Alert popup appears |

---

## Advanced Interactions

### Interacting with Web Elements

#### Basic Element Methods
```python
from selenium.webdriver.common.by import By

element = driver.find_element(By.ID, "username")

# Type text
element.send_keys("admin")

# Clear text field
element.clear()

# Click element
element.click()

# Press keyboard keys
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.ARROW_DOWN)
element.send_keys(Keys.ENTER)
```

#### Element Properties
```python
# Check if element is selected (checkbox/radio)
is_selected = element.is_selected()

# Check if element is visible
is_visible = element.is_displayed()

# Check if element is enabled
is_enabled = element.is_enabled()

# Get element text
text = element.text

# Get attribute value
id_value = element.get_attribute("id")

# Get CSS property
color = element.value_of_css_property("color")
```

### Action Chains (Advanced Interactions)

For complex mouse and keyboard actions:

```python
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
actions = ActionChains(driver)

# Mouse hover
menu = driver.find_element(By.ID, "menu")
actions.move_to_element(menu).perform()

# Double click
element = driver.find_element(By.ID, "button")
actions.double_click(element).perform()

# Right click
actions.context_click(element).perform()

# Drag and Drop
source = driver.find_element(By.ID, "drag")
target = driver.find_element(By.ID, "drop")
actions.drag_and_drop(source, target).perform()

# Click and Hold
actions.click_and_hold(element).perform()
actions.release(element).perform()
```

### Handling Alerts

```python
from selenium.webdriver.common.alert import Alert

# Switch to alert
alert = Alert(driver)

# Get alert text
alert_text = alert.text

# Accept alert (click OK)
alert.accept()

# Dismiss alert (click Cancel)
alert.dismiss()

# Send text to alert input
alert.send_keys("Hello, Alert!")
```

### Handling IFrames

```python
# Switch to iframe
iframe = driver.find_element(By.ID, "myIframe")
driver.switch_to.frame(iframe)

# Now interact with elements inside iframe
element = driver.find_element(By.ID, "element_in_iframe")
element.click()

# Switch back to main content
driver.switch_to.default_content()
```

### Cookie Management

```python
# Add a cookie
driver.add_cookie({"name": "foo", "value": "bar"})

# Get a specific cookie
cookie = driver.get_cookie("foo")
print(cookie)  # {'name': 'foo', 'value': 'bar'}

# Get all cookies
all_cookies = driver.get_cookies()

# Delete a specific cookie
driver.delete_cookie("foo")

# Delete all cookies
driver.delete_all_cookies()
```

---

## Page Object Model

Page Object Model (POM) is a design pattern that improves code organization and maintainability.

### Benefits of POM

- ✅ **Organized Code**: Each page has its own class
- ✅ **Reusable**: Share page objects across multiple tests
- ✅ **Easy Maintenance**: Change locators in one place
- ✅ **Better Readability**: Clear separation of concerns

### Project Structure with POM

```
project/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── home_page.py
│   └── dashboard_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   └── test_dashboard.py
└── driver_setup.py
```

### Example: Login Page Object

```python
# pages/login_page.py
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    
    # Locators
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    
    # Actions
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
```

### Example: Test Script Using POM

```python
# tests/test_login.py
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com/login")
    
    def teardown_method(self):
        self.driver.quit()
    
    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("admin", "password123")
        
        # Verify login was successful
        assert "dashboard" in self.driver.current_url
```

---

## Error Handling

### Common Selenium Exceptions

| Exception | Cause | Solution |
|-----------|-------|----------|
| `NoSuchElementException` | Element not found | Check locator, wait for element |
| `ElementClickInterceptedException` | Another element blocks click | Use Explicit Wait, scroll element |
| `ElementNotInteractableException` | Element hidden/disabled | Make element visible, enable it |
| `NoAlertPresentException` | Alert not found | Check if alert exists |
| `TimeoutException` | Element took too long to load | Increase wait time, optimize code |
| `StaleElementReferenceException` | Element no longer in DOM | Re-locate element |

### Exception Handling Example

```python
from selenium.common.exceptions import NoSuchElementException, TimeoutException

try:
    element = driver.find_element(By.ID, "button")
    element.click()
except NoSuchElementException:
    print("Element not found")
except TimeoutException:
    print("Timeout waiting for element")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Assertions & Testing

### Basic Python Assertions

```python
# Simple assertion
assert driver.title == "Google"

# Assertion with message
assert driver.title == "Google", "Title does not match"

# Verify element properties
element = driver.find_element(By.ID, "login")
assert element.is_displayed(), "Element is not displayed"
assert element.is_enabled(), "Element is disabled"
assert element.is_selected(), "Element is not selected"
```

### Using Pytest

```python
# tests/test_login.py
import pytest
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.quit()
    
    def test_login_success(self):
        login_page = LoginPage(self.driver)
        login_page.login("admin", "password")
        assert "dashboard" in self.driver.current_url
    
    def test_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.login("wrong", "credentials")
        assert "error" in driver.page_source.lower()
```

### Using Unittest

```python
import unittest
from selenium import webdriver

class TestGoogle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
    
    def tearDown(self):
        self.driver.quit()
    
    def test_page_title(self):
        self.assertEqual(self.driver.title, "Google")
    
    def test_url_contains(self):
        self.assertIn("google", self.driver.current_url)

if __name__ == "__main__":
    unittest.main()
```

---

## Best Practices

### ✅ DO's

1. **Use Explicit Waits** - More reliable than implicit waits
   ```python
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "button")))
   ```

2. **Implement Page Object Model** - Makes tests maintainable
   ```python
   from pages.login_page import LoginPage
   ```

3. **Use Proper Locators** - In order of preference:
   - ID (fastest)
   - Name
   - CSS Selector
   - XPath (slowest)

4. **Handle Exceptions** - Use try-except blocks
   ```python
   try:
       element = driver.find_element(By.ID, "button")
   except NoSuchElementException:
       print("Element not found")
   ```

5. **Use Assertions** - Verify expected behavior
   ```python
   assert driver.title == "Expected Title"
   ```

6. **Clean Up Resources** - Always close the driver
   ```python
   driver.quit()
   ```

7. **Wait for Dynamic Content** - Use waits, not sleep
   ```python
   # Good
   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "element")))
   
   # Avoid
   import time
   time.sleep(5)
   ```

### ❌ DON'Ts

1. **Don't use hardcoded waits**
   ```python
   # Avoid
   time.sleep(5)
   ```

2. **Don't embed locators in tests**
   ```python
   # Avoid
   element = driver.find_element(By.XPATH, "//div/p/span/button[@id='login']")
   
   # Use POM instead
   element = login_page.login_button
   ```

3. **Don't ignore exceptions**
   ```python
   # Avoid
   try:
       element.click()
   except:
       pass
   ```

4. **Don't use generic XPaths**
   ```python
   # Avoid
   driver.find_element(By.XPATH, "//*")
   
   # Better
   driver.find_element(By.ID, "username")
   ```

5. **Don't forget to close the browser**
   ```python
   # Always include
   driver.quit()
   ```

---

## Features & Limitations

### ⭐ Features

- ✅ Multi-browser and multi-language support
- ✅ Cross-platform compatibility
- ✅ Parallel test execution
- ✅ Advanced user interaction simulation
- ✅ Dynamic element handling
- ✅ Alert and popup handling
- ✅ Cookie management
- ✅ Screenshot and video capture
- ✅ JavaScript execution
- ✅ Mobile browser automation (with Appium)
- ✅ CI/CD integration

### ⚠️ Limitations

- ❌ Web applications only (not for desktop apps)
- ❌ Limited mobile app support (requires Appium)
- ❌ No built-in reporting (use TestNG, Pytest)
- ❌ Slower than performance testing tools
- ❌ Dynamic element handling can be complex
- ❌ High maintenance for large projects
- ❌ Requires programming knowledge
- ❌ Limited cross-browser consistency

---

## Real-World Applications

1. **Regression Testing** - Verify new changes don't break existing features
2. **Functional Testing** - Validate application features work correctly
3. **Cross-Browser Testing** - Ensure consistent behavior across browsers
4. **Data Web Scraping** - Extract data from dynamic websites
5. **Continuous Integration** - Automated testing in CI/CD pipelines
6. **User Journey Testing** - Simulate complete user workflows
7. **Performance Monitoring** - Track page load behavior
8. **Automated Task Execution** - Schedule repetitive web tasks

---

## Sample Test Script

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Initialize driver
driver = webdriver.Chrome()

try:
    # Navigate to website
    driver.get("https://www.google.com")
    
    # Wait for search box and enter text
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium Python")
    
    # Submit search
    search_box.submit()
    
    # Wait for results
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g"))
    )
    
    # Verify results
    assert "Selenium" in driver.title
    print("✅ Test Passed!")
    
except TimeoutException:
    print("❌ Test Failed: Timeout")
finally:
    driver.quit()
```

---

## Resources

- **Official Documentation**: [Selenium Python Docs](https://selenium-python.readthedocs.io/)
- **WebDriver API**: [W3C WebDriver Specification](https://w3c.github.io/webdriver/)
- **Community**: [Selenium GitHub](https://github.com/SeleniumHQ/selenium)

---

## License

This project is open source and available for educational purposes.

---

## Contributing

Feel free to fork, modify, and submit improvements to this Selenium automation framework!

---

**Last Updated**: March 2026  
**Version**: 1.0
