import pytest
from selenium import webdriver
from utils.data import Login
from utils.locators import MainLocators
from pages.login_page import LoginPage
from utils.data import MainData
import allure
import os
from dotenv import load_dotenv


load_dotenv()

@allure.epic("Testing login page")
class TestLogin:
    base_url = os.getenv("BASE_URL")
    main_locators = MainLocators()
    data = MainData()

    @allure.title("test login with page title check")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login1_positive(self, driver):
        """Авторизация используя корректные данные (standard_user, secret_sauce) с проверкой хедера страницы"""
        page = LoginPage(driver, self.base_url)
        page.open()
        page.login()
        header_title = page.get_text(self.main_locators.TITLE)
        expected_header_title = self.data.header_title
        assert (
            header_title == expected_header_title
        ), f"Unexpected text. Expected: {expected_header_title}, Actual: {header_title}"

    @allure.title("test login with checking the number of products")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login2_positive(self, driver):
        """Авторизация используя корректные данные (standard_user, secret_sauce) с проверкой кол-ва карточек продуктов"""
        page = LoginPage(driver, self.base_url)
        page.open()
        page.login()
        cards_length = page.get_length(self.main_locators.CARDS)
        expected_cards_length = 6
        assert (
            cards_length == expected_cards_length
        ), f"Unexpected qty of product cards. Expected: {expected_cards_length}, Actual: {cards_length}"
