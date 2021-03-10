from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    value1 = browser.find_element_by_xpath('//input[@name="first_name"]')
    value1.send_keys('Ivan')
    value2 = browser.find_element_by_xpath('//input[@name="last_name"]')
    value2.send_keys('Petrov')
    value3 = browser.find_element_by_xpath('//input[@name="firstname"]')
    value3.send_keys('Smolensk')
    value4 = browser.find_element_by_xpath('//input[@id="country"]')
    value4.send_keys('Russia')
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
