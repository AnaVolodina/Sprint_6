from selenium.webdriver.common.by import By


class FAQ_Locators:
    QUESTION = [By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    ANSWER = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]
    COOKIE_BUTTON_LOCATOR = [By.ID, "rcc-confirm-button"]