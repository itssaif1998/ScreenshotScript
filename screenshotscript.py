import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

#To open his profile
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.facebook.com')
email = driver.find_element_by_name("email")
email.send_keys("saif.mir123@yahoo.co.in")
password = driver.find_element_by_name("pass")
password.send_keys('l19b1r9l6')
password.send_keys(Keys.ENTER)
driver.get('https://www.facebook.com/dickson.dokowe')

#For Scroll
SCROLL_PAUSE_TIME = 1.5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#To take a screenshot
pic = pyautogui.screenshot(region=(300,500, 800, 600))
pic.save('TheLie.png')

#To upload the image
uploadElement = driver.find_element_by_id('uploadfile_0')
