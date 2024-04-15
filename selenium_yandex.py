
import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('config.json') as config_file:
    config_data = json.load(config_file)

Username = config_data['credentials']['username']
Password = config_data['credentials']['password']

class TestYandexAuthorization(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)  # Ждем, пока элементы загрузятся
        self.driver.maximize_window()

    def test_authorization(self):
        self.driver.get("https://passport.yandex.ru/auth/")

        login_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "passp-field-login"))
        )
        login_field.send_keys(Username)  # Замените на Ваш логин
        login_field.send_keys(Keys.RETURN)

        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "passp-field-passwd"))
        )
        password_field.send_keys(Password)  # Замените на Ваш пароль
        password_field.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 30).until(
            EC.url_contains("https://id.yandex.ru")
        )

        print("Current URL:", self.driver.current_url)  # Вывод текущего URL

        assert "https://id.yandex.ru" in self.driver.current_url

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()