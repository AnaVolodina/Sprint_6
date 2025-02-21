import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.page_faq import QuestionsPage
from pages.page_logo import LogoPage
from pages.page_order import OrderPage


BASE_URL = "https://qa-scooter.praktikum-services.ru/"

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture()
def questions_page(driver):
    questions_page = QuestionsPage(driver, BASE_URL)
    return questions_page

@pytest.fixture()
def logo_page(driver):
    logo_page = LogoPage(driver, BASE_URL)
    return logo_page

@pytest.fixture()
def order_page(driver):
    order_page = OrderPage (driver, BASE_URL)
    return order_page
