from pages.main_page import MainPage
from utils.data import MainData
from functions.functions import sort_list_by_price, sort_list_by_name
import pytest
import allure
import os
import random
from dotenv import load_dotenv


load_dotenv()


@allure.epic("Testing main page")
class TestMainPage:
    base_url = os.getenv("BASE_URL")
    main_url = os.getenv("MAIN_URL")
    about_url = os.getenv("ABOUT_URL")
    main_data = MainData()

    @allure.title("test logout")
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout(self, driver):
        """Выход из системы"""
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        assert (
            driver.current_url == self.main_url
        ), f"Incorrect URL. Expected: {self.main_url}, Actual: {driver.current_url}"
        page.logout()
        assert (
            driver.current_url != self.main_url and driver.current_url == self.base_url
        )
        value = page.check_element_is_displayed()
        assert value is True, "Login form is not displayed"

    @allure.title("filter functionality test by price")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("value", MainData.sorting_by_price)
    def test_select_products_by_price(self, driver, value):
        """Проверка работоспособности фильтров (low to high) и (high to low)"""
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        lst = page.check_sorting(value[0])
        assert lst == sort_list_by_price(lst, value[1]), value[2]

    @allure.title("filter functionality test by name")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("value", MainData.sorting_by_name)
    def test_select_products_by_name(self, driver, value):
        """Проверка работоспособности фильтра (A to Z) и (Z to A)"""
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        lst = page.check_sorting_by_name(value[0])
        assert lst == sort_list_by_name(lst, value[1]), value[2]

    @allure.title("test of adding a product to cart")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_item_to_cart(self, driver):
        """Добавление товара в корзину"""
        expected_value = "1"
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        value = page.add_to_cart()
        assert (
            value.text == expected_value
        ), f"Number of added products does not match {expected_value}"

    @allure.title("test for removing a product from cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_remove_item_from_cart(self, driver):
        """Удаление товара из корзины"""
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        page.add_to_cart()
        page.remove_from_cart()
        value = page.check_element_is_not_present()
        assert value is True, "The element is present in the DOM tree"

    @allure.title("test for clicking on 'About'")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_about(self, driver):
        """Проверка работоспособности кнопки "About" в меню"""
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        page.about()
        assert (
            driver.current_url == self.about_url
        ), f"Incorrect URL. Expected: {self.about_url}, Actual: {driver.current_url}"

    @allure.title("test for clicking on 'Reset App State'")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_reset_app_state(self, driver):
        """Проверка работоспособности кнопки 'Reset App State'"""
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        page.reset_app_state()
        value = page.check_element_is_not_present()
        assert value is True, "The element is present in the DOM tree"

    @allure.title("test for checking product card names")
    @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.parametrize("value", [random.choice(range(1, 7))])
    @pytest.mark.parametrize("value", main_data.card_contents)
    def test_product_card_name(self, driver, value):
        """Проверка названий карточек товаров"""
        page = MainPage(driver, self.base_url)
        page.open()
        page.login()
        # print(page.check_card(value[0]))
        card_names = page.get_name()
        expected_text = value[1]
        assert (
            card_names[value[0]] == expected_text
        ), f"Unexpected text. Expected: {expected_text}, Actual: {card_names[value[0]]}"
