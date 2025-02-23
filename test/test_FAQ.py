import pytest
import allure
from locators.FAQ_locators import FAQ_Locators
from data import expected_texts


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку перед вопросом открывается соответствующий ответ')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', [
        (FAQ_Locators.ACCORDION_BUTTON_FAQ_1, FAQ_Locators.ANSWER_FAQ_1, expected_texts['1']),
        (FAQ_Locators.ACCORDION_BUTTON_FAQ_2, FAQ_Locators.ANSWER_FAQ_2, expected_texts['2']),
        (FAQ_Locators.ACCORDION_BUTTON_FAQ_3, FAQ_Locators.ANSWER_FAQ_3, expected_texts['3']),
        (FAQ_Locators.ACCORDION_BUTTON_FAQ_4, FAQ_Locators.ANSWER_FAQ_4, expected_texts['4']),
        (FAQ_Locators.ACCORDION_BUTTON_FAQ_5, FAQ_Locators.ANSWER_FAQ_5, expected_texts['5']),
        (FAQ_Locators.ACCORDION_BUTTON_FAQ_6, FAQ_Locators.ANSWER_FAQ_6, expected_texts['6']),
        (FAQ_Locators.ACCORDION_BUTTON_FAQ_7, FAQ_Locators.ANSWER_FAQ_7, expected_texts['7']),
        (FAQ_Locators.ACCORDION_BUTTON_FAQ_8, FAQ_Locators.ANSWER_FAQ_8, expected_texts['8'])

    ])
    def test_check_question_and_answer(self, questions_page, question_locator, answer_locator, expected_text):
        questions_page.open_page()
        questions_page.close_cookie_popup()
        questions_page.scroll_to_faq()
        questions_page.click_the_question(question_locator)
        answer = questions_page.get_the_answer_text(answer_locator)
        assert answer == expected_text
