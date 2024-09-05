from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

linkedin_email = os.environ["EMAIL"]
linkedin_password = os.environ["PASSWORD"]
url = "https://www.linkedin.com/jobs/search/?currentJobId=4003266498&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_LOCATION_SUGGESTION&refresh=true"

# Keep Chrome browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

# Pause to allow page to load
time.sleep(5)  # Wait for the page to load (adjust time if necessary)

# Locate the sign-in button by class name and click it
sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()

username = driver.find_element(By.ID, "username")
username.send_keys(linkedin_email)

password = driver.find_element(By.ID, "password")
password.send_keys(linkedin_password, Keys.ENTER)

jobs_button = driver.find_element(By.CLASS_NAME, "t-12 break-words block t-black--light t-normalglobal-nav__primary-link-text")
jobs_button.click()
