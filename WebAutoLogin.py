from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

with open("details.config" , "r") as details:
    file_data = details.read().split("\n")
    data = {}
    for line in file_data[:-1]:
        line = line.split(": ")
        data[line[0]] = line[1]


# Using Chrome to access web
driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')


# Open the website
driver.get('https://wifi.superloop.com/#!/login')
time.sleep(3)
try:
    go = driver.find_element_by_id('new')
    go.click()
except Exception as e:
    pass
time.sleep(3)

login_button = driver.find_elements_by_xpath('//*[@id="content"]/div/md-toolbar/div/div[5]/button/strong')[0]
login_button.click()


time.sleep(3)

user = driver.find_element_by_xpath('//*[@id="input_5"]')
passwd = driver.find_element_by_xpath('//*[@id="input_6"]')
user.send_keys(data["User"])
passwd.send_keys(data["Password"])
button = driver.find_element_by_xpath('//*[@id="card-0"]/md-card/md-card-content/div/form/section/button')
button.click()
time.sleep(3)
try:
    button = driver.find_element_by_xpath('/html/body/div[1]/md-toolbar/div/span[4]/button[1]')
    button.click()
except:
    pass
time.sleep(3)
driver.close()
exit()
