import pytest
from selenium import webdriver
from utils.data import Urls, Login
from utils.locators import MainLocators
from pages.login_page import LoginPage


class TestLogin:
    url = Urls()
    main_locators = MainLocators()

    def test_login_positive(self, driver):
        """Авторизация используя корректные данные (standard_user, secret_sauce)"""
        page = LoginPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        header_title = page.get_text(self.main_locators.TITLE)
        cards_length = page.get_length(self.main_locators.CARDS)
        expected_header_title = "Products"
        expected_cards_length = 6
        assert (
            header_title == expected_header_title
        ), f"Unexpected text. Expected: {expected_header_title}, Actual: {header_title}"
        assert (
            cards_length == expected_cards_length
        ), f"Unexpected qty of product cards. Expected: {expected_cards_length}, Actual: {cards_length}"
