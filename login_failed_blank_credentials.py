from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
print("Opening website link")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.implicitly_wait(5)
driver.maximize_window()

print("Searching for username field")
username_field = driver.find_element(By.NAME, "username")

print("Searching for password field")
password_field = driver.find_element(By.NAME, "password")

print("Searching for login button")
login_button = driver.find_element(By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")

print("Logging in")
login_button.click()

try:
    alert = driver.find_element(By.CLASS_NAME, "oxd-input-field-error-message")
    print("Login failed - " + alert.text)
except:
    print("Login success")

time.sleep(3)
