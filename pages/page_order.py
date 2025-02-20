import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import URLs
from locators.order_locators import Order_locators
from selenium.webdriver.common.keys import Keys
from locators.FAQ_locators import FAQ_Locators



class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие браузера")
    def open_browser(self, driver):
        driver.get(URLs.MAIN_PAGE_URL)
        return self

    @allure.step("Закрытие всплывающего окна cookie (если есть)")
    def close_cookie_popup(self, driver):
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(FAQ_Locators.COOKIE_BUTTON_LOCATOR)
        )
        cookie_button.click()
        return self

    @allure.step("Нажатие на кнопку Заказать в шапке лендинга")
    def click_up_order_button(self, driver):
        driver.find_element(*Order_locators.ORDER_BUTTON_UP).click()
        return self

    @allure.step("Нажатие на кнопку Заказать в нижней части страницы")
    def click_down_order_button(self, driver):
        element = driver.find_element(*Order_locators.ORDER_BUTTON_DOWN)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return self

    @allure.step("Заполнение поля Имя")
    def fill_name_field(self, driver, name):
        driver.find_element(*Order_locators.NAME).send_keys(name)
        return self

    @allure.step("Заполнение поля Фамилия")
    def fill_surname_field(self, driver, surname):
        driver.find_element(*Order_locators.SURNAME).send_keys(surname)
        return self

    @allure.step("Заполнение поля Адрес")
    def fill_address_field(self, driver, address):
        driver.find_element(*Order_locators.ADDRESS).send_keys(address)
        return self

    @allure.step("Заполнение поля Станция метро")
    def check_metro_station(self, driver, metro):
        driver.find_element(*Order_locators.METRO).send_keys(metro)
        driver.find_element(*Order_locators.LIST_OF_STATIONS).click()
        return self

    @allure.step("Заполнение поля Телефон")
    def fill_number_field(self, driver, number):
        driver.find_element(*Order_locators.NUMBER).send_keys(number)
        return self


    @allure.step("Нажатие на кнопку Далее")
    def click_next_button(self, driver):
        driver.find_element(*Order_locators.NEXT_BUTTON).click()
        return self

    @allure.step("Выбор даты доставки")
    def fill_delivery_date_field(self, driver, data):
        driver.find_element(*Order_locators.DELIVERY_DATE).send_keys(data, Keys.ENTER)
        return self

    @allure.step("Выбор срока аренды")
    def rental_time(self, driver, day):
        driver.find_element(*Order_locators.RENT_TIME).click()
        select_rent_time_locator = (Order_locators.SELECT_RENT_TIME[0], Order_locators.SELECT_RENT_TIME[1].format(day))
        driver.find_element(*select_rent_time_locator).click()
        return self

    @allure.step("Выбор цвета")
    def checkbox_color(self, driver, color):
        if color == 'чёрный жемчуг':
            driver.find_element(*Order_locators.BLACK_COLOR_CHECKBOX).click()
        elif color == 'серая безысходность':
            driver.find_element(*Order_locators.GREY_COLOR_CHECKBOX).click()
        return self

    @allure.step("Заполнение поля Комментарии к заказу")
    def comment_for_courier(self, driver, comment):
        driver.find_element(*Order_locators.COMMENT).send_keys(comment)
        return self


    @allure.step("Нажатие на кнопку Заказать")
    def click_order_button(self, driver):
        driver.find_element(*Order_locators.ORDER_BUTTON).click()
        return self

    @allure.step("Нажатие на кнопку 'Да' в окне подтверждения заказа")
    def click_confirmation_button(self, driver):
        driver.find_element(*Order_locators.YES_BUTTON).click()
        return self

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self, driver):
        text = driver.find_element(*Order_locators.ORDER_COMPLETED).text
        assert 'Заказ оформлен' in text
        return self

    @allure.step("Полный позитивный сценарий")
    def user_order(self,
                        driver, name, surname, address, metro, number,
                        delivery_date, rent_days, colour, comment):
        self.fill_name_field(driver, name)
        self.fill_surname_field(driver, surname)
        self.fill_address_field(driver, address)
        self.check_metro_station(driver, metro)
        self.fill_number_field(driver, number)
        self.click_next_button(driver)
        self.fill_delivery_date_field(driver, delivery_date)
        self.rental_time(driver, rent_days)
        self.checkbox_color(driver, colour)
        self.comment_for_courier(driver, comment)
        self.click_order_button(driver)
        self.click_confirmation_button(driver)
        self.confirmation_window(driver)
        return self