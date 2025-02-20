import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs
from locators.logo_locators import Logo_locators
from locators.order_locators import Order_locators


class LogoPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие браузера")
    def open_browser(self, driver):
        driver.get(URLs.MAIN_PAGE_URL)
        return self

    @allure.step("Нажатие на кнопку Заказать в шапке лендинга")
    def click_order_button(self, driver):
        driver.find_element(*Order_locators.ORDER_BUTTON_UP).click()
        return self

    @allure.step("Нажатие на логотип Самоката")
    def click_scooter_logo(self, driver):
        driver.find_element(*Logo_locators.SCOOTER_BUTTON).click()
        return self

    @allure.step("Нажатие на логотип Яндекса")
    def click_yandex_logo(self, driver):
        driver.find_element(*Logo_locators.YANDEX_BUTTON).click()
        return self

    @allure.step("Открытие главной страницы Дзена в новом окне")
    def switching_to_the_new_window(self, driver):
        driver.switch_to.window(driver.window_handles[1])
        return self

    @allure.step("Проверка URL страницы Дзена")
    def check_dzen_url(self, driver):
        WebDriverWait(driver, 10).until(
            EC.url_to_be(URLs.DZEN_URL))
        assert driver.current_url == URLs.DZEN_URL
        return self

    @allure.step("Проверка URL страницы после нажатия на Самокат")
    def check_main_page_url(self, driver):
        assert driver.current_url == URLs.MAIN_PAGE_URL
        return self