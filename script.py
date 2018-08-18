from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

class Points():

    def __init__(self):
        self.url = "https://freecodecamp.org/"
        self.usernames = []
        fieldnames = ["user_name", "initial_points", "current_points"]
        csvfile = open('usernames.csv', 'w', newline='')
        self.writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        self.writer.writeheader()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

    def add_username(self, username):
        initial_point = self.get_points(username)
        self.writer.writerow({'user_name': username, "initial_points": initial_point})
    
    def get_points(self, username):
        self.browser.get(self.url + username)
        self.browser.implicitly_wait(30)
        point = self.browser.find_element_by_class_name('points').text
        return point