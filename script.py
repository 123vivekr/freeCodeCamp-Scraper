from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
# import re
# import pandas as pd
import os

#launch url
url = "https://www.freecodecamp.org/123vivekr"

# create a new Firefox session
# driver = webdriver.Chrome()
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

python_button = driver.find_element_by_class_name('points')
print(python_button)
# python_button.click() #click fhsu link