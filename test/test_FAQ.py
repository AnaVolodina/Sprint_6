import pytest
import allure
from data import Questions_and_answers


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку перед вопросом открывается соответствующий ответ')
    @pytest.mark.parametrize('index, question, answer', Questions_and_answers.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, questions_page, index, question, answer):
        questions_page.open_page()
        questions_page.close_cookie_popup()
        questions_page.scroll_to_faq()
        question_text = questions_page.get_question_text(index)
        answer_text = questions_page.get_answer_text(index)
        # Проверяем, что текст вопроса соответствует ожидаемому
        assert question_text == question
        # Проверяем, что текст ответа соответствует ожидаемому
        assert answer_text == answer