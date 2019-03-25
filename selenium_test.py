from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time



from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://54.71.52.140/")
element =driver.find_element_by_link_text('About Us')
driver.implicitly_wait(5)

element.click()

print(driver.title)
print("Selenium Test Sucessful")
#print(driver.content)
time.sleep(8)

