import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs
from locators.FAQ_locators import FAQ_Locators


class QuestionsPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие браузера")
    def open_browser(self, driver):
        driver.get(URLs.MAIN_PAGE_URL)
        return self

    @allure.step("Закрытие всплывающего окна cookie (если есть)")
    def close_cookie_popup (self, driver):
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(FAQ_Locators.COOKIE_BUTTON_LOCATOR)
        )
        cookie_button.click()
        return self

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self, driver):
        element = driver.find_element(By.CLASS_NAME, "accordion")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self

    @allure.step("Получение текста вопроса")
    def get_question(self, driver, index):
        question_locator = (FAQ_Locators.QUESTION[0], FAQ_Locators.QUESTION[1].format(index))
        question = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(question_locator))
        question.click()
        return question.text

    @allure.step("Получение текста ответа")
    def get_answer(self, driver, index):
        answer_locator = (FAQ_Locators.ANSWER[0], FAQ_Locators.ANSWER[1].format(index))
        answer = driver.find_element(*answer_locator)
        return answer.text

