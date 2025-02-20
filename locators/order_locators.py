from selenium.webdriver.common.by import By


class Order_locators:
    # Кнопки "Заказать"
    ORDER_BUTTON_UP = [By.CLASS_NAME, "Button_Button__ra12g"]
    ORDER_BUTTON_DOWN = [By.CLASS_NAME, "Home_FinishButton__1_cWm"]

    # Форма Для кого самокат
    NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    SURNAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    LIST_OF_STATIONS = [By.XPATH, "//li[@data-index='0']"]
    NUMBER = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    # Форма Про аренду
    DELIVERY_DATE = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENT_TIME = [By.XPATH, '//div[text()="* Срок аренды"]']
    SELECT_RENT_TIME = [By.XPATH, '//div[text()="{}"]']
    BLACK_COLOR_CHECKBOX = [By.XPATH, '//label[@for="black"]']
    GREY_COLOR_CHECKBOX = [By.XPATH, '//label[@for="grey"]']
    COMMENT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    # Кнопка Да в всплывающем окне подтверждения заказа
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]

    # Текст окна "Заказ оформлен"
    ORDER_COMPLETED = [By.XPATH, '//div[contains(text(), "Заказ оформлен")]']