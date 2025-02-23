import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.logo_locators import Logo_locators
from locators.order_locators import Order_locators
from pages.base_page import BasePage
from data import URLs

class LogoPage(BasePage):
    def __init__(self, driver: WebDriver, base_url: str):
        super().__init__(driver, base_url) # Передаем base_url в BasePage
        self.base_url = base_url

    @allure.step("Открытие страницы")
    def open_page(self):  # Реализация абстрактного метода
        super().open_page()

    @allure.step("Нажатие на кнопку Заказать в шапке лендинга")
    def click_order_button(self):
        self.click_element(Order_locators.ORDER_BUTTON_UP)

    @allure.step("Нажатие на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(Logo_locators.SCOOTER_BUTTON)

    @allure.step("Нажатие на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(Logo_locators.YANDEX_BUTTON)

    @allure.step("Переключение на новое окно")
    def switch_to_the_new_window(self, expected_url):
        self.switch_to_window(expected_url)



    @allure.step("Проверка URL страницы Дзена")
    def check_dzen_url(self):
        return self.check_url


    @allure.step("Проверка URL страницы после нажатия на Самокат")
    def check_main_page_url(self):
        self.click_element(Logo_locators.SCOOTER_BUTTON)
        return self.check_url
