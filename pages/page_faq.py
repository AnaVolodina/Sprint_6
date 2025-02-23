import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.FAQ_locators import FAQ_Locators
from pages.base_page import BasePage
from data import URLs


class QuestionsPage(BasePage):
    def __init__(self, driver: WebDriver, base_url: str):
        super().__init__(driver, base_url) # Передаем base_url в BasePage

    @allure.step("Открытие страницы")
    def open_page(self):  # Реализация абстрактного метода
        super().open_page()

    @allure.step("Закрытие всплывающего окна cookie (если есть)")
    def close_cookie_popup(self):
        self.click_element(FAQ_Locators.COOKIE_BUTTON_LOCATOR)

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self):
        self.scroll_to_element(FAQ_Locators.ACCORDION)

    @allure.step('Клик по вопросу')
    def click_the_question(self, question_locator):
        self.find_element(question_locator)
        self.click_element(question_locator)


    @allure.step('Получение текста ответа')
    def get_the_answer_text(self, answer_locator):
        self.find_element(answer_locator)
        answer_text = self.get_element_text(answer_locator)
        return answer_text



