import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.FAQ_locators import FAQ_Locators
from pages.base_page import BasePage


class QuestionsPage(BasePage):
    def __init__(self, driver: WebDriver, base_url: str):
        super().__init__(driver, base_url) # Передаем base_url в BasePage
        self.base_url = base_url

    @allure.step("Открытие страницы")
    def open_page(self):  # Реализация абстрактного метода
       self.driver.get(self.base_url)

    @allure.step("Закрытие всплывающего окна cookie (если есть)")
    def close_cookie_popup(self):
        cookie_button = self.find_element(FAQ_Locators.COOKIE_BUTTON_LOCATOR)
        if cookie_button:
            cookie_button.click()

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self):
        element = self.find_element(FAQ_Locators.ACCORDION)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Получение текста вопроса")
    def get_question_text(self, index):
        question_locator = (FAQ_Locators.QUESTION[0], FAQ_Locators.QUESTION[1].format(index))
        question = self.find_element(question_locator)
        if question:
            question.click()
            return question.text
        else:
            return None

    @allure.step("Получение текста ответа")
    def get_answer_text(self, index):
        locator = (FAQ_Locators.ANSWER[0], FAQ_Locators.ANSWER[1].format(index))
        answer = self.find_element(locator)
        return answer.text

