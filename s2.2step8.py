from selenium import webdriver
import os
import time
try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
   
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys('My name')
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys('My last name')
    input3 = browser.find_element_by_name("email")
    input3.send_keys('My email')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "pop.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)
    option1 = browser.find_element_by_class_name("btn.btn-primary")
    option1.click()
finally:
    time.sleep(5)
    browser.quit()
