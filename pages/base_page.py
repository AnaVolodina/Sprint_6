from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import ABC, abstractmethod
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from data import URLs
from selenium.webdriver.common.keys import Keys
from locators.FAQ_locators import FAQ_Locators
from locators.order_locators import Order_locators


class BasePage(ABC):
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url

    def open_page(self):
       self.driver.get(self.base_url)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise


    def click_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except NoSuchElementException:
            raise


    def send_keys_to_element(self, locator, order_data, timeout: int = 10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            element.send_keys(order_data)
        except NoSuchElementException:
            raise


    def get_element_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            if element:
                return element.text
        except NoSuchElementException:
            raise

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def check_url(self, expected_url, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
            return True  # URL соответствует ожидаемому
        except TimeoutException:
            return False  # URL не соответствует ожидаемому

    def switch_to_window(self, expected_url, timeout: int = 30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(2))
            window_handles = self.driver.window_handles
            new_window_handle = window_handles[-1]
            self.driver.switch_to.window(new_window_handle)
            if expected_url:
                WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
                return self.driver.current_url == expected_url  # Проверяем и возвращаем результат
            return True
        except TimeoutException:
            return False

    def fill_date_field(self, locator, data):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.send_keys(data, Keys.ENTER)
        except NoSuchElementException:
            raise

    def rent_time(self, locator, data):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            select_rent_time_locator = (Order_locators.SELECT_RENT_TIME[0], Order_locators.SELECT_RENT_TIME[1].format(data))
            self.find_element(select_rent_time_locator).click()
        except NoSuchElementException:
            raise
