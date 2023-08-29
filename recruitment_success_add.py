from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import random
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
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

print("Opening Recruitment page")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

print("Searching for Add button")
add_button = driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-header-container > button")

print("Clicking Add button")
add_button.click()

names = ['James', 'John', 'Robert', 'Maria', 'Jim', 'Sigma', 'Joko', 'Suprapto', 'Bambang',
         'Olivia', 'Cook', 'Tyler', 'Handerson', 'Rizky', 'Vivi', 'Rose', '田中', '茂', '山田',
         '小町', '高木', 'ねね', 'こぼ', '星野', '光る','中村']

print("Generating a random name")
first_name = random.choice(names)
names.remove(first_name)
middle_name = random.choice(names)
names.remove(middle_name)
last_name = random.choice(names)

full_name = first_name + " " + middle_name + " " + last_name
print("The generated name is ", full_name)

print("Getting the name fields")
first_name_field = driver.find_element(By.NAME, 'firstName')
middle_name_field = driver.find_element(By.NAME, 'middleName')
last_name_field = driver.find_element(By.NAME, 'lastName')


print("Filling in the name fields")
first_name_field.send_keys(first_name)
middle_name_field.send_keys(middle_name)
last_name_field.send_keys(last_name)

time.sleep(1)
print("Selecting vacancy")
vacancy_button = driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div')
vacancy_button.click()
time.sleep(1)

vacancy_list = driver.find_elements(By.CLASS_NAME, 'oxd-select-option')
vacancy_list = vacancy_list[1:]
random.choice(vacancy_list).click()

print("Generating new email")
email_list = ['real','cool','person','kind','slay','sigma','giga','handsome']
email1 = random.choice(email_list)
email_list.remove(email1)
email2 = random.choice(email_list)
email = email1 + email2 + str(random.randint(0,999))+ "@gmail.com"

print("The generated email is ", email)

print("Filling in email")
email_field = driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(3) > div > div:nth-child(1) > div > div:nth-child(2) > input')
email_field.send_keys(email)

print("Generating contact number")
contact_number = "0812" + str(random.randint(11111111,99999999))

print("The generated contact number is ", contact_number)

print("Filling in contact number")
contact_number_field = driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div:nth-child(3) > div > div:nth-child(2) > div > div:nth-child(2) > input')
contact_number_field.send_keys(contact_number)

print("Searching for save button")
save_button = driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space')

print("Saving recruitment info")
save_button.click()

print("Validating if the recruitment info is saved")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")

cards = driver.find_elements(By.CLASS_NAME, "oxd-table-card")

try:
    print("Searching for user with name " + full_name)
    for card in cards:
        candidate_name = card.text.split("\n")[1]
        if full_name == candidate_name:
            print("User with name " + full_name + " found")
            break
except:
    print("User not found, add new recruitment failed")



time.sleep(3)
