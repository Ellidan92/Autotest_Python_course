from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get('http://SunInJuly.github.io/execute_script.html')

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    x = int(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(str(calc(x)))
    browser.find_element_by_id('robotCheckbox').click()
    radio = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    browser.find_element_by_css_selector("button[type='submit']").click()

finally:
   time.sleep(10)
   browser.quit()