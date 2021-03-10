from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    browser.find_element_by_css_selector('button[type="submit"]').click()
    browser.switch_to.alert.accept()
    x = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(str(calc(x)))
    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()