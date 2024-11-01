# import selenium
# from selenium.webdriver.common.by import By
# browser=selenium.webdriver.Chrome()
# browser.get("https://www.seleniumhq.org")
# elem=browser.find_element(By.LINK_TEXT,'Downloads')
# search=browser.find_element(By.ID,'q')
# search.send_keys('Downloads')
# elem.click()
# input()
# browser.quit()

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://web.whatsapp.com")
wait=WebDriverWait(driver,600)
target='"Bhanu"'  #friend's name
string="Hii.."    #message
x_arg="//span[contains(@title, "+ target+")]"
target=wait.until(ec.presence_of_element_located((By.XPATH,x_arg)))
target.click()
input_box=driver.find_element(By.CLASS_NAME,'_ak1r')
for i in range(50):
    input_box.send_keys(string+Keys.ENTER)