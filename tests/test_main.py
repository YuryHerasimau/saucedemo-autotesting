from pages.main_page import MainPage
from utils.data import Urls, MainData
from functions.functions import sort_list
import pytest


class TestMainPage:
    url = Urls()
    main_data = MainData()

    def test_logout(self, driver):
        """Выход из системы"""
        page = MainPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        assert (
            driver.current_url == self.url.MAIN_URL
        ), f"Incorrect URL. Expected: {self.url.MAIN_URL}, Actual: {driver.current_url}"
        page.logout()
        assert (
            driver.current_url != self.url.MAIN_URL
            and driver.current_url == self.url.BASE_URL
        )
        value = page.check_element_is_displayed()
        assert value is True, "Login form is not displayed"

    @pytest.mark.parametrize("value", MainData.sorting_by_price)
    def test_select(self, driver, value):
        """Проверка работоспособности фильтра (low to high)
        Проверка работоспособности фильтра (high to low)
        """
        page = MainPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        lst = page.check_sorting(value[0])
        assert lst == sort_list(lst, value[1]), value[2]

    def test_add_item_to_cart(self, driver):
        """Добавление товара в корзину"""
        expected_value = "1"
        page = MainPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        value = page.add_to_cart()
        assert (
            value.text == expected_value
        ), f"Number of added products does not match {expected_value}"

    def test_remove_item_from_cart(self, driver):
        """Удаление товара из корзины"""
        expected_value = "1"
        page = MainPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        page.add_to_cart()
        page.remove_from_cart()
        value = page.check_element_is_not_present()
        assert value is True, "The element is present in the DOM tree"
