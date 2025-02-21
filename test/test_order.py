import allure
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительскую директорию (корень проекта)
from data import OrderData



class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, order_data', [('click_up_order_button', OrderData.FIRST_ORDER),
                                                           ('click_down_order_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, order_page, order_data, button_method):
        order_page.open_page()
        order_page.close_cookie_popup()
        # Клик по кнопке "Заказать" в шапке лендинга и в нижней части страницы через параметр button_method
        getattr(order_page, button_method)()
        # Заполнение полей для заказа самоката через параметр order_data
        order_page.user_order(**order_data)
        # Проверка окна подтверждения по тексту "Заказ оформлен"
        order_page.confirmation_window()
        message_text = order_page.confirmation_window()
        assert 'Заказ оформлен' in message_text
