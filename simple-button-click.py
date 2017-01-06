from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'YOUR_USERNAME'
passwordStr = 'YOUR_PASS'

browser = webdriver.Chrome()
browser.get(('http://YOUR_WEB_SITE/login.php'))

username = browser.find_element_by_id('user_login')
username.send_keys(usernameStr)
nextButton = browser.find_element_by_id('user_pass')
nextButton.click()

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'user_login')))
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('user_pass')
signInButton.click()


