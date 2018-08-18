from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# set chrome headless
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)

# scrape sites
url = "https://freecodecamp.org/"
usernames = ["123vivekr", "isht3", "ak04"]

# points holder
points = []

for username in usernames:
    browser.get(url + username)
    browser.implicitly_wait(30)
    point = browser.find_element_by_class_name('points').text
    points.append({username: point[:-7]})

print(points)