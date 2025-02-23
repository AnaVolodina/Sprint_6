import allure
from data import URLs


class TestLogoPage:
    @allure.title('Проверка URL после нажатия на логотип Самоката')
    def test_url_scooter_logo(self, logo_page):
        logo_page.open_page()
        logo_page.click_order_button()
        logo_page.click_scooter_logo()
        expected_main_url = URLs.BASE_URL
        logo_page.check_main_page_url()
        actual_url = logo_page.get_current_url()
        assert actual_url == expected_main_url


    @allure.title('Проверка URL после нажатия на логотип Яндекса')
    def test_url_yandex_logo(self, logo_page):
        logo_page.open_page()
        logo_page.click_yandex_logo()
        expected_url = URLs.DZEN_URL
        logo_page.switch_to_the_new_window(expected_url)
        logo_page.check_dzen_url()
        actual_url = logo_page.get_current_url()
        assert actual_url == expected_url









