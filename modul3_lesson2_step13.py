from selenium import webdriver
import time
import unittest

class test_registration_form(unittest.TestCase):

    def test_first_form(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        First_name = browser.find_element_by_css_selector("div.first_block div.first_class .first")
        First_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector("div.first_block div.second_class .second")
        last_name.send_keys("Ivanov")
        email = browser.find_element_by_css_selector("div.first_block div.third_class .third")
        email.send_keys('ivan92@yandex.ru')
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f'Wrong text {welcome_text}')
        # закрываем браузер после всех манипуляций
        browser.close()

    def test_second_form(self):
        link = " http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        First_name = browser.find_element_by_css_selector("div.first_block div.first_class .first")
        First_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector("div.first_block div.second_class .second")
        last_name.send_keys("Ivanov")
        email = browser.find_element_by_css_selector("div.first_block div.third_class .third")
        email.send_keys('ivan92@yandex.ru')
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f'Wrong text {welcome_text}')
        # закрываем браузер после всех манипуляций
        browser.quit()
if __name__ == "__main__":
    unittest.main()
