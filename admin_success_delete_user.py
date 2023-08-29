from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import random
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

print("Sending credentials")
username_field.send_keys("Admin")
password_field.send_keys("admin123")

print("Logging in")
login_button.click()

try:
    alert = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text")
    print("Login failed")
except:
    print("Login success")

print("Opening Admin Management page")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")

print("Getting user data")
data_raw = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
users = [data.text.split('\n')[0] for data in data_raw]

print("Picking random user to delete")
user = random.choice(users)

while user == "Admin":
    user = random.choice(users)

cards = driver.find_elements(By.CLASS_NAME, "oxd-table-card")

print("Deleting user " + user)
try:
    print("Searching for " + user)
    for card in cards:
        if user in card.text:
            print("User " + user + " found")
            print("Searching for delete button")
            delete_button = card.find_element(By.CLASS_NAME, "bi-trash")

            print("Clicking delete button")
            delete_button.click()

            print("Searching confirm delete button")
            confirm_delete_button = driver.find_element(By.CLASS_NAME, "oxd-button--label-danger")

            print("Clicking confirm delete button")
            confirm_delete_button.click()

            time.sleep(5)

            print("Getting updated user data")
            data_raw_new = driver.find_elements(By.CLASS_NAME, "data")
            users_new = data_raw_new[::4]

            print("Validating deletion of user")
            user_is_found = False
            for user_new in users_new:
                if user == user_new.text:
                    print("User " + user + " is not deleted")
                    user_found = True

            if not user_is_found:
                print("User successfully deleted")
                break

except:
    print("User not found, deletion failed")

time.sleep(3)
