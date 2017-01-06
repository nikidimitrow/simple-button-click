from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


usernameStr = 'admin@mosv'
passwordStr = 'k4ssketski'

browser = webdriver.Chrome()
browser.get(('http://10.10.14.220/wp-login.php'))

username = browser.find_element_by_id('user_login')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('user_pass')
nextButton.click()

password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'user_pass')))
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('wp-submit')
signInButton.click()

signInButton = browser.find_element_by_class_name('page-count')
signInButton.click()