import pytest
from utils.data import Urls, OrderData
from pages.order_page import OrderPage


class TestOrder:
    url = Urls()
    data = OrderData()

    def test_order_with_valid_user_data(self, driver):
        """"Оформление заказа используя корректные данные"""
        page = OrderPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        expected_text = page.order_with_valid_user_data(self.data.valid_user_data)
        assert (
            self.data.successful_message == expected_text
        ), f"Unexpected text. Expected: {expected_text}, Actual: {self.data.successful_message}"

    @pytest.mark.parametrize("lst_data", data.invalid_user_data)
    def test_order_with_wrong_user_data(self, driver, lst_data):
        """"Оформление заказа используя невалидные данные"""
        page = OrderPage(driver, self.url.BASE_URL)
        page.open()
        page.login()
        expected_text = page.order_with_wrong_user_data(lst_data)
        assert (
            lst_data[3] == expected_text
        ), f"Unexpected text. Expected: {expected_text}, Actual: {lst_data[3]}"
