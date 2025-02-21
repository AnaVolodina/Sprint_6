from selenium.webdriver.common.by import By


class Logo_locators:
    SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
    YANDEX_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]
    DZEN_LOGO = [By.ID, "dzen-header"]