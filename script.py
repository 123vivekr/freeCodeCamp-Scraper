from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

# set chrome headless
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)

# get usernames
with open("user_names.txt") as file:
    usernames = file.read().split('\n')

# scrape site
url = "https://freecodecamp.org/"

# points holder
points = []

# scape user points
for username in usernames:
    browser.get(url + username)
    browser.implicitly_wait(10)
    point = browser.find_element_by_class_name('points').text
    points.append({
        username: username,
        "points": point[:-7]
    })

# output to file as json
with open("output.json", "w") as file:
    json.dump(points, file, indent=4, ensure_ascii=False)