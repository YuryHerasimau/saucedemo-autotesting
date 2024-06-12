from pages.base_page import BasePage
from utils.locators import MainLocators, LoginFormLocators
import allure


class MainPage(BasePage):
    main_locators = MainLocators()
    login_locators = LoginFormLocators()

    @allure.step("Click 'Logout'")
    def logout(self):
        self.click_on_element(self.main_locators.BURGER_MENU_BUTTON)
        self.click_on_element(self.main_locators.LOGOUT_BUTTON)

    @allure.step("Check the element is displayed")
    def check_element_is_displayed(self):
        login_form = self.element_is_visible(self.login_locators.LOGIN_FORM)
        return self.element_is_displayed(login_form)

    @allure.step("Select the dropdown item by visible text")
    def select(self, value):
        locator = self.main_locators.PRODUCT_SELECTOR
        self.select_by_visible_text(locator=locator, value=value)

    @allure.step("Get product prices")
    def get_price(self):
        lst = self.elements_are_visible(self.main_locators.PRICE_VALUE)
        return [i.text for i in lst]

    @allure.step("Check sorting by price")
    def check_sorting(self, value):
        sorted_list = self.elements_are_visible(self.main_locators.PRICE_VALUE)
        self.select(value)
        return self.get_price()

    @allure.step("Get product names")
    def get_name(self):
        lst = self.elements_are_visible(self.main_locators.PRODUCT_NAME)
        return [i.text for i in lst]

    @allure.step("Check sorting by name")
    def check_sorting_by_name(self, value):
        sorted_list = self.elements_are_visible(self.main_locators.PRODUCT_NAME)
        self.select(value)
        return self.get_name()

    @allure.step("Add SAUCE_LABS_BACKPACK to cart and get the COUNT_ITEMS value")
    def add_to_cart(self):
        self.click_on_element(self.main_locators.SAUCE_LABS_BACKPACK)
        value = self.element_is_visible(self.main_locators.COUNT_ITEMS)
        return value

    @allure.step("Remove from cart")
    def remove_from_cart(self):
        self.click_on_element(self.main_locators.REMOVE_SAUCE_LABS_BACKPACK)

    @allure.step("Check the element is not present")
    def check_element_is_not_present(self):
        return self.element_is_not_present(self.main_locators.COUNT_ITEMS)

    @allure.step("Click 'About'")
    def about(self):
        self.click_on_element(self.main_locators.BURGER_MENU_BUTTON)
        self.click_on_element(self.main_locators.ABOUT_BUTTON)

    @allure.step("Click 'Reset App State'")
    def reset_app_state(self):
        self.click_on_element(self.main_locators.BURGER_MENU_BUTTON)
        self.click_on_element(self.main_locators.RESET_APP_STATE_BUTTON)

    def check_card(self, value):
        # return self.main_locators.get_card(value=value)
        return self.main_locators.CARD_LAMBDA(value)
