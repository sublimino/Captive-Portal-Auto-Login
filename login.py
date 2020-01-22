import sys
import os

from selenium import webdriver


driver = webdriver.Firefox()

URL = os.getenv('PORTAL_URL')
USER = os.environ.get('PORTAL_USER')

try:
    driver.get(URL)
except:
	sys.exit(0)

username = driver.find_element_by_name("username")
username.clear()

username.send_keys(USER)

driver.find_element_by_id("submitbutton").click()

print("Logged In.")

driver.close()
