import allure
import pytest
from pages.page_logo import LogoPage


class TestLogoPage:
    @allure.title('Проверка URL после нажатия на логотип Самоката')
    def test_url_scooter_logo(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open_browser(driver)
        logo_page.click_order_button(driver)
        logo_page.click_scooter_logo(driver)
        logo_page.check_main_page_url(driver)


    @allure.title('Проверка URL после нажатия на логотип Яндекса')
    def test_url_yandex_logo(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open_browser(driver)
        logo_page.click_yandex_logo(driver)
        logo_page.switching_to_the_new_window(driver)
        logo_page.check_dzen_url(driver)


