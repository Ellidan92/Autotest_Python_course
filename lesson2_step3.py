from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')
try:
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)
    Select(browser.find_element_by_id('dropdown')).select_by_value(str(num1+num2))
    browser.find_element_by_css_selector('button[type = "submit"]').click()

finally:
    time.sleep(5)
    browser.quit()