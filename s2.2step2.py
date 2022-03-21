from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_element = browser.find_element_by_id("num1").text
    x = x_element
    y_element = browser.find_element_by_id("num2").text
    y = y_element
    sum_el = str(int(x)+int(y))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_el)
    time.sleep(1)
    option1 = browser.find_element_by_class_name("btn.btn-default")
    option1.click()
    time.sleep(1)
finally:
    time.sleep(5)
    browser.quit()    
    
