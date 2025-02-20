import allure
import pytest
from pages.page_faq import QuestionsPage
from data import Questions_and_answers


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку перед вопросом открывается соответствующий ответ')
    @pytest.mark.parametrize('index, question, answer', Questions_and_answers.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, driver, index, question, answer):
        page = QuestionsPage(driver)
        page.open_browser(driver)
        page.close_cookie_popup(driver)
        page.scroll_to_faq(driver)
        question_text = page.get_question(driver, index)
        answer_text = page.get_answer(driver, index)
        # Проверяем, что текст вопроса соответствует ожидаемому
        assert question_text == question
        # Проверяем, что текст ответа соответствует ожидаемому
        assert answer_text == answer