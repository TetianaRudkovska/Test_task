import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the WebDriver 
driver = webdriver.Chrome()

# Opening the website
driver.get("https://www.saucedemo.com")

# Successful login with valid credentials
username = driver.find_element("id", "user-name")
password = driver.find_element("id", "password")
login_button = driver.find_element("id", "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

# Waiting for a while to let the login complete
time.sleep(2)

# Verifying successful login by checking the URL or an element on the next page
if "inventory" in driver.current_url:
    print("Successful login")
else:
    print("Login failed")

# Going back to the login page
driver.get("https://www.saucedemo.com")

# Failed login with invalid credentials
username = driver.find_element("id", "user-name")
password = driver.find_element("id", "password")
login_button = driver.find_element("id", "login-button")

username.send_keys("invalid_user")
password.send_keys("wrong_password")
login_button.click()

# Waiting for a while to let the login complete
time.sleep(2)

# Verifying error message for invalid login attempt
error_message = driver.find_element("css selector", ".error-message-container.error h3").text
if "Username and password do not match any user in this service" in error_message:
    print("Error message displayed correctly")
else:
    print("Error message verification failed")

# Go back to the login page
driver.get("https://www.saucedemo.com")

# Completing a purchase end to end request
username = driver.find_element("id", "user-name")
password = driver.find_element("id", "password")
login_button = driver.find_element("id", "login-button")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

# Waiting for a while to let the login complete
time.sleep(2)


# Close the browser
driver.quit()

