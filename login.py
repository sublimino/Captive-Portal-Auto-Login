import sys
import os

from selenium import webdriver


driver = webdriver.Firefox()

URL = os.getenv('PORTAL_URL')
USER = os.getenv('PORTAL_USER')
USER_ELEMENT = os.getenv('PORTAL_USER_ELEMENT_NAME', "username")
PASS = os.getenv('PORTAL_PASS', '')
PASS_ELEMENT = os.getenv('PORTAL_PASS_ELEMENT_NAME', "password")
SUBMIT_ELEMENT_ID = os.getenv('PORTAL_SUBMIT_ELEMENT_ID')

try:
    driver.get(URL)
except:
	sys.exit(0)

username = driver.find_element_by_name(USER_ELEMENT)
username.clear()
username.send_keys(USER)

if PASS != "":
    password = driver.find_element_by_name(PASS_ELEMENT)
    password.clear()
    password.send_keys(PASS)

driver.find_element_by_id(SUBMIT_ELEMENT_ID).click()

print("Logged In.")

driver.close()
