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

print("Opening Personnel Information Management page")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

print("Getting user data")
data_raw = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
users = [data.text.split('\n')[0:3] for data in data_raw]

print("Picking random user to edit")
user = random.choice(users)

cards = driver.find_elements(By.CLASS_NAME, "oxd-table-card")

try:
    print("Searching for user with ID " + user[0])
    for card in cards:
        card_id = card.text.split("\n")[0]
        if user[0] == card_id:
            print("User with ID " + user[0] + " found")
            print("Searching for edit button")
            edit_button = card.find_element(By.CLASS_NAME, "bi-pencil-fill")

            print("Clicking edit button")
            edit_button.click()

            print("Searching for first name field")
            first_name_field = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
            first_name = first_name_field.get_attribute("value")

            print("Searching for middle name field")
            middle_name_field = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input")
            middle_name = middle_name_field.get_attribute("value")

            print("Searching for last name field")
            last_name_field = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input")
            last_name = last_name_field.get_attribute("value")
            
            time.sleep(3)
            full_name = first_name + " " + middle_name + " " + last_name
            new_name = last_name + " " + middle_name + " " + first_name

            print(full_name)
            print(new_name)

            print("Editing the name to '" + new_name +"'")
            for i in range(len(new_name)):
                first_name_field.send_keys(Keys.BACKSPACE)
            
            first_name_field.send_keys(last_name)

            for i in range(len(new_name)):
                last_name_field.send_keys(Keys.BACKSPACE)
            
            last_name_field.send_keys(first_name)
            
            time.sleep(3)

            print("Searching for save button")
            save_button = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div.oxd-form-actions > button")

            print("Clicking save button")
            save_button.click()
            time.sleep(5)

            print("Returning to the PIM page")
            driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

            time.sleep(5)

            print("Getting updated user data")
            data_raw_update = driver.find_elements(By.CLASS_NAME, "oxd-table-card")
            users_update = [data.text.split('\n')[0:3] for data in data_raw_update]

            print("Validating edit of user")
            user_is_edited = False
            for user_new in users_update:
                if user[0] == user_new[0]:
                    print("User " + new_name + " found")

                    print("Checking if the name is changed")
                    if full_name != new_name:
                        print("Old name: " + full_name)
                        print("New name: " + new_name)
                        user_is_edited = True
                        break

            if user_is_edited:
                print("User successfully edited")
                break
        

except:
    print("User not found, edit failed")

time.sleep(3)
