from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

try:
    browser.find_element_by_name('firstname').send_keys('Ivan')
    browser.find_element_by_name('lastname').send_keys('Ivanov')
    browser.find_element_by_name('email').send_keys('ivanov@yandex.ru')
    browser.find_element_by_id('file').send_keys('C:\\Users\\GSilin\\PycharmProjects\\pythonProject1\\test.txt')
    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    time.sleep(10)
    browser.quit()