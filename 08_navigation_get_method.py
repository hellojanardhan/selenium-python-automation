#1.  Navigating Links Using get() Method in Selenium
"""
What is the get() method?

In Selenium , get() method is ysed to open a website
It tell the browser to navigate to a specific URL
Syntax:
    driver.get("https://www.example.com")

What happens internally?
------------------------
1. WebDriver sends a GET request to the server
2. The browsers opens web page
3. Selenium waits until the page is fully loaded
4. Then control returns to the script
"""

#2. Why get() method is important?
"""
Without get() , 
    -> Browser opens
    -> But no website loads
So , get is first setp in most selenium scripts
"""

#3. Example
"""
Explaination:
1. webdriver.Firefox() : Opens Firefox browser
2. driver.get() : Navigates to Google
3. driver.quit() : Closes the browser
"""
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.google.com")
driver.quit()

