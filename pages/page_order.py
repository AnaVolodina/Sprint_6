import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.order_locators import Order_locators
from selenium.webdriver.common.keys import Keys
from locators.FAQ_locators import FAQ_Locators
from pages.base_page import BasePage
from data import URLs
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):
    def __init__(self, driver: WebDriver, base_url: str):
        super().__init__(driver, base_url) # Передаем base_url в BasePage
        self.base_url = base_url

    @allure.step("Открытие страницы")
    def open_page(self):  # Реализация абстрактного метода
        super().open_page()

    @allure.step("Закрытие всплывающего окна cookie (если есть)")
    def close_cookie_popup(self):
        cookie_button = self.find_element(FAQ_Locators.COOKIE_BUTTON_LOCATOR)
        self.click_element(cookie_button)

    @allure.step("Нажатие на кнопку Заказать в шапке лендинга")
    def click_up_order_button(self):
        order_button = self.find_element(Order_locators.ORDER_BUTTON_UP)
        self.click_element(order_button)

    @allure.step("Нажатие на кнопку Заказать в нижней части страницы")
    def click_down_order_button(self):
        self.scroll_to_element(Order_locators.ORDER_BUTTON_DOWN)
        self.click_element(Order_locators.ORDER_BUTTON_DOWN)

    @allure.step("Заполнение поля Имя")
    def fill_name_field(self, text):
        self.send_keys_to_element(Order_locators.NAME, text)

    @allure.step("Заполнение поля Фамилия")
    def fill_surname_field(self, text):
        self.send_keys_to_element(Order_locators.SURNAME, text)

    @allure.step("Заполнение поля Адрес")
    def fill_address_field(self, text):
        self.send_keys_to_element(Order_locators.ADDRESS, text)

    @allure.step("Заполнение поля Станция метро")
    def check_metro_station(self, text):
        self.send_keys_to_element(Order_locators.METRO, text)
        stations_list = self.find_element(Order_locators.LIST_OF_STATIONS)
        self.click_element(stations_list)

    @allure.step("Заполнение поля Телефон")
    def fill_number_field(self, text):
        self.send_keys_to_element(Order_locators.NUMBER, text)

    @allure.step("Нажатие на кнопку Далее")
    def click_next_button(self):
        next_button = self.find_element(Order_locators.NEXT_BUTTON)
        self.click_element(next_button)

    @allure.step("Выбор даты доставки")
    def fill_delivery_date_field(self, text):
        self.fill_date_field(Order_locators.DELIVERY_DATE, text)


    @allure.step("Выбор срока аренды")
    def rental_time(self, text):
        self.rent_time(Order_locators.RENT_TIME, text)


    @allure.step("Выбор цвета")
    def checkbox_color(self, color):
        if color == 'чёрный жемчуг':
            self.click_element(Order_locators.BLACK_COLOR_CHECKBOX)
        elif color == 'серая безысходность':
            self.click_element(Order_locators.GREY_COLOR_CHECKBOX)

    @allure.step("Заполнение поля Комментарии к заказу")
    def comment_for_courier(self, text):
        self.send_keys_to_element(Order_locators.COMMENT, text)

    @allure.step("Нажатие на кнопку Заказать")
    def click_order_button(self):
        order_button = self.find_element(Order_locators.ORDER_BUTTON)
        self.click_element(order_button)

    @allure.step("Нажатие на кнопку 'Да' в окне подтверждения заказа")
    def click_confirmation_button(self):
        confirmation_button = self.find_element(Order_locators.YES_BUTTON)
        self.click_element(confirmation_button)

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self):
        message = self.get_element_text(Order_locators.ORDER_COMPLETED)
        return message

    @allure.step("Полный позитивный сценарий")
    def user_order(self,
                        name, surname, address, metro, number,
                        delivery_date, rent_days, colour, comment):
        self.fill_name_field(name)
        self.fill_surname_field(surname)
        self.fill_address_field(address)
        self.check_metro_station(metro)
        self.fill_number_field(number)
        self.click_next_button()
        self.fill_delivery_date_field(delivery_date)
        self.rental_time(rent_days)
        self.checkbox_color(colour)
        self.comment_for_courier(comment)
        self.click_order_button()
        self.click_confirmation_button()
        self.confirmation_window()
