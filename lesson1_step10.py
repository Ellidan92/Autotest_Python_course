from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

try:
    number = browser.find_element_by_id('treasure').get_attribute('valuex')
    browser.find_element_by_id('answer').send_keys(calc(number))
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button[type="submit"]').click()
finally:
    time.sleep(10)
    browser.quit()