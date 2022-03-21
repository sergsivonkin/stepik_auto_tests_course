from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = "http://suninjuly.github.io/cats.html"
browser.get(link)
option = browser.find_element_by_id("button")
