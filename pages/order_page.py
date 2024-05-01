from pages.base_page import BasePage
from utils.locators import CartLocators, OrderLocators, MainLocators


class OrderPage(BasePage):
    cart_locators = CartLocators()
    order_locators = OrderLocators()
    main_locators = MainLocators()

    def order_with_valid_user_data(self, lst_data):
        self.add_item_to_cart()
        self.fill_field(lst_data[0], lst_data[1], lst_data[2])
        self.click_on_element(self.order_locators.FINISH_BUTTON)
        return self.get_text(self.order_locators.SUCCESSFULL_ORDER)

    def order_with_wrong_user_data(self, lst_data):  # first_name, last_name, zip_code
        self.add_item_to_cart()
        self.fill_field(lst_data[0], lst_data[1], lst_data[2])
        return self.get_text(self.order_locators.ERROR_MESSAGE)

    def add_item_to_cart(self):
        self.element_is_clickable(self.main_locators.SAUCE_LABS_BACKPACK).click()
        self.element_is_clickable(self.main_locators.COUNT_ITEMS).click()
        self.element_is_clickable(self.cart_locators.CHECKOUT_BUTTON).click()

    def fill_field(self, first_name, last_name, zip_code):
        self.element_is_visible(self.order_locators.FIRST_NAME_FIELD).send_keys(
            first_name
        )
        self.element_is_visible(self.order_locators.LAST_NAME_FIELD).send_keys(
            last_name
        )
        self.element_is_visible(self.order_locators.ZIP_CODE_FIELD).send_keys(zip_code)
        self.element_is_clickable(self.order_locators.CONTINUE_BUTTON).click()
