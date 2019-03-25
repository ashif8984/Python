'''
This Script does the selenium tests for a webpage and click link

Prerequites:
    1. Install python and pip module
    2. Set the python enviornment variable
    3. Install selenium (pip install selenium)
    4. Install geckodriver for firefox browser & paste the geckdriver.exe under Script folder of Python

'''

# importing selenium modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time



from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

#WebPage to Test
driver.get("http://54.71.52.140/")

#Selecting the Element to Test(here href element)
element =driver.find_element_by_link_text('About Us')
driver.implicitly_wait(5) #wait for 5 seconds

element.click()

print(driver.title)
print("Selenium Test Sucessful")
#print(driver.content)
time.sleep(8)

