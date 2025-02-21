from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from abc import ABC, abstractmethod
from selenium.common.exceptions import TimeoutException


class BasePage(ABC):
    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url

    @abstractmethod
    def open_page(self):
        pass

    def find_element(self, locator: tuple, timeout: int = 10):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            print(f"Элемент с локатором {locator} не найден за {timeout} секунд.")
            raise

    def click_element(self, locator: tuple, timeout: int = 10):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except Exception as e:
            print(f"Не удалось кликнуть на элемент с локатором {locator} за {timeout} секунд.")
            raise  # Перевыбрасываем исключение, чтобы тест упал

    def send_keys_to_element(self, locator: tuple, text: str, timeout: int = 10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            element.send_keys(text)
        except Exception as e:
            print(f"Не удалось ввести текст в элемент с локатором {locator} за {timeout} секунд.")
            raise  # Перевыбрасываем исключение, чтобы тест упал

    def get_element_text(self, locator: tuple, timeout: int = 10) -> str:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            return element.text
        except Exception as e:
            print(f"Не удалось получить текст элемента с локатором {locator} за {timeout} секунд.")
            raise  # Перевыбрасываем исключение, чтобы тест упал


    def execute_script(self, script, element):
        self.driver.execute_script(script, element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))


    def get_current_url(self):
        return self.driver.current_url

    def check_url(self, expected_url, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
            return True  # URL соответствует ожидаемому
        except TimeoutException:
            print(f"URL did not change to {expected_url} in {timeout} seconds")
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

        except TimeoutException as e:
            print(f"Timeout or URL mismatch: {e}")
            return False
