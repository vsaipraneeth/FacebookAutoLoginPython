from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser=webdriver.Chrome()
userName='EnterYourFacebookUserName' 
userPassword='EnterYourFacebookPassword'

#change value of userName variable to your facebook username.

#change value of userPassword variable to your facebook password.

browser.get(('https://www.facebook.com/'))
username=browser.find_element_by_id('email')
username.send_keys(userName)
password=browser.find_element_by_id('pass')
password.send_keys(userPassword)
login=browser.find_element_by_id('loginbutton')
login.click()
