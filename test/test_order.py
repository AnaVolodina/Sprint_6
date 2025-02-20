import allure
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # Добавляем родительскую директорию (корень проекта)
from data import OrderData
from pages.page_order import OrderPage


class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, order_data', [('click_up_order_button', OrderData.FIRST_ORDER),
                                                           ('click_down_order_button', OrderData.SECOND_ORDER)])
    def test_make_an_order(self, driver, order_data, button_method):
        page = OrderPage(driver)
        page.open_browser(driver)
        page.close_cookie_popup(driver)
        # Клик по кнопке "Заказать" в шапке лендинга и в нижней части страницы через параметр button_method
        getattr(page, button_method)(driver)
        # Заполнение полей для заказа самоката через параметр order_data
        page.user_order(driver, **order_data)
        # Проверка окна подтверждения по тексту "Заказ оформлен"
        page.confirmation_window(driver)
