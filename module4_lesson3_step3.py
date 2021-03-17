import pytest
from selenium import webdriver
import time
import math

def right_answer():
    return str(math.log(int(time.time()+96.7)))

@pytest.mark.parametrize('link_number', ['236895','236896','236897','236897','236898','236899','236903','236904','236905'])
def test_url_aliens(link_number):

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(f'https://stepik.org/lesson/{link_number}/step/1')
    browser.find_element_by_css_selector('textarea[placeholder = "Напишите ваш ответ здесь..."]').send_keys(right_answer())
    browser.find_element_by_class_name("submit-submission").click()
    status_message = browser.find_element_by_css_selector('pre[class = "smart-hints__hint"]').text
    browser.quit()
    assert status_message == "Correct!", f"{status_message} != Correct!"
