import pytest
from utils.data import OrderData
from pages.order_page import OrderPage
import allure
import os
from dotenv import load_dotenv


load_dotenv()


@allure.epic("Testing order page")
class TestOrder:
    base_url = os.getenv("BASE_URL")
    data = OrderData()

    @allure.title("test for placing an order with valid data")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order_with_valid_user_data(self, driver):
        """Оформление заказа используя корректные данные"""
        page = OrderPage(driver, self.base_url)
        page.open()
        page.login()
        expected_text = page.order_with_valid_user_data(self.data.valid_user_data)
        assert (
            self.data.successful_message == expected_text
        ), f"Unexpected text. Expected: {expected_text}, Actual: {self.data.successful_message}"

    @allure.title("test for placing an order with invalid data")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("lst_data", data.invalid_user_data)
    def test_order_with_wrong_user_data(self, driver, lst_data):
        """Оформление заказа используя невалидные данные"""
        page = OrderPage(driver, self.base_url)
        page.open()
        page.login()
        expected_text = page.order_with_wrong_user_data(lst_data)
        assert (
            lst_data[3] == expected_text
        ), f"Unexpected text. Expected: {expected_text}, Actual: {lst_data[3]}"
