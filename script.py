from selenium import webdriver

url = "https://freecodecamp.org/"
usernames = ["123vivekr", "isht3", "ak04"]
browser = webdriver.PhantomJS()
points = []

for username in usernames:
    browser.get(url + username)
    browser.implicitly_wait(30)
    point = browser.find_element_by_class_name('points').text
    points.append({username: point[:-7]})

print(points)