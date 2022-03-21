from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    option1 = browser.find_element_by_class_name("trollface.btn.btn-primary")
    option1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    answer.send_keys(str(math.log(abs(12*math.sin(int(x))))))
    option2 = browser.find_element_by_class_name("btn.btn-primary")
    option2.click()
finally:
    time.sleep(5)
    browser.quit()
