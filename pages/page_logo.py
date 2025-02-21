import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.logo_locators import Logo_locators
from locators.order_locators import Order_locators
from pages.base_page import BasePage


class LogoPage(BasePage):
    def __init__(self, driver: WebDriver, base_url: str):
        super().__init__(driver, base_url) # Передаем base_url в BasePage
        self.base_url = base_url

    @allure.step("Открытие страницы")
    def open_page(self):  # Реализация абстрактного метода
        self.driver.get(self.base_url)

    @allure.step("Нажатие на кнопку Заказать в шапке лендинга")
    def click_order_button(self):
        self.find_element(Order_locators.ORDER_BUTTON_UP).click()

    @allure.step("Нажатие на логотип Самоката")
    def click_scooter_logo(self):
        self.find_element(Logo_locators.SCOOTER_BUTTON).click()

    @allure.step("Нажатие на логотип Яндекса")
    def click_yandex_logo(self):
        self.find_element(Logo_locators.YANDEX_BUTTON).click()

    @allure.step("Переключение на новое окно")
    def switch_to_the_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


    @allure.step("Проверка URL страницы Дзена")
    def check_dzen_url(self):
        self.find_element(Logo_locators.DZEN_LOGO)
        return self.driver.current_url


    @allure.step("Проверка URL страницы после нажатия на Самокат")
    def check_main_page_url(self):
        return self.driver.current_url
