from pages.base_page import BasePage
from utils.locators import MainLocators, LoginFormLocators


class MainPage(BasePage):
    main_locators = MainLocators()
    login_locators = LoginFormLocators()

    def logout(self):
        self.click_on_element(self.main_locators.BURGER_MENU_BUTTON)
        self.click_on_element(self.main_locators.LOGOUT_BUTTON)

    def check_element_is_displayed(self):
        login_form = self.element_is_visible(self.login_locators.LOGIN_FORM)
        return self.element_is_displayed(login_form)

    def select(self, value):
        locator = self.main_locators.PRODUCT_SELECTOR
        self.select_by_visible_text(locator=locator, value=value)

    def get_price(self):
        lst = self.elements_are_visible(self.main_locators.PRICE_VALUE)
        return [i.text for i in lst]

    def check_sorting(self, value):
        sorted_list = self.elements_are_visible(self.main_locators.PRICE_VALUE)
        self.select(value)
        return self.get_price()

    def add_to_cart(self):
        self.click_on_element(self.main_locators.SAUCE_LABS_BACKPACK)
        value = self.element_is_visible(self.main_locators.COUNT_ITEMS)
        return value

    def remove_from_cart(self):
        self.click_on_element(self.main_locators.REMOVE_SAUCE_LABS_BACKPACK)

    def check_element_is_not_present(self):
        return self.element_is_not_present(self.main_locators.COUNT_ITEMS)
