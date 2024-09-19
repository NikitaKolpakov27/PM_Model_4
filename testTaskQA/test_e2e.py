import os
import unittest
import time
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv('./.env')

user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
first_name = os.getenv('FIRST_NAME')
last_name = os.getenv('LAST_NAME')
zip_code = os.getenv('ZIP_CODE')

class MainTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge()
        self.addCleanup(self.browser.quit)

    def test(self):
        self.browser.get('https://www.saucedemo.com/')

        # Находим поле для ввода логина и вводим данные
        self.browser.find_element("id", "user-name").send_keys(user_name)
        time.sleep(0.3)

        # То же самое для пароля
        self.browser.find_element("id", "password").send_keys(password)
        time.sleep(0.3)

        # Находим кнопку и жмем ее
        self.browser.find_element("id", "login-button").submit()
        time.sleep(0.3)

        # Добавляем товар в корзину
        self.browser.find_element("id", "add-to-cart-sauce-labs-backpack").click()
        time.sleep(0.3)

        # Переходим в корзину
        self.browser.find_element("id", "shopping_cart_container").click()
        time.sleep(0.3)

        # Переходим к оплате
        self.browser.find_element("id", "checkout").click()
        time.sleep(0.3)

        # Вводим данные для оплаты
        self.browser.find_element("id", "first-name").send_keys(first_name)
        self.browser.find_element("id", "last-name").send_keys(last_name)
        self.browser.find_element("id", "postal-code").send_keys(zip_code)
        self.browser.find_element("id", "continue").click()

        self.browser.find_element("id", "finish").click()
        time.sleep(0.3)

        # Проверяем, есть ли на странице текст, обозначающий, что покупка завершена успешно
        self.assertTrue(self.browser.page_source.__contains__("Thank you for your order!"))
        self.browser.find_element("id", "back-to-products").click()
        time.sleep(0.3)


if __name__ == '__main__':
    unittest.main()
