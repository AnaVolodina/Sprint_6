import allure
from selenium.webdriver.remote.webdriver import WebDriver
from locators.order_locators import Order_locators
from selenium.webdriver.common.keys import Keys
from locators.FAQ_locators import FAQ_Locators
from pages.base_page import BasePage


class OrderPage(BasePage):
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

    @allure.step("Нажатие на кнопку Заказать в шапке лендинга")
    def click_up_order_button(self):
        self.find_element(Order_locators.ORDER_BUTTON_UP).click()

    @allure.step("Нажатие на кнопку Заказать в нижней части страницы")
    def click_down_order_button(self):
        element = self.find_element(Order_locators.ORDER_BUTTON_DOWN)
        self.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Заполнение поля Имя")
    def fill_name_field(self, name):
        self.find_element(Order_locators.NAME).send_keys(name)

    @allure.step("Заполнение поля Фамилия")
    def fill_surname_field(self, surname):
        self.find_element(Order_locators.SURNAME).send_keys(surname)

    @allure.step("Заполнение поля Адрес")
    def fill_address_field(self, address):
        self.find_element(Order_locators.ADDRESS).send_keys(address)

    @allure.step("Заполнение поля Станция метро")
    def check_metro_station(self, metro):
        self.find_element(Order_locators.METRO).send_keys(metro)
        self.find_element(Order_locators.LIST_OF_STATIONS).click()

    @allure.step("Заполнение поля Телефон")
    def fill_number_field(self, number):
        self.find_element(Order_locators.NUMBER).send_keys(number)

    @allure.step("Нажатие на кнопку Далее")
    def click_next_button(self):
        self.find_element(Order_locators.NEXT_BUTTON).click()

    @allure.step("Выбор даты доставки")
    def fill_delivery_date_field(self, delivery_date):
        self.find_element(Order_locators.DELIVERY_DATE).send_keys(delivery_date, Keys.ENTER)

    @allure.step("Выбор срока аренды")
    def rental_time(self, day):
        self.find_element(Order_locators.RENT_TIME).click()
        select_rent_time_locator = (Order_locators.SELECT_RENT_TIME[0], Order_locators.SELECT_RENT_TIME[1].format(day))
        self.find_element(select_rent_time_locator).click()

    @allure.step("Выбор цвета")
    def checkbox_color(self, color):
        if color == 'чёрный жемчуг':
            self.find_element(Order_locators.BLACK_COLOR_CHECKBOX).click()
        elif color == 'серая безысходность':
            self.find_element(Order_locators.GREY_COLOR_CHECKBOX).click()

    @allure.step("Заполнение поля Комментарии к заказу")
    def comment_for_courier(self, comment):
        self.find_element(Order_locators.COMMENT).send_keys(comment)

    @allure.step("Нажатие на кнопку Заказать")
    def click_order_button(self):
        self.find_element(Order_locators.ORDER_BUTTON).click()

    @allure.step("Нажатие на кнопку 'Да' в окне подтверждения заказа")
    def click_confirmation_button(self):
        self.find_element(Order_locators.YES_BUTTON).click()

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self):
        message = self.find_element(Order_locators.ORDER_COMPLETED)
        return message.text

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
